# AI Migration Assistant

## Setup

1. Create virtual environment
2. Install requirements:
   pip install -r backend/requirements.txt

3. Add .env file with OPENAI_API_KEY

4. Run backend:
   uvicorn backend.main:app --reload

5. Open frontend/index.html in browser

Perfect 👍
Here is your **complete, professional README.md** — including:

* Requirements
* API key setup
* Virtual environment creation
* Installing dependencies
* Running backend
* Running frontend
* Testing with Swagger
* Common errors
* Project structure

You can copy this directly into your `README.md`.

---

# 📄 README.md

```markdown
# 🚀 AI Migration Assistant

AI-powered .NET Upgrade & Migration Analyzer.

This tool scans a .NET project, extracts metadata and key patterns,
and generates an AI-assisted migration report for upgrading:

- .NET Framework version
- Razor
- Bootstrap
- jQuery
- NuGet packages

Powered by:
- FastAPI
- Groq (Llama 3 models)
- Python

---

# 📁 Project Structure

ai-migration-assistant/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── ai_engine.py
│   ├── file_scanner.py
│   ├── report_generator.py
│   ├── requirements.txt
│   └── uploads/
│
├── frontend/
│   ├── index.html
│   └── app.js
│
├── .env
└── README.md

---

# 🛠 Requirements

## 1️⃣ Software Requirements

- Python 3.9 or higher
- pip
- Internet connection (for Groq API)

Check Python version:

```

python --version

```

---

# 🔑 API Key Setup (Groq - Free Tier)

1. Go to:
   https://console.groq.com/

2. Create account

3. Generate API key

4. Create `.env` file in project root:

```

GROQ_API_KEY=your_groq_api_key_here

```

⚠️ Make sure there are no spaces.

---

# 🧪 Backend Setup (Step-by-Step)

## Step 1 — Navigate to backend folder

```

cd backend

```

---

## Step 2 — Create Virtual Environment

Windows:

```

python -m venv venv

```

OR

```

py -m venv venv

```

---

## Step 3 — Activate Virtual Environment

Windows PowerShell:

```

venv\Scripts\Activate

```

If execution policy error appears:

```

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

```

Then activate again.

You should see:

```

(venv) PS C:...

```

---

## Step 4 — Install Dependencies

```

pip install -r requirements.txt

```

---

## Step 5 — Run Backend Server

```

python -m uvicorn main:app --reload

```

If successful, you will see:

```

Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000)

```

---

# 🌐 Testing the Application

## Option 1 — Swagger UI (Recommended)

Open browser:

```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

```

Steps:

1. Click POST `/analyze`
2. Click "Try it out"
3. Upload a .zip file of a .NET project
4. Enter prompt (example below)
5. Click Execute

Example prompt:

```

Upgrade from .NET 7 to .NET 10 and latest Bootstrap and jQuery.

```

You will receive structured JSON migration report.

---

## Option 2 — Use Frontend UI

1. Open:

```

frontend/index.html

```

2. Upload ZIP file
3. Enter prompt
4. Click Analyze

---

# 📦 Supported Input

Currently supported:

- .zip files only

The ZIP must contain the root .NET project folder.

Example:

```

ProjectName/
Program.cs
Project.csproj
Controllers/
Views/

```

---

# 🧠 How It Works

1. Upload project ZIP
2. Extract files
3. Scan:
   - TargetFramework
   - NuGet packages
   - Program.cs patterns
   - Bootstrap & jQuery
4. Send structured metadata to AI
5. Generate migration plan
6. Return structured JSON report

---

# ⚠️ Common Errors & Fixes

## 1️⃣ 429 Rate Limit / Quota Error

Cause:
API quota exceeded

Fix:
Check Groq console for usage limits

---

## 2️⃣ Model Decommissioned Error

Fix:
Update model name in `ai_engine.py`
Refer:
https://console.groq.com/docs/models

---

## 3️⃣ JSON Parsing Error

Handled automatically.
The system cleans markdown and comments before parsing.

---

## 4️⃣ uvicorn not recognized

Use:

```

python -m uvicorn main:app --reload

```

---

# 🔒 Security Note

This is a prototype-level migration assistant.

Do NOT use for production enterprise upgrades without:
- Manual review
- Testing
- Validation

---

# 🚀 Future Improvements

- Roslyn-based semantic analysis
- CLI version
- Automated PR generation
- Risk scoring engine
- PDF report export
- Enterprise multi-project support

---

# 👨‍💻 Author

AI Migration Assistant – Prototype Version 1.0
Built for .NET Upgrade & Migration Automation
```

---

# 🎯 What You Have Now

You now have:

✔ Proper backend
✔ Free-tier AI integration
✔ Working migration analyzer
✔ Professional README
✔ Demo-ready project

---

If you want next, I can help you:

* Prepare 2–3 minute demo explanation script
* Add professional architecture diagram
* Convert this into a resume-ready project description
* Improve migration intelligence logic

Tell me what you want next 🚀
