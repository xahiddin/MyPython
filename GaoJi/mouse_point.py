from ctypes import *


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    ax = int(po.x)
    ay = int(po.y)
    check(ax, ay)


def check(ax, ay):
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    bx = int(po.x)
    by = int(po.y)
    if ax != bx or ay != by:
        print(int(po.x), int(po.y))


while 1:
    get_mouse_point()
