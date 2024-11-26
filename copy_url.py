import os
import subprocess
import pyperclip
from pynput import keyboard

def get_current_url():
    """
    Get the currently focused browser URL for macOS or Linux.
    """
    try:
        if os.name == "posix":
            if "darwin" in os.uname().sysname.lower():  # macOS
                script = '''
                tell application "System Events"
                    set frontApp to name of first application process whose frontmost is true
                end tell
                if frontApp is "Safari" then
                    tell application "Safari" to get URL of front document
                else if frontApp is "Google Chrome" then
                    tell application "Google Chrome" to get URL of active tab of front window
                else if frontApp is "Firefox" then
                    tell application "Firefox" to get URL of front document
                end if
                '''
                url = subprocess.check_output(["osascript", "-e", script]).decode().strip()
            else:  # Linux
                active_window = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"]).decode().strip()
                print(active_window)
                if "Firefox" in active_window or "Chrome" in active_window:
                    # Simulate Ctrl+L and Ctrl+C to copy the URL
                    subprocess.run(["xdotool", "getactivewindow", "key", "ctrl+l", "ctrl+c"])
                    url = subprocess.check_output(["xclip", "-o", "-selection", "clipboard"]).decode().strip()
                else:
                    raise Exception("Active window is not a supported browser.")
        else:
            raise Exception("Unsupported OS")
    except Exception as e:
        print(f"Error retrieving URL: {e}")
        return None

    return url

def on_press(key):
    try:
        # if key == keyboard.Key.ctrl:  # Check for Ctrl + ²
        if "²" in str(key):  # Check for Ctrl + ²
            url = get_current_url()
            if url:
                pyperclip.copy(url)
                print(f"Copied to clipboard: {url}")
            else:
                print("Could not fetch the current URL.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Listening for ² to be pressed...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()

