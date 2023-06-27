import win32gui
import time

hwndMain = win32gui.FindWindow(None, "Lunar Client 1.8.9 (v2.7.2-2324)")

time.sleep(5)

print(str(win32gui.ScreenToClient(hwndMain, win32gui.GetCursorPos())))