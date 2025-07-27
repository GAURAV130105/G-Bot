import tkinter as tk
from tkinter import Toplevel, scrolledtext, messagebox
from PIL import Image, ImageTk, Image


qa_pairs = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hey there! 👋 How can I help?",
    "what is your name": "I'm G-Bot, your friendly assistant!",
    "who made you": "I was created by Gaurav using Python.",
    "how are you": "I'm doing great! How can I assist you?",
    "what can you do": "I can answer basic questions and guide you.",
    "hello": "Hey there! 👋",
    "help": "Sure! What do you need help with?",
    "thank you": "You're welcome! 😊",
    "ok": "Great! If you have any questions, just ask.",
    "yes": "Awesome! How can I assist you?",
    "no": "Alright! If you change your mind, just let me know.",
    "do you know python": "Yes, I know Python! It's a great programming language.",
    "thanks": "No problem! If you have more questions, just ask.",
    "goodbye": "Goodbye! If you need anything else, just ask.",
    "bye": "Goodbye! Have a nice day!"
}


def get_response(user_input):
    user_input = user_input.lower().strip()
    return qa_pairs.get(user_input, "Sorry, I don’t have that knowledge. I’ll improve soon!")

def open_chat_window():
    chat_window = Toplevel(root)
    chat_window.title("G-Bot Chat")
    chat_window.geometry("400x500")

    chat_display = scrolledtext.ScrolledText(chat_window, wrap=tk.WORD, width=50, height=20, font=("Arial", 10))
    chat_display.pack(pady=10)
    chat_display.config(state=tk.DISABLED)

    entry = tk.Entry(chat_window, width=40)
    entry.pack(pady=5)

    def send_message():
        user_msg = entry.get()
        if not user_msg:
            messagebox.showinfo("Empty", "Please type something!")
            return
        entry.delete(0, tk.END)

        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"You: {user_msg}\n")

        response = get_response(user_msg)
        chat_display.insert(tk.END, f"G-Bot: {response}\n\n")
        chat_display.config(state=tk.DISABLED)

    send_btn = tk.Button(chat_window, text="Send", command=send_message)
    send_btn.pack()


root = tk.Tk()
root.title("Mascot Chat Launcher")
root.geometry("250x300")
root.resizable(False, False)


img_path = "chatbot/Mascot.png"  # Replace with your mascot path
mascot_img = Image.open(img_path).resize((150, 150), Image.Resampling.LANCZOS)
mascot_photo = ImageTk.PhotoImage(mascot_img)

mascot_label = tk.Label(root, image=mascot_photo, cursor="hand2")
mascot_label.pack(pady=5)

info_label = tk.Label(root, text="How May I Assist You Today", font=("Arial", 10))
info_label.pack()


mascot_label.bind("<Button-1>", lambda e: open_chat_window())

root.mainloop()
