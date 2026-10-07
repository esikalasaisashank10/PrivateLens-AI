import tkinter as tk
from tkinter import filedialog, messagebox
import fitz
import ollama
import os

MODEL = "llama3.2:3b"
text = ""

def select_pdf():
    global text
    file_path = filedialog.askopenfilename(
        title="Select a PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not file_path:
        return
    try:
        status_label.config(text="Reading PDF...")
        window.update()
        doc = fitz.open(file_path)
        text = "\n".join(page.get_text() for page in doc)
        doc.close()

        if not text.strip():
            messagebox.showwarning(
                "No text found",
                "This PDF does not contain selectable text. OCR support can be added later."
            )
            generate_button.config(state="disabled")
            status_label.config(text="No readable text found")
            return

        file_label.config(text=os.path.basename(file_path))
        status_label.config(text="PDF loaded ✓")
        generate_button.config(state="normal")
    except Exception as e:
        messagebox.showerror("PDF Error", str(e))
        status_label.config(text="Could not read PDF")

def generate_content():
    if not text:
        return

    user_prompt = prompt_box.get("1.0", tk.END).strip()

    instructions = {
        "Summary": """Summarize this document in simple language.
Give:
1. Short overview
2. Main points
3. Important concepts""",
        "Key Points": """Extract the most important points from this document.
Explain each point briefly in simple language.""",
        "Explain Simply": """Explain the important concepts from this document
as if you are teaching a beginner student.
Use simple language and small examples where useful.""",
        "Quiz Me": """Create 10 questions based ONLY on this document.
Give the questions first and then provide the answers.""",
        "Exam Questions": """Create 10 useful exam-oriented questions based ONLY
on this document. Include short-answer and descriptive questions.
Provide answers after the questions.""",
        "Study Notes": """Convert this document into organized study notes.
Use headings, subheadings, important definitions, key concepts,
examples, and important points. Keep the language simple."""
    }

    instruction = user_prompt or instructions[mode_var.get()]

    prompt = f"""{instruction}

IMPORTANT:
- Use ONLY the information contained in the document.
- If the document does not contain enough information, say so.
- Do not invent facts.

DOCUMENT:
{text}
"""

    status_label.config(text="AI is processing locally...")
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Generating response locally...")
    generate_button.config(state="disabled")
    window.update()

    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        result = response["message"]["content"]
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
        status_label.config(text="Completed ✓ • Processed locally")
    except Exception as e:
        output.delete("1.0", tk.END)
        output.insert(tk.END,
            "Could not connect to the local AI model.\n\n"
            "Make sure Ollama is installed and run:\n"
            "ollama run llama3.2:3b\n\n"
            f"Technical details:\n{e}"
        )
        status_label.config(text="Local AI connection failed")
    finally:
        generate_button.config(state="normal")

window = tk.Tk()
window.title("PrivateLens AI")
window.geometry("900x720")
window.minsize(800, 650)
window.configure(bg="#f4f6f8")

tk.Label(window, text="PrivateLens AI", font=("Arial", 26, "bold"),
         bg="#f4f6f8").pack(pady=(20, 4))
tk.Label(window, text="Your private, offline AI study assistant",
         font=("Arial", 12), bg="#f4f6f8").pack()
tk.Label(window, text="🔒 Your document stays on this device",
         font=("Arial", 10), bg="#f4f6f8").pack(pady=(5, 18))

tk.Button(window, text="📄  Select PDF", command=select_pdf,
          font=("Arial", 12, "bold"), padx=20, pady=8).pack()

file_label = tk.Label(window, text="No PDF selected",
                      font=("Arial", 10), bg="#f4f6f8")
file_label.pack(pady=7)

tk.Label(window, text="Choose a study action",
         font=("Arial", 11, "bold"), bg="#f4f6f8").pack(pady=(8, 4))

mode_var = tk.StringVar(value="Summary")
mode_menu = tk.OptionMenu(
    window, mode_var,
    "Summary", "Key Points", "Explain Simply",
    "Quiz Me", "Exam Questions", "Study Notes"
)
mode_menu.config(font=("Arial", 10), width=20)
mode_menu.pack()

tk.Label(window, text="Or ask your own question",
         font=("Arial", 11, "bold"), bg="#f4f6f8").pack(pady=(13, 5))

prompt_box = tk.Text(window, height=3, width=85,
                     font=("Arial", 11), wrap=tk.WORD)
prompt_box.pack(padx=30)

generate_button = tk.Button(
    window, text="Generate", command=generate_content,
    state="disabled", font=("Arial", 12, "bold"),
    padx=30, pady=8
)
generate_button.pack(pady=10)

status_label = tk.Label(window, text="Select a PDF to begin",
                        font=("Arial", 10), bg="#f4f6f8")
status_label.pack()

output = tk.Text(window, height=18, width=95,
                 font=("Arial", 11), wrap=tk.WORD)
output.pack(padx=30, pady=14, fill=tk.BOTH, expand=True)

window.mainloop()
