from pynput.keyboard import Listener

def writetofile(x,y):
    print("current mouse position is ".format((x,y)))

with Listener(on_move=writetofile) as l:
    l.join()