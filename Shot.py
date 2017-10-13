import win32gui
import win32ui
import win32con
import win32api

desktop = win32gui.GetDesktopWindow()

width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

desktop_dc = win32gui.GetWindowDC(desktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)
mem_dc = img_dc.CreateCompatibleDC()

shot = win32ui.CreateBitmap()
shot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(shot)

mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

shot.SaveBitmapFile(mem_dc, 'E:\\yes.bmp')

mem_dc.DeleteDC()
win32gui.DeleteObject(shot.GetHandle())
