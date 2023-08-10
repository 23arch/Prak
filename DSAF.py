import pyautogui
import time

def interact_with_vnc():
    try:
        # Replace these coordinates with the actual coordinates on the VNC session
        vnc_x, vnc_y = 100, 100

        # Click on the VNC session at the specified coordinates
        pyautogui.click(x=vnc_x, y=vnc_y)

        # Send key 'a' to the VNC session
        pyautogui.press('a')

        # Wait for a moment
        time.sleep(2)

    except Exception as e:
        print("Error while interacting with VNC:", str(e))

if __name__ == "__main__":
    interact_with_vnc()
