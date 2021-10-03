#Guess the number
import random
def guessgame(a,b,Ans):
    Players_guess = int(input(f"Player pls Guess the number between {a} and {b} \n"))
    nguess = 1
    while(Players_guess != Ans ):
        if Players_guess >Ans: 
          Players_guess = int (input ("wrong! Pls input a smaller number"))
          nguess +=1
        elif Players_guess <Ans :
            Players_guess =int(input("wrong! Pls input a greater number"))
            nguess +=1
        elif Players_guess == Ans : print("Correct! ")
    
    return nguess

a = int(input("Pls enter the Lower Bound:- "))
b = int(input("Pls enter the Upper Bound:- "))
Ans = random.randint(a,b)
print("****Player 1's Game*****")
g1 = guessgame(a,b,Ans)
print("****Player 2's Game*****")
g2 = guessgame(a,b,Ans)

if g1<g2:
    print("Player 1 won the match")
elif g2>g1:
    print("Player 2 won the match ")
else:
    print("The match has tied")







