
import sys
import os
from time import sleep
#print(sys.argv)
def vote(name,age):
    if age>=18:
        print(f"\n {name} can vote")
    else:
        print(f"\n {name} cannot vote")
        
vote(sys.argv[1],int(sys.argv[2]))
sleep(3)
os.system("cls")
