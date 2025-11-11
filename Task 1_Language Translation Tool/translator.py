from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyperclip  # For copy feature (optional)
import pyttsx3    # For text-to-speech (optional)

# Initialize translator
translator = Translator()

# Initialize main window
root = Tk()
root.title("Language Translator")
root.geometry("600x400")
root.resizable(False, False)

# Title
Label(root, text="🌐 Language Translator", font=("Arial", 16, "bold")).pack(pady=10)

# Input text box
Label(root, text="Enter text:", font=("Arial", 12)).pack()
input_text = Text(root, height=5, width=60, wrap=WORD)
input_text.pack(pady=5)

# Dropdowns for languages
langs = list(LANGUAGES.values())

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="From:").grid(row=0, column=0, padx=5)
src_lang = ttk.Combobox(frame, values=langs, width=20)
src_lang.set("english")
src_lang.grid(row=0, column=1)

Label(frame, text="To:").grid(row=0, column=2, padx=5)
dest_lang = ttk.Combobox(frame, values=langs, width=20)
dest_lang.set("hindi")
dest_lang.grid(row=0, column=3)

# Output area
Label(root, text="Translated text:", font=("Arial", 12)).pack()
output_text = Text(root, height=5, width=60, wrap=WORD)
output_text.pack(pady=5)

# Functions
def translate_text():
    try:
        src = src_lang.get()
        dest = dest_lang.get()
        text = input_text.get("1.0", END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        # Get language codes
        src_code = [k for k, v in LANGUAGES.items() if v == src.lower()]
        dest_code = [k for k, v in LANGUAGES.items() if v == dest.lower()]

        if not src_code or not dest_code:
            messagebox.showerror("Error", "Invalid language selection!")
            return

        translated = translator.translate(text, src=src_code[0], dest=dest_code[0])
        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

def copy_text():
    pyperclip.copy(output_text.get("1.0", END).strip())
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def speak_text():
    text = output_text.get("1.0", END).strip()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "No text to speak!")

# Buttons
btn_frame = Frame(root)
btn_frame.pack(pady=10)

Button(btn_frame, text="Translate", command=translate_text, width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
Button(btn_frame, text="Copy", command=copy_text, width=10, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
Button(btn_frame, text="Speak", command=speak_text, width=10, bg="#9C27B0", fg="white").grid(row=0, column=2, padx=5)

root.mainloop()
