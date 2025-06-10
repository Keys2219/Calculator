import tkinter as tk
from tkinter import ttk
from calculator import Calculator  # Assuming your logic is saved as calculator.py

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MARVEL Terminal Calculator")
        self.calculator = Calculator()
        self.setup_theme()
        self.create_widgets()
        self.bind_keys()

    def setup_theme(self):
        self.root.configure(bg="#1e1e1e")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("JetBrains Mono", 16), foreground="#D6E4F0", background="#2e2e2e", borderwidth=0)
        self.style.map("TButton",
                       foreground=[('pressed', '#a9bcd0'), ('active', '#b3cde0')],
                       background=[('pressed', '!disabled', '#333333'), ('active', '#3c3c3c')])

    def create_widgets(self):
        self.display_var = tk.StringVar()
        self.display = tk.Entry(self.root, textvariable=self.display_var, font=("JetBrains Mono", 28), bd=0,
                                bg="#121212", fg="#A9B7C6", insertbackground="#A9B7C6", justify='right')
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=(10, 5))
        self.display_var.set("0")

        buttons = [
            ["mc", "mr", "m+", "m-", "C"],
            ["7", "8", "9", "÷", "√"],
            ["4", "5", "6", "×", "%"],
            ["1", "2", "3", "-", "1/x"],
            ["0", ".", "±", "+", "="]
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                ttk.Button(self.root, text=char, command=lambda ch=char: self.on_button_click(ch)).grid(
                    row=r+1, column=c, sticky="nsew", padx=3, pady=3)

        for i in range(5):
            self.root.columnconfigure(i, weight=1)
        for i in range(len(buttons) + 1):
            self.root.rowconfigure(i, weight=1)

    def bind_keys(self):
        self.root.bind("<Key>", self.key_event)

    def key_event(self, event):
        result = self.calculator.handle_input(event.keysym if event.keysym in ("Enter", "Escape") else event.char)
        self.display_var.set(result)

    def on_button_click(self, char):
        result = self.calculator.handle_input(char)
        self.display_var.set(result)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.geometry("480x640")
    root.minsize(400, 500)
    root.mainloop()
