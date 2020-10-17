

from random import choice
def getcolor():
    c = "#"
    ch = ['a','b','c','d','e','f','1','2','3','4','5','6']
    for i in range(6):
        c += choice(ch)
    return c
