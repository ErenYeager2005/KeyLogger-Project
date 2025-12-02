from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse=Controller()
    mouse.position=(100,200)

def controlkeyboard():
    keyboard=Controller()
    keyboard.type("i am the honoured one")

controlkeyboard()

