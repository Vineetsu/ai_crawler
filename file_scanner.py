import os
import re
import json

def extract_csproj_info(file_path):
    data = {
        "target_framework": None,
        "nuget_packages": []
    }

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

        tf_match = re.search(r"<TargetFramework>(.*?)</TargetFramework>", content)
        if tf_match:
            data["target_framework"] = tf_match.group(1)

        packages = re.findall(r'<PackageReference Include="(.*?)" Version="(.*?)"', content)
        for pkg in packages:
            data["nuget_packages"].append({
                "name": pkg[0],
                "version": pkg[1]
            })

    return data


def scan_program_file(file_path):
    patterns = [
        "UseEndpoints",
        "UseMvc",
        "AddMvc",
        "IHostingEnvironment",
        "AddAuthentication",
        "AddAuthorization"
    ]

    detected = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        for pattern in patterns:
            if pattern in content:
                detected.append(pattern)

    return detected


def scan_project(project_path):
    metadata = {
        "target_framework": None,
        "nuget_packages": [],
        "program_patterns": [],
        "bootstrap_version": None,
        "jquery_version": None
    }

    for root, dirs, files in os.walk(project_path):
        for file in files:

            if file.endswith(".csproj"):
                csproj_data = extract_csproj_info(os.path.join(root, file))
                metadata["target_framework"] = csproj_data["target_framework"]
                metadata["nuget_packages"] = csproj_data["nuget_packages"]

            if file == "Program.cs":
                patterns = scan_program_file(os.path.join(root, file))
                metadata["program_patterns"].extend(patterns)

            if file == "package.json":
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    pkg_json = json.load(f)
                    deps = pkg_json.get("dependencies", {})
                    metadata["bootstrap_version"] = deps.get("bootstrap")
                    metadata["jquery_version"] = deps.get("jquery")

            if file.endswith(".html") or file.endswith(".cshtml"):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if "bootstrap" in content.lower():
                        metadata["bootstrap_version"] = "CDN_detected"
                    if "jquery" in content.lower():
                        metadata["jquery_version"] = "CDN_detected"

    return metadata
