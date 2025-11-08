from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from basic_extractor import ImprovedMetalTextExtractor
import os

app = FastAPI(title="MetalOCR API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

extractor = ImprovedMetalTextExtractor()

@app.get("/")
async def serve_frontend():
    # Serve your HTML page when visiting root
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    return FileResponse(frontend_path)

@app.post("/extract_text/")
async def extract_text(file: UploadFile = File(...)):
    print(f"✅ Received file: {file.filename}")
    content = await file.read()
    extracted_text = extractor.extract_text_from_bytes(content)
    print("🔹 Sending extracted text to frontend...")
    return {"extracted_text": extracted_text}
