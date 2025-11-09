# 🧠 TextVision - FastAPI OCR Text Extractor

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Built with FastAPI](https://img.shields.io/badge/Built%20with-FastAPI-green.svg)](https://fastapi.tiangolo.com/)

TextVision is a lightweight and powerful **Optical Character Recognition (OCR)** web application that extracts text from images using **FastAPI**, **OpenCV**, and **Tesseract OCR**.

It provides a clean and responsive web interface for uploading an image and instantly converting it into readable text.

---

## 🚀 Features

- 📂 Upload images (JPG, PNG, etc.)
- 🤖 Real-time OCR processing using `pytesseract`
- ⚡ FastAPI backend for fast response
- 🌐 Drag-and-drop or manual upload support
- 💡 Simple frontend (HTML + CSS + JavaScript)
- 🔁 CORS-enabled backend for smooth API communication

---

## 🏗️ Project Structure

```plaintext
TextVision/
│
├── backend/
│   ├── app.py                     # FastAPI main application
│   ├── basic_extractor.py         # Core OCR logic using OpenCV + Tesseract
│   ├── requirements.txt           # Python dependencies
│
├── frontend/
│   └── index.html                 # Frontend upload interface
│
└── README.md                      # Project documentation
