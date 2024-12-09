# app/main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from app.routes import upload, report
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(upload.router)
app.include_router(report.router)

# Ensure directories exist
UPLOAD_DIR = "uploaded_files"
REPORT_DIR = "reports"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>File Upload and Plagiarism Detection API</title>
        </head>
        <body>
            <h1>Welcome to the File Upload and Plagiarism Detection API</h1>
            <p>Use the form below to upload files and detect plagiarism.</p>
            <form action="/upload/" method="post" enctype="multipart/form-data">
                <input type="file" name="files" multiple>
                <button type="submit">Upload Files</button>
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
