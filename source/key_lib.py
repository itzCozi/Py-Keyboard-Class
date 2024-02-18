import win32api          #line:5
import ctypes          #line:6
import time          #line:7
from typing import *         #line:9
from win32con import *         #line:10
from ctypes import wintypes          #line:11
from win32api import STD_INPUT_HANDLE          #line:12
from win32console import (GetStdHandle ,KEY_EVENT ,ENABLE_ECHO_INPUT ,ENABLE_LINE_INPUT ,ENABLE_PROCESSED_INPUT )         #line:16
class Keyboard :         #line:20
  ""         #line:40
  class _Vars :         #line:42
    ""         #line:45
    @staticmethod          #line:47
    def error (OOOOO0O0O00O0O0O0 :str ,O0OOOO0O00OO0000O :str =None ,O000OOOO0OO000O00 :str =None ,O0OOO0O00OOOOOOO0 :str =None )->None :         #line:53
      ""         #line:56
      if OOOOO0O0O00O0O0O0 =='p':         #line:57
        print (f'PARAMETER: Given variable {O0OOOO0O00OO0000O} is not a {O000OOOO0OO000O00}.')         #line:58
      elif OOOOO0O0O00O0O0O0 =='r':         #line:59
        print (f'RUNTIME: {O0OOO0O00OOOOOOO0.capitalize()}.')         #line:60
      elif OOOOO0O0O00O0O0O0 =='u':         #line:61
        print ('UNKNOWN: An unknown error was encountered.')         #line:62
      return None          #line:63
    exit_code :None =None          #line:65
    INPUT_MOUSE :int =0          #line:66
    INPUT_KEYBOARD :int =1          #line:67
    MAPVK_VK_TO_VSC :int =0          #line:68
    KEYEVENTF_KEYUP :int =0x0002          #line:69
    KEYEVENTF_UNICODE :int =0x0004          #line:70
    KEYEVENTF_SCANCODE :int =0x0008          #line:71
    KEYEVENTF_EXTENDEDKEY :int =0x0001          #line:72
    user32 :ctypes .WinDLL =ctypes .WinDLL ('user32',use_last_error =True )         #line:73
  vk_codes :dict ={"left_mouse":0x01 ,"right_mouse":0x02 ,"middle_mouse":0x04 ,"mouse_button1":0x05 ,"mouse_button2":0x06 ,"win":0x5B ,"select":0x29 ,"pg_down":0x21 ,"pg_up":0x22 ,"end":0x23 ,"home":0x24 ,"insert":0x2D ,"delete":0x2E ,"back":0x08 ,"enter":0x0D ,"shift":0x10 ,"ctrl":0x11 ,"alt":0x12 ,"caps":0x14 ,"escape":0x1B ,"space":0x20 ,"tab":0x09 ,"sleep":0x5F ,"zoom":0xFB ,"num_lock":0x90 ,"scroll_lock":0x91 ,"plus":0xBB ,"comma":0xBC ,"minus":0xBD ,"period":0xBE ,"vol_mute":0xAD ,"vol_down":0xAE ,"vol_up":0xAF ,"next":0xB0 ,"prev":0xB1 ,"pause":0xB2 ,"play":0xB3 ,"left":0x25 ,"up":0x26 ,"right":0x27 ,"down":0x28 ,"f1":0x70 ,"f2":0x71 ,"f3":0x72 ,"f4":0x73 ,"f5":0x74 ,"f6":0x75 ,"f7":0x76 ,"f8":0x77 ,"f9":0x78 ,"f10":0x79 ,"f11":0x7A ,"f12":0x7B ,"f13":0x7C ,"f14":0x7D ,"f15":0x7E ,"pad_0":0x60 ,"pad_1":0x61 ,"pad_2":0x62 ,"pad_3":0x63 ,"pad_4":0x64 ,"pad_5":0x65 ,"pad_6":0x66 ,"pad_7":0x67 ,"pad_8":0x68 ,"pad_9":0x69 ,"multiply":0x6A ,"add":0x6B ,"separator":0x6C ,"subtract":0x6D ,"decimal":0x6E ,"divide":0x6F ,"0":0x30 ,"1":0x31 ,"2":0x32 ,"3":0x33 ,"4":0x34 ,"5":0x35 ,"6":0x36 ,"7":0x37 ,"8":0x38 ,"9":0x39 ,"a":0x41 ,"b":0x42 ,"c":0x43 ,"d":0x44 ,"e":0x45 ,"f":0x46 ,"g":0x47 ,"h":0x48 ,"i":0x49 ,"j":0x4A ,"k":0x4B ,"l":0x4C ,"m":0x4D ,"n":0x4E ,"o":0x4F ,"p":0x50 ,"q":0x51 ,"r":0x52 ,"s":0x53 ,"t":0x54 ,"u":0x55 ,"v":0x56 ,"w":0x57 ,"x":0x58 ,"y":0x59 ,"z":0x5A ,"=":0x6B ," ":0x20 ,".":0xBE ,",":0xBC ,"-":0x6D ,"`":0xC0 ,"/":0xBF ,";":0xBA ,"[":0xDB ,"]":0xDD ,"_":0x6D ,"|":0xDC ,"~":0xC0 ,"?":0xBF ,":":0xBA ,"<":0xBC ,">":0xBE ,"{":0xDB ,"}":0xDD ,"!":0x31 ,"@":0x32 ,"         #":0x33 ,"$":0x34 ,"%":0x35 ,"^":0x36 ,"&":0x37 ,"*":0x38 ,"(":0x39 ,")":0x30 ,"+":0x6B ,"\"":0xDE ,"\'":0xDE ,"\\":0xDC ,"\n":0x0D }         #line:229
  wintypes .ULONG_PTR :type [wintypes .WPARAM ]=wintypes .WPARAM          #line:232
  global MOUSEINPUT ,KEYBDINPUT          #line:233
  class MOUSEINPUT (ctypes .Structure ):         #line:235
    _fields_ :tuple [tuple [Literal ['dx'],wintypes .LONG ],tuple [Literal ['dy'],wintypes .LONG ],tuple [Literal ['mouseData'],wintypes .DWORD ],tuple [Literal ['dwFlags'],wintypes .DWORD ],tuple [Literal ['time'],wintypes .DWORD ],tuple [Literal ['dwExtraInfo'],type [wintypes .WPARAM ]]]=(('dx',wintypes .LONG ),('dy',wintypes .LONG ),('mouseData',wintypes .DWORD ),('dwFlags',wintypes .DWORD ),('time',wintypes .DWORD ),('dwExtraInfo',wintypes .ULONG_PTR ))         #line:250
  class KEYBDINPUT (ctypes .Structure ):         #line:252
    _fields_ :tuple [tuple [Literal ['wVk'],wintypes .WORD ],tuple [Literal ['wScan'],wintypes .WORD ],tuple [Literal ['dwFlags'],wintypes .DWORD ],tuple [Literal ['time'],wintypes .DWORD ],tuple [Literal ['dwExtraInfo'],type [wintypes .WPARAM ]]]=(('wVk',wintypes .WORD ),('wScan',wintypes .WORD ),('dwFlags',wintypes .DWORD ),('time',wintypes .DWORD ),('dwExtraInfo',wintypes .ULONG_PTR ))         #line:265
    def __init__ (O0OOO000OOO0OO00O :Self ,*OO0O0OOOOO000O000 :tuple [Any ,...],**OOOO0O000OO0000OO :dict [str ,Any ])->None :         #line:271
      super (KEYBDINPUT ,O0OOO000OOO0OO00O ).__init__ (*OO0O0OOOOO000O000 ,**OOOO0O000OO0000OO )         #line:273
      if not O0OOO000OOO0OO00O .dwFlags &Keyboard ._Vars .KEYEVENTF_UNICODE :         #line:274
        O0OOO000OOO0OO00O .wScan :Any =Keyboard ._Vars .user32 .MapVirtualKeyExW (O0OOO000OOO0OO00O .wVk ,Keyboard ._Vars .MAPVK_VK_TO_VSC ,0 )         #line:277
  class INPUT (ctypes .Structure ):         #line:279
    class _INPUT (ctypes .Union ):         #line:281
      _fields_ :tuple [tuple [Literal ['ki'],type [KEYBDINPUT ]],tuple [Literal ['mi'],type [MOUSEINPUT ]]]=(('ki',KEYBDINPUT ),('mi',MOUSEINPUT ))         #line:285
    _anonymous_ :tuple [Literal ['_input']]=('_input',)         #line:287
    _fields_ :tuple [tuple [Literal ['type'],wintypes .DWORD ],tuple [Literal ['_input'],type [_INPUT ]]]=(('type',wintypes .DWORD ),('_input',_INPUT ))         #line:291
  LPINPUT :Any =ctypes .POINTER (INPUT )         #line:293
  @staticmethod          #line:297
  def _checkCount (O0OOO0O0OO0O00O00 :Any ,OOO0O0OO00OOO0OO0 :Any ,OO0O0O000O000OO0O :Any )->Any :         #line:298
    if O0OOO0O0OO0O00O00 ==0 :         #line:299
      raise ctypes .WinError (ctypes .get_last_error ())         #line:300
    return OO0O0O000O000OO0O          #line:301
  @staticmethod          #line:303
  def _lookup (OOOOO00O0O0O00OOO :Any )->int |bool :         #line:304
    if OOOOO00O0O0O00OOO in Keyboard .vk_codes :         #line:305
      return Keyboard .vk_codes .get (OOOOO00O0O0O00OOO )         #line:306
    else :         #line:307
      return False          #line:308
  @staticmethod          #line:310
  def mouseScroll (O00OOO0O000O000OO :str ,OOOOO00O0OOO0O000 :int ,OOO0O00O0OO0O0O00 :int =0 ,OO0O00O0O00OOOO00 :int =0 )->None |bool :         #line:311
    if O00OOO0O000O000OO =='v'or O00OOO0O000O000OO =='vertical':         #line:312
      win32api .mouse_event (MOUSEEVENTF_WHEEL ,OOO0O00O0OO0O0O00 ,OO0O00O0O00OOOO00 ,OOOOO00O0OOO0O000 ,0 )         #line:313
    elif O00OOO0O000O000OO =='h'or O00OOO0O000O000OO =='horizontal':         #line:314
      win32api .mouse_event (MOUSEEVENTF_HWHEEL ,OOO0O00O0OO0O0O00 ,OO0O00O0O00OOOO00 ,OOOOO00O0OOO0O000 ,0 )         #line:315
    else :         #line:316
      return False          #line:317
  class ManipulateMouse :         #line:319
    ""         #line:326
    @staticmethod          #line:328
    def getPosition ()->tuple :         #line:329
      ""         #line:332
      class OO0OOO0OO00OO00OO (ctypes .Structure ):         #line:334
        _fields_ :list =[("x",ctypes .c_long ),("y",ctypes .c_long )]         #line:335
      OOO0OOO0O0OO00OO0 :OO0OOO0OO00OO00OO =OO0OOO0OO00OO00OO ()         #line:337
      ctypes .windll .user32 .GetCursorPos (ctypes .byref (OOO0OOO0O0OO00OO0 ))         #line:338
      return (OOO0OOO0O0OO00OO0 .x ,OOO0OOO0O0OO00OO0 .y )         #line:339
    @staticmethod          #line:341
    def setPosition (OOO0OOO0OOOO00O0O :int ,O0OOOO0O0000O00OO :int )->None :         #line:342
      ""         #line:345
      ctypes .windll .user32 .SetCursorPos (OOO0OOO0OOOO00O0O ,O0OOOO0O0000O00OO )         #line:346
  class GetKeystroke :         #line:348
    ""         #line:362
    def __init__ (OOO000O000OOOOO00 :Self )->None :         #line:364
      ""         #line:367
      OOO000O000OOOOO00 .cur_event_len :None |int =None          #line:368
    def __enter__ (O00O00OOOOOO0O00O :Self )->Any :         #line:370
      ""         #line:373
      O00O00OOOOOO0O00O .readHandle :Any =GetStdHandle (STD_INPUT_HANDLE )         #line:374
      O00O00OOOOOO0O00O .readHandle .SetConsoleMode (ENABLE_LINE_INPUT |ENABLE_ECHO_INPUT |ENABLE_PROCESSED_INPUT )         #line:377
      O00O00OOOOOO0O00O .cur_event_len :int =0          #line:379
      O00O00OOOOOO0O00O .cur_keys_len :int =0          #line:380
      O00O00OOOOOO0O00O .captured_chars :list =[]         #line:381
      return O00O00OOOOOO0O00O          #line:383
    def __exit__ (O0O0OO000O0OOO000 :Self ,OO00O00OOOO00O000 :Any ,OOO00OO0OO0OO0OOO :Any ,O00O0O00O0O00000O :Any )->None :         #line:385
      ""         #line:388
      pass          #line:389
    def poll (O00OO0OOOOOOO0OOO :Self )->str |None :         #line:392
      ""         #line:398
      if not len (O00OO0OOOOOOO0OOO .captured_chars )==0 :         #line:399
        return O00OO0OOOOOOO0OOO .captured_chars .pop (0 )         #line:400
      O00OO000O00O00OOO :tuple =O00OO0OOOOOOO0OOO .readHandle .PeekConsoleInput (10000 )         #line:401
      if len (O00OO000O00O00OOO )==0 :         #line:403
        return None          #line:404
      if not len (O00OO000O00O00OOO )==O00OO0OOOOOOO0OOO .cur_event_len :         #line:406
        for OO0O00OOOO0O00O00 in O00OO000O00O00OOO [O00OO0OOOOOOO0OOO .cur_event_len :]:         #line:408
          if OO0O00OOOO0O00O00 .EventType ==KEY_EVENT :         #line:409
            if ord (OO0O00OOOO0O00O00 .Char )==0 or not OO0O00OOOO0O00O00 .KeyDown :         #line:410
              pass          #line:411
            else :         #line:412
              O00OO0000O0OOOOOO :str =str (OO0O00OOOO0O00O00 .Char )         #line:413
              O00OO0OOOOOOO0OOO .captured_chars .append (O00OO0000O0OOOOOO )         #line:414
        O00OO0OOOOOOO0OOO .cur_event_len :int =len (O00OO000O00O00OOO )         #line:416
      if not len (O00OO0OOOOOOO0OOO .captured_chars )==0 :         #line:417
        return O00OO0OOOOOOO0OOO .captured_chars .pop ()         #line:418
  _Vars .user32 .SendInput .errcheck :Any =_checkCount          #line:420
  _Vars .user32 .SendInput .argtypes :Any =(wintypes .UINT ,LPINPUT ,ctypes .c_int )         #line:425
  @staticmethod          #line:429
  def getKeyState (OOO0OOOOO0000O0O0 :str |int )->bool :         #line:430
    ""         #line:439
    if not isinstance (OOO0OOOOO0000O0O0 ,str |int ):         #line:440
      Keyboard ._Vars .error (error_type ='p',var ='key_code',type ='integer or string')         #line:441
      return Keyboard ._Vars .exit_code          #line:442
    if Keyboard ._lookup (OOO0OOOOO0000O0O0 )is not False :         #line:444
      OOO0OOOOO0000O0O0 :int =Keyboard ._lookup (OOO0OOOOO0000O0O0 )         #line:445
    elif OOO0OOOOO0000O0O0 not in Keyboard .vk_codes and OOO0OOOOO0000O0O0 not in Keyboard .vk_codes .values ():         #line:446
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not valid')         #line:447
      return Keyboard ._Vars .exit_code          #line:448
    O00O00000OOO00O0O :int =Keyboard ._Vars .user32 .GetKeyState (OOO0OOOOO0000O0O0 )         #line:450
    if O00O00000OOO00O0O ==1 :         #line:451
      OO0O0O0O000O00O0O :bool =True          #line:452
    else :         #line:453
      OO0O0O0O000O00O0O :bool =False          #line:454
    if 'key_state'in locals ():         #line:456
      return OO0O0O0O000O00O0O          #line:457
    else :         #line:458
      Keyboard ._Vars .error (error_type ='r',runtime_error ='user32 returned a non "1" or "0" value')         #line:461
      return Keyboard ._Vars .exit_code          #line:462
  @staticmethod          #line:464
  def locateCursor ()->Tuple [int ,int ]:         #line:465
    ""         #line:471
    return Keyboard .ManipulateMouse .getPosition ()         #line:474
  @staticmethod          #line:476
  def moveCursor (O0OOO0O000OO0O00O :int ,O000O00OOO00OO000 :int )->None :         #line:477
    ""         #line:484
    if not isinstance (O0OOO0O000OO0O00O ,int ):         #line:485
      Keyboard ._Vars .error (error_type ='p',var ='x',type ='integer')         #line:486
      return Keyboard ._Vars .exit_code          #line:487
    if not isinstance (O000O00OOO00OO000 ,int ):         #line:488
      Keyboard ._Vars .error (error_type ='p',var ='y',type ='integer')         #line:489
      return Keyboard ._Vars .exit_code          #line:490
    Keyboard .ManipulateMouse .setPosition (O0OOO0O000OO0O00O ,O000O00OOO00OO000 )         #line:493
  @staticmethod          #line:495
  def scrollMouse (O0O00O0OOO0000O00 :str ,O0O0OOOO000O0O0OO :int ,OO00OO00O0O000O00 :int =0 ,OOO0000OOOO0O0OOO :int =0 )->None :         #line:496
    ""         #line:507
    if not isinstance (O0O00O0OOO0000O00 ,str ):         #line:508
      Keyboard ._Vars .error (error_type ='p',var ='direction',type ='string')         #line:509
      return Keyboard ._Vars .exit_code          #line:510
    if not isinstance (O0O0OOOO000O0O0OO ,int ):         #line:511
      Keyboard ._Vars .error (error_type ='p',var ='amount',type ='integer')         #line:512
      return Keyboard ._Vars .exit_code          #line:513
    if not isinstance (OO00OO00O0O000O00 ,int ):         #line:514
      Keyboard ._Vars .error (error_type ='p',var ='dx',type ='integer')         #line:515
      return Keyboard ._Vars .exit_code          #line:516
    if not isinstance (OOO0000OOOO0O0OOO ,int ):         #line:517
      Keyboard ._Vars .error (error_type ='p',var ='dy',type ='integer')         #line:518
      return Keyboard ._Vars .exit_code          #line:519
    O0OOOOO00OOOO000O :list =['up','down','left','right']         #line:521
    if O0O00O0OOO0000O00 not in O0OOOOO00OOOO000O :         #line:522
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given direction is not valid')         #line:523
      return Keyboard ._Vars .exit_code          #line:524
    if O0O0OOOO000O0O0OO <1 :         #line:525
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given amount is less than 1')         #line:526
      return Keyboard ._Vars .exit_code          #line:527
    if O0O00O0OOO0000O00 =='up':         #line:529
      Keyboard .mouseScroll ('vertical',O0O0OOOO000O0O0OO ,OO00OO00O0O000O00 ,OOO0000OOOO0O0OOO )         #line:530
    elif O0O00O0OOO0000O00 =='down':         #line:531
      Keyboard .mouseScroll ('vertical',-O0O0OOOO000O0O0OO ,OO00OO00O0O000O00 ,OOO0000OOOO0O0OOO )         #line:532
    elif O0O00O0OOO0000O00 =='right':         #line:533
      Keyboard .mouseScroll ('horizontal',O0O0OOOO000O0O0OO ,OO00OO00O0O000O00 ,OOO0000OOOO0O0OOO )         #line:534
    elif O0O00O0OOO0000O00 =='left':         #line:535
      Keyboard .mouseScroll ('horizontal',-O0O0OOOO000O0O0OO ,OO00OO00O0O000O00 ,OOO0000OOOO0O0OOO )         #line:536
  @staticmethod          #line:538
  def pressMouse (OO0O00O0O00OO0O0O :str |int )->None :         #line:539
    ""         #line:551
    if not isinstance (OO0O00O0O00OO0O0O ,str |int ):         #line:552
      Keyboard ._Vars .error (error_type ='p',var ='mouse_button',type ='integer or string')         #line:553
      return Keyboard ._Vars .exit_code          #line:554
    OOO0OO000OO00OOOO :list =["left_mouse",0x01 ,"right_mouse",0x02 ,"middle_mouse",0x04 ,"mouse_button1",0x05 ,"mouse_button2",0x06 ]         #line:559
    if OO0O00O0O00OO0O0O not in OOO0OO000OO00OOOO and hex (OO0O00O0O00OO0O0O )not in OOO0OO000OO00OOOO :         #line:560
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not a mouse button')         #line:561
      return Keyboard ._Vars .exit_code          #line:562
    if Keyboard ._lookup (OO0O00O0O00OO0O0O )is not False :         #line:564
      OO0O00O0O00OO0O0O :int =Keyboard ._lookup (OO0O00O0O00OO0O0O )         #line:565
    elif OO0O00O0O00OO0O0O not in Keyboard .vk_codes and OO0O00O0O00OO0O0O not in Keyboard .vk_codes .values ():         #line:566
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not valid')         #line:567
      return Keyboard ._Vars .exit_code          #line:568
    OOO0000000000OOO0 :Keyboard .INPUT =Keyboard .INPUT (type =Keyboard ._Vars .INPUT_MOUSE ,mi =MOUSEINPUT (wVk =OO0O00O0O00OO0O0O ,dwFlags =Keyboard ._Vars .KEYEVENTF_KEYUP ))         #line:576
    Keyboard ._Vars .user32 .SendInput (1 ,ctypes .byref (OOO0000000000OOO0 ),ctypes .sizeof (OOO0000000000OOO0 ))         #line:577
  @staticmethod          #line:579
  def releaseMouse (O0O0O0OO00OOO0O00 :str |int )->None :         #line:580
    ""         #line:592
    if not isinstance (O0O0O0OO00OOO0O00 ,str |int ):         #line:593
      Keyboard ._Vars .error (error_type ='p',var ='mouse_button',type ='integer or string')         #line:594
      return Keyboard ._Vars .exit_code          #line:595
    O0O0000OO0OOOO0OO :list =["left_mouse",0x01 ,"right_mouse",0x02 ,"middle_mouse",0x04 ,"mouse_button1",0x05 ,"mouse_button2",0x06 ]         #line:600
    if O0O0O0OO00OOO0O00 not in O0O0000OO0OOOO0OO and hex (O0O0O0OO00OOO0O00 )not in O0O0000OO0OOOO0OO :         #line:601
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not a mouse button')         #line:604
      return Keyboard ._Vars .exit_code          #line:605
    if Keyboard ._lookup (O0O0O0OO00OOO0O00 )is not False :         #line:607
      O0O0O0OO00OOO0O00 :int =Keyboard ._lookup (O0O0O0OO00OOO0O00 )         #line:608
    elif O0O0O0OO00OOO0O00 not in Keyboard .vk_codes and O0O0O0OO00OOO0O00 not in Keyboard .vk_codes .values ():         #line:609
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not valid')         #line:610
      return Keyboard ._Vars .exit_code          #line:611
    O0000O0OOOO00O0O0 :Keyboard .INPUT =Keyboard .INPUT (type =Keyboard ._Vars .INPUT_MOUSE ,mi =MOUSEINPUT (wVk =O0O0O0OO00OOO0O00 ))         #line:616
    Keyboard ._Vars .user32 .SendInput (1 ,ctypes .byref (O0000O0OOOO00O0O0 ),ctypes .sizeof (O0000O0OOOO00O0O0 ))         #line:617
  @staticmethod          #line:619
  def pressKey (OO0O0O00OO000O0OO :str |int )->None :         #line:620
    ""         #line:626
    if not isinstance (OO0O0O00OO000O0OO ,str |int ):         #line:627
      Keyboard ._Vars .error (error_type ='p',var ='key_code',type ='integer or string')         #line:628
      return Keyboard ._Vars .exit_code          #line:629
    if Keyboard ._lookup (OO0O0O00OO000O0OO )is not False :         #line:631
      OO0O0O00OO000O0OO :int =Keyboard ._lookup (OO0O0O00OO000O0OO )         #line:632
    elif OO0O0O00OO000O0OO not in Keyboard .vk_codes and OO0O0O00OO000O0OO not in Keyboard .vk_codes .values ():         #line:633
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not valid')         #line:634
      return Keyboard ._Vars .exit_code          #line:635
    O0O000O00000O00O0 :Keyboard .INPUT =Keyboard .INPUT (type =Keyboard ._Vars .INPUT_KEYBOARD ,ki =KEYBDINPUT (wVk =OO0O0O00OO000O0OO ))         #line:640
    Keyboard ._Vars .user32 .SendInput (1 ,ctypes .byref (O0O000O00000O00O0 ),ctypes .sizeof (O0O000O00000O00O0 ))         #line:641
  @staticmethod          #line:643
  def releaseKey (OOO00O0O0OO0OOOOO :str |int )->None :         #line:644
    ""         #line:650
    if not isinstance (OOO00O0O0OO0OOOOO ,str |int ):         #line:651
      Keyboard ._Vars .error (error_type ='p',var ='key_code',type ='integer or string')         #line:652
      return Keyboard ._Vars .exit_code          #line:653
    if Keyboard ._lookup (OOO00O0O0OO0OOOOO )is not False :         #line:655
      OOO00O0O0OO0OOOOO :int =Keyboard ._lookup (OOO00O0O0OO0OOOOO )         #line:656
    elif OOO00O0O0OO0OOOOO not in Keyboard .vk_codes and OOO00O0O0OO0OOOOO not in Keyboard .vk_codes .values ():         #line:657
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not valid')         #line:658
      return Keyboard ._Vars .exit_code          #line:659
    O000OO0O00O0O0O0O :Keyboard .INPUT =Keyboard .INPUT (type =Keyboard ._Vars .INPUT_KEYBOARD ,ki =KEYBDINPUT (wVk =OOO00O0O0OO0OOOOO ,dwFlags =Keyboard ._Vars .KEYEVENTF_KEYUP ))         #line:667
    Keyboard ._Vars .user32 .SendInput (1 ,ctypes .byref (O000OO0O00O0O0O0O ),ctypes .sizeof (O000OO0O00O0O0O0O ))         #line:668
  @staticmethod          #line:670
  def pressAndReleaseKey (OOO00OO00O0O0OO00 :str |int )->None :         #line:671
    ""         #line:677
    if not isinstance (OOO00OO00O0O0OO00 ,str |int ):         #line:678
      Keyboard ._Vars .error (error_type ='p',var ='key_code',type ='integer or string')         #line:679
      return Keyboard ._Vars .exit_code          #line:680
    if Keyboard ._lookup (OOO00OO00O0O0OO00 )is not False :         #line:682
      OOO00OO00O0O0OO00 :int =Keyboard ._lookup (OOO00OO00O0O0OO00 )         #line:683
    elif OOO00OO00O0O0OO00 not in Keyboard .vk_codes and OOO00OO00O0O0OO00 not in Keyboard .vk_codes .values ():         #line:684
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not valid')         #line:685
      return Keyboard ._Vars .exit_code          #line:686
    Keyboard .pressKey (OOO00OO00O0O0OO00 )         #line:688
    Keyboard .releaseKey (OOO00OO00O0O0OO00 )         #line:689
  @staticmethod          #line:691
  def pressAndReleaseMouse (O0O0O0O0OO00O0O00 :str |int )->None :         #line:692
    ""         #line:704
    if not isinstance (O0O0O0O0OO00O0O00 ,str |int ):         #line:705
      Keyboard ._Vars .error (error_type ='p',var ='mouse_button',type ='integer or string')         #line:706
      return Keyboard ._Vars .exit_code          #line:707
    OOO0O0000O00OOO00 :list =["left_mouse",0x01 ,"right_mouse",0x02 ,"middle_mouse",0x04 ,"mouse_button1",0x05 ,"mouse_button2",0x06 ]         #line:712
    if O0O0O0O0OO00O0O00 not in OOO0O0000O00OOO00 and hex (O0O0O0O0OO00O0O00 )not in OOO0O0000O00OOO00 :         #line:713
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not a mouse button')         #line:714
      return Keyboard ._Vars .exit_code          #line:715
    OO00O0OOOO0O0OOO0 :str =O0O0O0O0OO00O0O00          #line:716
    if Keyboard ._lookup (O0O0O0O0OO00O0O00 )is not False :         #line:718
      O0O0O0O0OO00O0O00 :int =Keyboard ._lookup (O0O0O0O0OO00O0O00 )         #line:719
    elif O0O0O0O0OO00O0O00 not in Keyboard .vk_codes and O0O0O0O0OO00O0O00 not in Keyboard .vk_codes .values ():         #line:720
      Keyboard ._Vars .error (error_type ='r',runtime_error ='given key code is not valid')         #line:721
      return Keyboard ._Vars .exit_code          #line:722
    Keyboard .pressMouse (OO00O0OOOO0O0OOO0 )         #line:724
    Keyboard .releaseMouse (OO00O0OOOO0O0OOO0 )         #line:725
  @staticmethod          #line:727
  def keyboardWrite (O000O0O0OO00O00O0 :str )->None :         #line:728
    ""         #line:735
    if not isinstance (O000O0O0OO00O00O0 ,str ):         #line:736
      Keyboard ._Vars .error (error_type ='p',var ='string',type ='string')         #line:737
      return Keyboard ._Vars .exit_code          #line:738
    O0OOO00O00000O0OO :list =list (O000O0O0OO00O00O0 )         #line:740
    O0OO0OO0O0000OOOO :list =['|','~','?',':','{','}','\"','!','@','         #','$','%','^','&','*','(',')','+','<','>','_']         #line:745
    for OO0OO00OO0OO0O00O in O0OOO00O00000O0OO :         #line:746
      if OO0OO00OO0OO0O00O not in Keyboard .vk_codes and not OO0OO00OO0OO0O00O .isupper ():         #line:747
        Keyboard ._Vars .error (error_type ='r',runtime_error =f'character: {OO0OO00OO0OO0O00O} is not in vk_codes map')         #line:751
        return Keyboard ._Vars .exit_code          #line:752
      if OO0OO00OO0OO0O00O .isupper ()or OO0OO00OO0OO0O00O in O0OO0OO0O0000OOOO :         #line:754
        Keyboard .pressKey ('shift')         #line:755
      else :         #line:756
        Keyboard .releaseKey ('shift')         #line:757
      OOO00OO0OO00O000O :int =Keyboard ._lookup (OO0OO00OO0OO0O00O .lower ())         #line:759
      OO0OOO00O0OO00OOO :Keyboard .INPUT =Keyboard .INPUT (type =Keyboard ._Vars .INPUT_KEYBOARD ,ki =KEYBDINPUT (wVk =OOO00OO0OO00O000O ))         #line:763
      Keyboard ._Vars .user32 .SendInput (1 ,ctypes .byref (OO0OOO00O0OO00OOO ),ctypes .sizeof (OO0OOO00O0OO00OOO ))         #line:764
      OO00O00OOOOOOOO0O :Keyboard .INPUT =Keyboard .INPUT (type =Keyboard ._Vars .INPUT_KEYBOARD ,ki =KEYBDINPUT (wVk =OOO00OO0OO00O000O ,dwFlags =Keyboard ._Vars .KEYEVENTF_KEYUP ))         #line:772
      Keyboard ._Vars .user32 .SendInput (1 ,ctypes .byref (OO00O00OOOOOOOO0O ),ctypes .sizeof (OO00O00OOOOOOOO0O ))         #line:773
    Keyboard .releaseKey ('shift')         #line:774
  @staticmethod          #line:776
  def altTab ()->None :         #line:777
    ""         #line:780
    Keyboard .pressKey (Keyboard .vk_codes ['alt'])         #line:783
    Keyboard .pressKey (Keyboard .vk_codes ['tab'])         #line:784
    Keyboard .releaseKey (Keyboard .vk_codes ['tab'])         #line:785
    time .sleep (2 )         #line:786
    Keyboard .releaseKey (Keyboard .vk_codes ['alt'])         #line:787
