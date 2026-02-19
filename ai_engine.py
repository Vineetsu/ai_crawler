from openai import OpenAI
from config import GROQ_API_KEY
import json

# Groq OpenAI-compatible client
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def generate_ai_report(metadata, user_prompt):
    """
    Generates AI migration report using Groq Llama model.
    Ensures JSON is parsed safely even if model wraps it in markdown.
    """

    system_prompt = """
You are a senior .NET migration architect.

Analyze the project metadata and generate a structured migration plan.

IMPORTANT RULES:
- Respond ONLY with valid JSON.
- Do NOT wrap the JSON in markdown.
- Do NOT include explanations outside JSON.
"""

    user_message = f"""
Project Metadata:
{json.dumps(metadata, indent=2)}

User Request:
{user_prompt}

Output JSON format:
{{
  "summary": "",
  "csproj_changes": [],
  "program_cs_changes": [],
  "razor_changes": [],
  "bootstrap_changes": [],
  "jquery_changes": [],
  "nuget_upgrade_strategy": [],
  "risk_assessment": ""
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Updated stable Groq model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    # 🔥 Remove markdown code fences if model adds them
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    # 🔥 Try parsing JSON safely
    try:
        parsed_json = json.loads(content)
        return parsed_json

    except json.JSONDecodeError as e:
        return {
            "summary": "Model output could not be parsed as strict JSON.",
            "error": str(e),
            "raw_output": content
        }
