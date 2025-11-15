from chatbot import get_best_answer

import tkinter as tk
from tkinter import scrolledtext

# GUI window
root = tk.Tk()
root.title("FAQ Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50)
chat_window.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

def send_message():
    user_msg = entry.get()
    entry.delete(0, tk.END)

    chat_window.insert(tk.END, "You: " + user_msg + "\n")
    response = get_best_answer(user_msg)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

root.mainloop()


