# Test for receiving key and mouse events in Windows
# works but i jus dont feel like implementing

import ctypes
from ctypes import wintypes

WH_KEYBOARD_LL = 13
WH_MOUSE_LL = 14
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_MOUSEMOVE = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
user32 = ctypes.WinDLL("user32", use_last_error=True)

# Define the callback function types
LowLevelKeyboardProc = ctypes.WINFUNCTYPE(
    ctypes.c_long, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
LowLevelMouseProc = ctypes.WINFUNCTYPE(
    ctypes.c_long, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)


class KBDLLHOOKSTRUCT(ctypes.Structure):
  _fields_ = [
      ("vkCode", wintypes.DWORD),
      ("scanCode", wintypes.DWORD),
      ("flags", wintypes.DWORD),
      ("time", wintypes.DWORD),
      ("dwExtraInfo", wintypes.ULONG)
  ]


def keyboard_proc(nCode, wParam, lParam):
  if nCode == 0:
    kbd = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
    if wParam == WM_KEYDOWN:
      print("Key pressed:", kbd.vkCode)
    elif wParam == WM_KEYUP:
      print("Key released:", kbd.vkCode)
  return user32.CallNextHookEx(None, nCode, wParam, ctypes.c_void_p(lParam))


def mouse_proc(nCode, wParam, lParam):
  if nCode == 0:
    if wParam == WM_MOUSEMOVE:
      print("Mouse moved")
    elif wParam == WM_LBUTTONDOWN:
      print("Left mouse button down")
    elif wParam == WM_LBUTTONUP:
      print("Left mouse button up")
  return ctypes.windll.user32.CallNextHookEx(None, ctypes.c_int(nCode), ctypes.c_int(wParam), ctypes.c_void_p(lParam))


keyboard_hook = LowLevelKeyboardProc(keyboard_proc)
mouse_hook = LowLevelMouseProc(mouse_proc)
user32.SetWindowsHookExW.argtypes = [
    ctypes.c_int, LowLevelKeyboardProc, wintypes.HINSTANCE, wintypes.DWORD]
user32.SetWindowsHookExW.restype = wintypes.HHOOK
keyboard_hook_handle = user32.SetWindowsHookExW(
    WH_KEYBOARD_LL, keyboard_hook, None, 0)
mouse_hook_handle = user32.SetWindowsHookExW(WH_MOUSE_LL, mouse_hook, None, 0)

# Enter a message loop to keep the hooks active
msg = wintypes.MSG()
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
  user32.TranslateMessage(ctypes.byref(msg))
  user32.DispatchMessageW(ctypes.byref(msg))

# Unhook the hooks when done
user32.UnhookWindowsHookEx(keyboard_hook_handle)
user32.UnhookWindowsHookEx(mouse_hook_handle)
