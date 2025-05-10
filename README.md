# Python Script Error Catcher (Drag & Drop GUI)

A simple Python script for easily debugging `.py` files with an intuitive **Drag & Drop** interface. This tool catches and displays both **outputs** and **errors** generated when running Python scripts, allowing for easy troubleshooting.

## Features

- **Drag & Drop Interface**: Simply drag a `.py` file onto the app to execute it and view the output or errors.
- **Instant Error Reporting**: Displays Python script errors (and outputs) directly in the GUI, so you don't need to check the terminal.
- **Automatic Package Installation**: If `tkinterdnd2` is missing, the script will automatically install it with admin privileges.
- **Cross-platform**: Works on Windows, Linux, and macOS (with minor adjustments).

## How It Works

1. **Drag** any `.py` file and drop it onto the GUI.
2. The script will run and **capture the output or errors**.
3. The results will be displayed in the application window in real-time.
4. If `tkinterdnd2` is missing, the script will **prompt** you to install it (with admin privileges) and continue without restarting the app.

## Installation

### Prerequisites

- Python 3.x
- `tkinterdnd2` package (will be installed automatically if missing)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/py_error_checker.git
