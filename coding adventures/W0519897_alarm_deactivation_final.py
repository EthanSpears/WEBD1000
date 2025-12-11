
import os
import time
import sys
import tkinter as tk
from tkinter import messagebox

PASSWORD_FILE = "passwords.txt"
MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 20

def load_passcodes(path: str):
    codes = set()
    if not os.path.exists(path):
        print(f"Password file not found: {path}")
        return codes
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
            code = raw.replace(" ", "")
            if len(code) == 5 and code.isdigit():
                codes.add(code)
            else:
                print(f"Skipping invalid code: '{raw}' (must be 5 digits)")
    return codes

def run_alarm_gui():
    valid_codes = load_passcodes(PASSWORD_FILE)
    if not valid_codes:
        print("No valid passcodes loaded. Add 5-digit codes to passwords.txt and try again.")
        return

    attempts = 0
    lockout_until = 0

    root = tk.Tk()
    root.title("Active Alarm")
    root.geometry("320x160")
    root.resizable(False, False)

    lbl = tk.Label(root, text=f"Alarm ACTIVE!\nEnter 5-digit passcode to disarm.\nLoaded codes: {len(valid_codes)}")
    lbl.pack(pady=10)

    entry = tk.Entry(root, justify="center")
    entry.pack(pady=5)
    entry.focus_set()

    status = tk.Label(root, text="", fg="red")
    status.pack(pady=5)

    def disarm():
        nonlocal attempts, lockout_until
        now = time.time()

        if now < lockout_until:
            remaining = int(lockout_until - now)
            status.config(text=f"Locked out. Try again in {remaining}s.")
            return

        code = entry.get().strip()
        if len(code) != 5 or not code.isdigit():
            status.config(text="Invalid format. Must be exactly 5 digits.")
            return

        if code in valid_codes:
            messagebox.showinfo("Alarm", "Correct code. Alarm disarmed.")
            root.destroy()
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                status.config(text=f"Wrong code. Attempts left: {remaining}.")
                entry.delete(0, tk.END)
            else:
                status.config(text=f"Too many attempts. Locked for {LOCKOUT_SECONDS}s.")
                lockout_until = time.time() + LOCKOUT_SECONDS
                attempts = 0
                entry.delete(0, tk.END)

    btn = tk.Button(root, text="Disarm", command=disarm)
    btn.pack(pady=10)

    root.mainloop()
    print("Program finished.")

if __name__ == "__main__":
    try:
        run_alarm_gui()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
