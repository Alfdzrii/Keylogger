from pynput.mouse import Controller 
from pynput.keyboard import Controller

# controlling mouse
def controlMouse():
    mouse = Controller()
    mouse.position = (100,10)

# controlling keyboard
def controlKeyboard():
    keyboard = Controller()
    keyboard.type("halo ganteng")

controlKeyboard()