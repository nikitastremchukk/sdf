import tkinter as tk
import keyboard

# Dictionary of call signs to IDs
DATA = {
    "Кузьма": 14,
    "Ведмідь": 27,
}

# Reverse mapping for ID lookup
REVERSE = {str(v): k for k, v in DATA.items()}

root = tk.Tk()
root.withdraw()  # Hide main root window


def open_search():
    """Open a small search window."""
    window = tk.Toplevel()
    window.title("Пошук")
    entry = tk.Entry(window)
    result = tk.Label(window, text="")
    entry.pack(padx=10, pady=10)
    result.pack(padx=10, pady=(0, 10))

    def submit(event=None):
        query = entry.get().strip()
        if query in DATA:
            result.config(text=f"{query} - {DATA[query]}")
        elif query in REVERSE:
            result.config(text=f"{REVERSE[query]} - {query}")
        else:
            result.config(text="Нічого не знайдено")

    def close(event=None):
        window.destroy()

    entry.bind("<Return>", submit)
    entry.bind("<Escape>", close)
    window.bind("<FocusOut>", close)
    entry.focus()


keyboard.add_hotkey("ctrl+space", open_search)

root.mainloop()
