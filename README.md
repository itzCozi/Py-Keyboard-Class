# Py-Keyboard-Class
A class used for handling inputs via VK codes and win32 API moved from Helper/curses.py. The Keyboard class can send inputs via functions like `scrollMouse`, `pressAndReleaseKey`, `keyboardWrite` and `pressAndReleaseMouse` it can also return keystrokes using the `GetKeystroke` wrapper which polls key presses.


## Code Pics
![main class doc-string](ignore/keyboard-doc-string.png 'Keyboard class doc-string')  
Keyboard class doc-string

![Keyboard input class](ignore/input-class.png 'class for Keyboard input')  
Main Keyboard input class (before static type hinting was added)


## Code Rules
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
* Make sure optional parameters are specifed in the functions doc-string EX: output_path (str, optional)


## Extra 
[Source](https://github.com/itzCozi/Py-Keyboard-Class/blob/main/source/py_key.py)  
[Compiler](https://pypi.org/project/auto-py-to-exe/)  


### Contact Me
Discord: .baddeveloper  
Email: Cooperransom08@outlook.com  
[Discord Server](https://discord.gg/xGnQQGxwq2)  |  [Replit](https://replit.com/@cozi08)  |  [Twitter](https://twitter.com/ransom_cooper)