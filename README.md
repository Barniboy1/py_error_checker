````
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
   git clone https://github.com/Barniboy1/py_error_checker.git
````

2. Navigate to the project directory:

   ```bash
   cd py_error_checker
   ```

3. Install dependencies (if they are not automatically installed):

   ```bash
   pip install tkinterdnd2
   ```

4. **Test the application**:

   * To test the script, you can use the included test file `crash_test.py`, which will intentionally raise a `NameError` when run.
   * Simply drag and drop `crash_test.py` into the window and the error message will appear in the GUI.

5. Run the script:

   ```bash
   python py_error_checker.py
   ```

## How to Use

* Simply **drag** a `.py` file into the app window.
* The output or errors will appear in the text box inside the app.

You can use this tool to **debug** your Python scripts easily and visually. This is ideal for Python developers who want to quickly see the result of their code execution without opening a terminal.

## Screenshots

![Screenshot](screenshots/screenshot.png)

## Video Tutorial

Watch the video tutorial to see how to use the Python Script Error Catcher in action:
[YouTube Video]([https://www.youtube.com/](https://www.youtube.com/shorts/EOrPWrg3BWk)

## Contributing

Feel free to fork the repository and submit a pull request if you have improvements or fixes!

### Bug Reports and Feature Requests

If you encounter any issues or have suggestions for new features, feel free to open an issue on this repository.

## License

MIT License. See [LICENSE](LICENSE) for details.

```
