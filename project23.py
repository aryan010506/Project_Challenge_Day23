import tkinter as tk
from tkinter import scrolledtext
import random

# ----- BASIC RESPONSES -----
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you today?"],
    "how are you": ["I'm doing great, thanks!", "I'm fine, how about you?"],
    "your name": ["I'm your Python chatbot.", "I'm a simple NLP chatbot made in Python."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that yet."

# ----- FUNCTIONS -----
def send_message(event=None):
    user_message = entry.get().strip()
    if user_message == "" or user_message == "Type your message here...":
        return
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_message + "\n")
    response = get_response(user_message)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)
    entry.delete(0, tk.END)

def on_entry_click(event):
    """Function to clear placeholder text when clicked."""
    if entry.get() == 'Type your message here...':
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focusout(event):
    """Function to put placeholder back if empty."""
    if entry.get() == '':
        entry.insert(0, 'Type your message here...')
        entry.config(fg='grey')

# ----- GUI -----
root = tk.Tk()
root.title("Python Chatbot")
root.geometry("500x600")
root.configure(bg="white")

# Title label
label = tk.Label(root, text="🤖 Basic NLP Chatbot", font=("Helvetica", 18, "bold"), bg="white")
label.pack(pady=10)

# Chat window with scrollbar
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Helvetica", 12), width=60, height=25)
chat_window.pack(padx=10, pady=10)

# Entry frame
entry_frame = tk.Frame(root, bg="white")
entry_frame.pack(padx=10, pady=10, fill=tk.X)

# Entry box with placeholder
entry = tk.Entry(entry_frame, font=("Helvetica", 12), width=45, fg='grey')
entry.pack(side=tk.LEFT, padx=(0,10), pady=5, fill=tk.X, expand=True)
entry.insert(0, 'Type your message here...')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)

# Send button
send_button = tk.Button(entry_frame, text="Send", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=send_message)
send_button.pack(side=tk.RIGHT)

# Bind Enter key to send
root.bind('<Return>', send_message)

root.mainloop()
