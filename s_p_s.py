
from getpass import getpass
from random import choice

p_win = [("scissor","paper"),("paper","rock"),("rock","scissor")]
c_win = [("paper","scissor"),("rock","paper"),("scissor","rock")]

print("Rock Paper Scissor".center(70,"*"))
p = getpass("\n Player 1 : ").strip().lower()
c = choice(["paper","scissor","rock"])
if (p,c) in p_win:
    print(f"\n Player won the game with choices \n\n Player : {p} and Computer : {c}")
elif (p,c) in c_win:
    print(f"\n Computer won the game with choices \n\n Player : {p} and Computer : {c}")
else:
    print("\n Incorrect choice")
    
print("End of the game".center(70,"*"))
