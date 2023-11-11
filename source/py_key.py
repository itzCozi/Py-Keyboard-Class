import time
import ctypes
from typing import Any
from ctypes import wintypes

# CODE
'''
* Make sure optional parameters are specifed in the
functions doc-string EX: output_path (str, optional)
* All variable declarations must be type hinted EX: num: int = 0
* All paths use '/' to separate dirs instead of '\' like windows
* All classes and functions use CamelCase variables use snake_case
* If a function has parameters each variable must have specified types
* When assigning parameters in functions dont use spaces between equals sign
* Functions without 'self' parameter in a class must have the @staticmethod tag
* Whenever in a formatted string use double quotes and then single quotes to end
* References to variables must be in double quotes EX: (var: "5" is not a number)
* If a variable or function uses more than one type use EX: num: int | float = 0.1
* When outputting a message like info or an error end the print statement with a period
'''

# TODO
'''
* Add scrolling function: https://stackoverflow.com/questions/9543397/creating-a-mouse-scroll-event-using-python
'''


class Keyboard:
  """
  A class for controlling and sending keystrokes

  -----------------------------------------
  |    function            description    |
  |---------------------------------------|
  | pressMouse: Sends a VK input to mouse |
  | releaseMouse: Halt VK signal          |
  | pressKey: Presses given key hex code  |
  | releaseKey: Stop given VK input       |
  | pressAndReleaseKey: N/A               |
  | pressAndReleaseMouse: N/A             |
  | keyboardWrite: Sends vk inputs        |
  -----------------------------------------
  """

  class _Vars:  # Variable container

    @staticmethod
    def error(
      error_type: str,
      var: str = None,
      type: str = None,
      runtime_error: str = None
    ) -> None:
      if error_type == 'p':
        print(f'PARAMETER: Given variable {var} is not a {type}.')
      elif error_type == 'r':
        print(f'RUNTIME: {runtime_error.capitalize()}.')
      elif error_type == 'u':
        print('UNKNOWN: An unknown error was encountered.')
      return None

    exit_code = None
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    INPUT_MOUSE = 0
    INPUT_KEYBOARD = 1
    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP = 0x0002
    KEYEVENTF_UNICODE = 0x0004
    KEYEVENTF_SCANCODE = 0x0008
    MAPVK_VK_TO_VSC = 0

  # Reference: https://msdn.microsoft.com/en-us/library/dd375731
  # Each key value is 4 chars long and formatted in hexadecimal
  vk_codes: dict = {
    # --- Mouse ---
    "left_mouse": 0x01,
    "right_mouse": 0x02,
    "middle_mouse": 0x04,
    "mouse_button1": 0x05,
    "mouse_button2": 0x06,
    # --- Control Keys ---
    "win": 0x5B,  # Left Windows key
    "select": 0x29,
    "pg_down": 0x21,
    "pg_up": 0x22,
    "end": 0x23,
    "home": 0x24,
    "insert": 0x2D,
    "delete": 0x2E,
    "back": 0x08,
    "enter": 0x0D,
    "shift": 0x10,
    "ctrl": 0x11,
    "alt": 0x12,
    "caps": 0x14,
    "escape": 0x1,
    "space": 0x20,
    "tab": 0x09,
    "sleep": 0x5F,
    "zoom": 0xFB,
    "num_lock": 0x90,
    "scroll_lock": 0x91,
    # --- OEM Specific ---
    "plus": 0xBB,
    "comma": 0xBC,
    "minus": 0xBD,
    "period": 0xBE,
    # --- Media ---
    "vol_mute": 0xAD,
    "vol_down": 0xAE,
    "vol_up": 0xAF,
    "next": 0xB0,
    "prev": 0xB1,
    "pause": 0xB2,
    "play": 0xB3,
    # --- Arrow Keys ---
    "left": 0x25,
    "up": 0x26,
    "right": 0x27,
    "down": 0x28,
    # --- Function Keys ---
    "f1": 0x70,
    "f2": 0x71,
    "f3": 0x72,
    "f4": 0x73,
    "f5": 0x74,
    "f6": 0x75,
    "f7": 0x76,
    "f8": 0x77,
    "f9": 0x78,
    "f10": 0x79,
    "f11": 0x7A,
    "f12": 0x7B,
    "f13": 0x7C,
    "f14": 0x7D,
    "f15": 0x7E,
    # --- Keypad ---
    "pad_0": 0x60,
    "pad_1": 0x61,
    "pad_2": 0x62,
    "pad_3": 0x63,
    "pad_4": 0x64,
    "pad_5": 0x65,
    "pad_6": 0x66,
    "pad_7": 0x67,
    "pad_8": 0x68,
    "pad_9": 0x69,
    # --- Symbols ---
    "multiply": 0x6A,
    "add": 0x6B,
    "separator": 0x6C,
    "subtract": 0x6D,
    "decimal": 0x6E,
    "divide": 0x6F,
    # --- Alphanumerical ---
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
    "a": 0x41,
    "b": 0x42,
    "c": 0x43,
    "d": 0x44,
    "e": 0x45,
    "f": 0x46,
    "g": 0x47,
    "h": 0x48,
    "i": 0x49,
    "j": 0x4A,
    "k": 0x4B,
    "l": 0x4C,
    "m": 0x4D,
    "n": 0x4E,
    "o": 0x4F,
    "p": 0x50,
    "q": 0x51,
    "r": 0x52,
    "s": 0x53,
    "t": 0x54,
    "u": 0x55,
    "v": 0x56,
    "w": 0x57,
    "x": 0x58,
    "y": 0x59,
    "z": 0x5A,
    "=": 0x6B,
    " ": 0x20,
    ".": 0xBE,
    ",": 0xBC,
    "-": 0x6D,
    "`": 0xC0,
    "/": 0xBF,
    ";": 0xBA,
    "[": 0xDB,
    "]": 0xDD,
    "_": 0x6D,   # Shift
    "|": 0xDC,   # Shift
    "~": 0xC0,   # Shift
    "?": 0xBF,   # Shift
    ":": 0xBA,   # Shift
    "<": 0xBC,   # Shift
    ">": 0xBE,   # Shift
    "{": 0xDB,   # Shift
    "}": 0xDD,   # Shift
    "!": 0x31,   # Shift
    "@": 0x32,   # Shift
    "#": 0x33,   # Shift
    "$": 0x34,   # Shift
    "%": 0x35,   # Shift
    "^": 0x36,   # Shift
    "&": 0x37,   # Shift
    "*": 0x38,   # Shift
    "(": 0x39,   # Shift
    ")": 0x30,   # Shift
    "+": 0x6B,   # Shift
    "\"": 0xDE,  # Shift
    "\'": 0xDE,
    "\\": 0xDC,
    "\n": 0x0D
  }

  # C struct declarations
  wintypes.ULONG_PTR = wintypes.WPARAM
  global MOUSEINPUT, KEYBDINPUT

  class MOUSEINPUT(ctypes.Structure):
    _fields_ = (
      ('dx', wintypes.LONG),
      ('dy', wintypes.LONG),
      ('mouseData', wintypes.DWORD),
      ('dwFlags', wintypes.DWORD),
      ('time', wintypes.DWORD),
      ('dwExtraInfo', wintypes.ULONG_PTR)
    )

  class KEYBDINPUT(ctypes.Structure):
    _fields_ = (
      ('wVk', wintypes.WORD),
      ('wScan', wintypes.WORD),
      ('dwFlags', wintypes.DWORD),
      ('time', wintypes.DWORD),
      ('dwExtraInfo', wintypes.ULONG_PTR)
    )

    def __init__(self, *args, **kwds) -> None:
      super(KEYBDINPUT, self).__init__(*args, **kwds)
      # some programs use the scan code even if KEYEVENTF_SCANCODE
      # isn't set in dwFflags, so try to map the right code
      if not self.dwFlags & Keyboard._Vars.KEYEVENTF_UNICODE:
        self.wScan = Keyboard._Vars.user32.MapVirtualKeyExW(
          self.wVk, Keyboard._Vars.MAPVK_VK_TO_VSC, 0
        )

  class INPUT(ctypes.Structure):

    class _INPUT(ctypes.Union):
      _fields_ = (('ki', KEYBDINPUT), ('mi', MOUSEINPUT))

    _anonymous_ = ('_input', )
    _fields_ = (('type', wintypes.DWORD), ('_input', _INPUT))

  LPINPUT = ctypes.POINTER(INPUT)

  # Helpers

  @staticmethod
  def _checkCount(result, func, args) -> Any:
    if result == 0:
      raise ctypes.WinError(ctypes.get_last_error())
    return args

  @staticmethod
  def _lookup(key) -> int | bool:
    if key in Keyboard.vk_codes:
      return Keyboard.vk_codes.get(key)
    else:
      return False

  _Vars.user32.SendInput.errcheck = _checkCount
  _Vars.user32.SendInput.argtypes = (
    wintypes.UINT,  # nInputs
    LPINPUT,  # pInputs
    ctypes.c_int  # cbSize
  )

  # Functions (most people will only use these)

  @staticmethod
  def pressMouse(mouse_button: str | int) -> None:
    """
    Releases a mouse button

    Args:
      mouse_button (str | int): The button to press accepted: (
        left_mouse,
        right_mouse,
        middle_mouse,
        mouse_button1,
        mouse_button
      )
    """
    mouse_list = [
      "left_mouse", 0x01, "right_mouse", 0x02, "middle_mouse", 0x04,
      "mouse_button1", 0x05, "mouse_button2", 0x06
    ]
    if mouse_button not in mouse_list and hex(mouse_button) not in mouse_list:
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not a mouse button')
      return Keyboard._Vars.exit_code

    if Keyboard._lookup(mouse_button) is not False:
      mouse_button = Keyboard._lookup(mouse_button)
    elif mouse_button not in Keyboard.vk_codes and mouse_button not in Keyboard.vk_codes.values():
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not valid')
      return Keyboard._Vars.exit_code

    x = Keyboard.INPUT(
      type=Keyboard._Vars.INPUT_MOUSE,
      mi=MOUSEINPUT(
        wVk=mouse_button,
        dwFlags=Keyboard._Vars.KEYEVENTF_KEYUP
      )
    )
    Keyboard._Vars.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

  @staticmethod
  def releaseMouse(mouse_button: str | int) -> None:
    """
    Presses a mouse button

    Args:
      mouse_button (str | int): The button to press accepted: (
        left_mouse,
        right_mouse,
        middle_mouse,
        mouse_button1,
        mouse_button
      )
    """
    mouse_list = [
      "left_mouse", 0x01, "right_mouse", 0x02, "middle_mouse", 0x04,
      "mouse_button1", 0x05, "mouse_button2", 0x06
    ]
    if mouse_button not in mouse_list and hex(mouse_button) not in mouse_list:
      Keyboard._Vars.error(
        error_type='r', runtime_error='given key code is not a mouse button'
      )
      return Keyboard._Vars.exit_code

    if Keyboard._lookup(mouse_button) is not False:
      mouse_button = Keyboard._lookup(mouse_button)
    elif mouse_button not in Keyboard.vk_codes and mouse_button not in Keyboard.vk_codes.values():
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not valid')
      return Keyboard._Vars.exit_code

    x = Keyboard.INPUT(
      type=Keyboard._Vars.INPUT_MOUSE,
      mi=MOUSEINPUT(wVk=mouse_button)
    )
    Keyboard._Vars.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

  @staticmethod
  def pressKey(key_code: str | int) -> None:
    """
    Presses a keyboard key

    Args:
      key_code (str | int): All keys in vk_codes dict are valid
    """
    if Keyboard._lookup(key_code) is not False:
      key_code = Keyboard._lookup(key_code)
    elif key_code not in Keyboard.vk_codes and key_code not in Keyboard.vk_codes.values():
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not valid')
      return Keyboard._Vars.exit_code

    x = Keyboard.INPUT(
      type=Keyboard._Vars.INPUT_KEYBOARD,
      ki=KEYBDINPUT(wVk=key_code)
    )
    Keyboard._Vars.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

  @staticmethod
  def releaseKey(key_code: str | int) -> None:
    """
    Releases a keyboard key

    Args:
      key_code (str | int): All keys in vk_codes dict are valid
    """
    if Keyboard._lookup(key_code) is not False:
      key_code = Keyboard._lookup(key_code)
    elif key_code not in Keyboard.vk_codes and key_code not in Keyboard.vk_codes.values():
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not valid')
      return Keyboard._Vars.exit_code

    x = Keyboard.INPUT(
      type=Keyboard._Vars.INPUT_KEYBOARD,
      ki=KEYBDINPUT(
        wVk=key_code,
        dwFlags=Keyboard._Vars.KEYEVENTF_KEYUP
      )
    )
    Keyboard._Vars.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

  @staticmethod
  def pressAndReleaseKey(key_code: str | int) -> None:
    """
    Presses and releases a keyboard key sequentially

    Args:
      key_code (str | int): All keys in vk_codes dict are valid
    """
    if Keyboard._lookup(key_code) is not False:
      key_code = Keyboard._lookup(key_code)
    elif key_code not in Keyboard.vk_codes and key_code not in Keyboard.vk_codes.values():
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not valid')
      return Keyboard._Vars.exit_code

    Keyboard.pressKey(key_code)
    time.sleep(0.25)
    Keyboard.releaseKey(key_code)

  @staticmethod
  def pressAndReleaseMouse(mouse_button: str | int) -> None:
    """
    Presses and releases a mouse button sequentially

    Args:
      mouse_button (str | int): The button to press accepted: (
        left_mouse,
        right_mouse,
        middle_mouse,
        mouse_button1,
        mouse_button
      )
    """
    mouse_list = [
      "left_mouse", 0x01, "right_mouse", 0x02, "middle_mouse", 0x04,
      "mouse_button1", 0x05, "mouse_button2", 0x06
    ]
    if mouse_button not in mouse_list and hex(mouse_button) not in mouse_list:
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not a mouse button')
      return Keyboard._Vars.exit_code
    original_name = mouse_button  # Keeps the original string before reassignment

    if Keyboard._lookup(mouse_button) is not False:
      mouse_button = Keyboard._lookup(mouse_button)
    elif mouse_button not in Keyboard.vk_codes and mouse_button not in Keyboard.vk_codes.values():
      Keyboard._Vars.error(error_type='r', runtime_error='given key code is not valid')
      return Keyboard._Vars.exit_code

    Keyboard.pressMouse(original_name)
    time.sleep(0.25)
    Keyboard.releaseMouse(original_name)

  @staticmethod
  def keyboardWrite(string: str) -> None:
    """
    Writes by sending virtual inputs

    Args:
      string (str): All keys in the 'Alphanumerical' section of vk_codes dict are valid
    """
    str_list = list(string)
    shift_alternate = [
      '|', '~', '?', ':', '{', '}', '\"', '!', '@', '#', '$', '%', '^', '&',
      '*', '(', ')', '+', '<', '>', '_'
    ]
    for char in str_list:
      if char not in Keyboard.vk_codes and not char.isupper():
        Keyboard._Vars.error(
          error_type='r',
          runtime_error=f'character: {char} is not in vk_codes map'
        )
        return Keyboard._Vars.exit_code

      if char.isupper() or char in shift_alternate:
        Keyboard.pressKey('shift')
      else:
        Keyboard.releaseKey('shift')

      key_code = Keyboard._lookup(char.lower())  # All dict entry's all lowercase
      x = Keyboard.INPUT(
        type=Keyboard._Vars.INPUT_KEYBOARD,
        ki=KEYBDINPUT(wVk=key_code)
      )
      Keyboard._Vars.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

      y = Keyboard.INPUT(
        type=Keyboard._Vars.INPUT_KEYBOARD,
        ki=KEYBDINPUT(
          wVk=key_code,
          dwFlags=Keyboard._Vars.KEYEVENTF_KEYUP
        )
      )
      Keyboard._Vars.user32.SendInput(1, ctypes.byref(y), ctypes.sizeof(y))
    Keyboard.releaseKey('shift')  # Incase it is not already released

  @staticmethod
  def altTab() -> None:
    """
    My development test function, just opens alt-tab menu
    """
    Keyboard.pressKey(Keyboard.vk_codes['alt'])
    Keyboard.pressKey(Keyboard.vk_codes['tab'])
    Keyboard.releaseKey(Keyboard.vk_codes['tab'])
    time.sleep(2)
    Keyboard.releaseKey(Keyboard.vk_codes['alt'])
