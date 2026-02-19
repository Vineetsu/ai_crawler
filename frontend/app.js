const form = document.getElementById("uploadForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    result.textContent = JSON.stringify(data, null, 2);
});
