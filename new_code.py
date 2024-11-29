import pyautogui
import time
from pynput import keyboard
import platform


def press_shortcuts():
    # Determine OS-specific keys
    if platform.system() == "Darwin":  # macOS
        ctrl_key = 'command'
        option_key = 'option'
    else:  # Windows or other OS
        ctrl_key = 'ctrl'
        option_key = 'alt'

    # Perform actions using platform-specific hotkeys
    # pyautogui.hotkey(option_key, 'tab')  # Switch to Firefox
    # time.sleep(1)

    pyautogui.hotkey(ctrl_key, 'l')  # Focus on address bar
    time.sleep(0.1)

    pyautogui.hotkey(ctrl_key, 'c')  # Copy address bar content
    time.sleep(0.1)

    pyautogui.hotkey(option_key, '1')  # Switch to first tab
    time.sleep(0.1)

    pyautogui.hotkey(ctrl_key, 'v')  # Paste content
    time.sleep(0.1)

    pyautogui.press('enter')  # Press Enter


ctrl_pressed = False

def on_press(key):
    global ctrl_pressed
    try:
        # Detect Ctrl or Cmd key press
        if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.cmd, keyboard.Key.cmd_r]:
            ctrl_pressed = True
        
        if ctrl_pressed and hasattr(key, 'char') and key.char == '9':
            ctrl_pressed = False
            print("Activate SPAM")
            time.sleep(0.1)
            press_shortcuts()
            print("done")

    except AttributeError:
        pass


def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.esc:
        return False
    if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.cmd, keyboard.Key.cmd_r]:
        ctrl_pressed = False


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
