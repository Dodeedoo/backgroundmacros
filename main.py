import win32gui
import win32con
import win32api
import time

hwndMain = win32gui.FindWindow(None, "Lunar Client 1.8.9 (v2.7.2-2324)")
#hwndMain = win32gui.FindWindow("Zulu Platform x64 Architecture", None)
print(hwndMain)
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
print(hwndChild)

time.sleep(4)
print("starting")
#print(win32gui.ScreenToClient(hwndMain, (714, 258)))
# l_param = win32api.MAKELONG(770, 251)
# print(l_param)
# win32api.PostMessage(hwndMain, win32con.WM_LBUTTONDOWN, 0x0002, l_param)
# win32api.PostMessage(hwndMain, win32con.WM_LBUTTONUP, 0x0002,  l_param)


while True:
    temp = win32api.PostMessage(hwndMain, win32con.WM_RBUTTONDOWN, 0x0002, 0)
    print(str(temp) + " down")
    time.sleep(1)
    temp = win32api.PostMessage(hwndMain, win32con.WM_RBUTTONUP, 0x0002, 0)
    print(str(temp) + " up")