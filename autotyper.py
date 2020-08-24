from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)

while True:
    for char in "pls meme":
        keyboard.press(char)
        keyboard.release(char)
    

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(4)


























