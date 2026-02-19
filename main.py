from fastapi import FastAPI, UploadFile, File, Form
import shutil
import zipfile
import os

from file_scanner import scan_project
from ai_engine import generate_ai_report
from report_generator import format_report

app = FastAPI()

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.post("/analyze")
async def analyze_project(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):
    zip_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(zip_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extract_path = zip_path.replace(".zip", "")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    metadata = scan_project(extract_path)

    ai_report = generate_ai_report(metadata, prompt)

    final_report = format_report(ai_report)

    return final_report
