# PrivateLens AI

## Offline & Private AI Study Assistant

PrivateLens AI is a privacy-focused, on-device AI study assistant designed to help students understand and study PDF documents without uploading their files to cloud AI services.

The current prototype focuses on PDF documents. It extracts text locally and uses a locally running **Llama 3.2 3B** model through **Ollama** to generate useful study content while keeping the user's document on their device.

---

## Problem

Students frequently use AI tools to understand lengthy academic documents, notes, and study materials. However, these documents may contain private, academic, or sensitive information.

Cloud-based AI tools may require users to upload their documents to external services and may also depend on an internet connection. This creates privacy concerns and can make AI-based studying difficult when internet access is unavailable.

---

## Proposed Solution

PrivateLens AI provides a local AI-powered study assistant for PDF documents.

Users can select a PDF and choose from different study options:

- **Summary**
- **Key Points**
- **Explain Simply**
- **Quiz Me**
- **Exam Questions**
- **Study Notes**
- **Custom Prompt**

The PDF is processed locally, and the extracted content is sent to the locally running AI model through Ollama. The document does not need to be uploaded to a cloud AI service.

---

##  Workflow

```text
PDF
 ↓
PyMuPDF
 ↓
Text Extraction
 ↓
Ollama
 ↓
Llama 3.2 3B
 ↓
Study Content
```

### Process

1. User launches PrivateLens AI.
2. User selects a PDF file.
3. Text is extracted locally using PyMuPDF.
4. User selects a study option or enters a custom prompt.
5. The extracted document content is processed by the local Llama 3.2 3B model through Ollama.
6. The generated study content is displayed in the application.

---

## Key Features

- 📄 **PDF Processing** – Extracts text from PDF documents locally.
- 📝 **AI Summarization** – Generates concise summaries.
- 📌 **Key Points** – Extracts important concepts and points.
- 💡 **Explain Simply** – Explains difficult concepts in beginner-friendly language.
- ❓ **Quiz Me** – Generates questions and answers based on the document.
- 🎓 **Exam Questions** – Creates exam-oriented questions.
- 📚 **Study Notes** – Converts document content into organized study notes.
- ✍️ **Custom Prompt** – Allows students to ask their own questions about the document.
- 🔒 **Local AI Processing** – Uses Ollama and Llama 3.2 3B locally instead of a cloud AI API.

---

##  Using the Windows App

If you are using the pre-built `PrivateLensAI.exe`, **Python is not required**.

### First-Time Setup

1. Install Ollama.
2. Open Command Prompt.
3. Run:

```bash
ollama run llama3.2:3b
```

4. Wait for the model to download.
5. Launch `PrivateLensAI.exe`.

After the initial setup:

```text
Double-click PrivateLensAI.exe
        ↓
Select PDF
        ↓
Choose study option
        ↓
Generate content
```

---

##  Running from Source

If you want to modify or run the Python source code, install Python and the required dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python PrivateLensAI.py
```

Ollama must also be installed and the Llama 3.2 3B model must be available locally.

---

## Building the Windows EXE

To build the Windows executable:

```bash
build.bat
```

The executable will be created at:

```text
dist\PrivateLensAI.exe
```

The EXE packages the Python application and its Python dependencies. It does **not** bundle the Ollama runtime or the Llama 3.2 3B model.

---

## Privacy & Offline Principle

PrivateLens AI is designed around the principle of keeping user content on the user's device.

After the initial installation of Ollama and download of the Llama 3.2 3B model, AI processing can be performed locally without requiring an internet connection or uploading the document to a cloud AI service.

---

##  Current Prototype Limitation

The current prototype primarily supports PDFs containing selectable text.

Scanned PDFs and image-based documents may require OCR, which is planned for future development.

---

##  Future Scope

The prototype can be extended with:

- OCR support for scanned PDFs
- Image understanding
- Video summarization
- Speech-to-text processing
- Chapter-wise summaries
- Better processing of large documents
- Source/page references for generated answers
- Additional student-focused study tools

---

## Core Principle

> **Useful AI for everyday studying while keeping user content private, local, and under the user's control.**

