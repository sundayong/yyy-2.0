import win32api, win32con, win32gui
from PIL import Image, ImageGrab
import  time

def get_window_pos(hd):
    handle = 396150  # win32gui.FindWindow(0, name)
    print(hd)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
        # text = win32gui.SetForegroundWindow(handle)
        time.sleep(1)
    return win32gui.GetWindowRect(handle)


x1, y1, x2, y2 = get_window_pos(396150)
print(x1, y1, x2, y2)
img_ready = ImageGrab.grab((x1, y1, x2, y2))
# 截图
img_ready.save("background.jpg")

if __name__ == '__main__':
    get_window_pos(123)