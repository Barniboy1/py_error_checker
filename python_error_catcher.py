import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
import importlib

def ensure_tkinterdnd2():
    try:
        import tkinterdnd2
    except ImportError:
        answer = messagebox.askyesno(
            "Missing Dependency",
            "'tkinterdnd2' is not installed.\nInstall it now?"
        )
        if answer:
            try:
                # Use the current Python interpreter
                subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinterdnd2"])
                # Dynamically reload after install
                importlib.invalidate_caches()
                globals()['tkinterdnd2'] = importlib.import_module("tkinterdnd2")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to install tkinterdnd2:\n{str(e)}")
                sys.exit()
        else:
            sys.exit("Dependency required.")

ensure_tkinterdnd2()

from tkinterdnd2 import DND_FILES, TkinterDnD

def run_python_script(path):
    output_text.delete("1.0", tk.END)
    if not path.lower().endswith(".py"):
        output_text.insert(tk.END, "⚠️ Only .py files are supported.\n")
        return

    try:
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.stdout:
            output_text.insert(tk.END, f"✅ Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"❌ Error:\n{result.stderr}\n")
        if not result.stdout and not result.stderr:
            output_text.insert(tk.END, "ℹ️ Script ran with no output or errors.\n")
    except Exception as e:
        output_text.insert(tk.END, f"❌ Critical error during execution:\n{str(e)}\n")

def on_file_drop(event):
    file_path = event.data.strip("{}").strip()
    run_python_script(file_path)

# GUI setup
app = TkinterDnD.Tk()
app.title("🐍 Python Script Error Catcher")
app.geometry("700x450")
app.configure(bg="#f5f5f5")

label = tk.Label(app, text="Drag and drop a .py file here", font=("Segoe UI", 14), bg="#f5f5f5")
label.pack(pady=10)

output_text = tk.Text(app, wrap="word", font=("Consolas", 10), bg="white", fg="black")
output_text.pack(expand=1, fill="both", padx=10, pady=10)

# Enable drag & drop
for widget in (label, output_text):
    widget.drop_target_register(DND_FILES)
    widget.dnd_bind("<<Drop>>", on_file_drop)

app.mainloop()
