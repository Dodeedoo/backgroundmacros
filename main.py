import win32gui
import win32con
import win32api
import time
import random

hwndMain = win32gui.FindWindow(None, "Minecraft 1.8.9")

print(hwndMain)
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
print(hwndChild)

# time.sleep(4)
#
# l_param = win32api.MAKELONG(101, 17)
# print(l_param)
# win32api.PostMessage(hwndMain, win32con.WM_LBUTTONDBLCLK, 0x0008, l_param)
#win32api.PostMessage(hwndMain, win32con.WM_LBUTTONUP, 0x0008,  l_param)


time.sleep(4)
print("starting")

while True:
    temp = win32api.PostMessage(hwndMain, win32con.WM_LBUTTONDOWN, 0x0002, 0)
    print(str(temp) + " down")
    # secs = random.uniform(0.1, 0.5)
    time.sleep(10)
    temp = win32api.PostMessage(hwndMain, win32con.WM_LBUTTONUP, 0x0002, 0)
    print(str(temp) + " up")
    #secs = random.uniform(3.0, 4.0)
    #time.sleep(secs)