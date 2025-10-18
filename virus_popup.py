import tkinter as tk
from tkinter import messagebox
import threading
import time
import sys
import winsound
import keyboard  # install via: pip install keyboard

def show_popup():
    while True:
        time.sleep(10)
        winsound.MessageBeep(winsound.MB_ICONHAND)  # Windows error sound
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Windows Defender Alert",
            "⚠ Threat Detected: A virus has been found on your computer.\nImmediate action is recommended."
        )
        root.destroy()

def check_for_escape():
    while True:
        if keyboard.is_pressed('esc'):
            print("[Exit] ESC key detected. Closing.")
            sys.exit()

if __name__ == "__main__":
    print("Fake virus alert started. Press ESC to stop.")

    threading.Thread(target=show_popup, daemon=True).start()
    threading.Thread(target=check_for_escape, daemon=True).start()

    while True:
        time.sleep(1)
