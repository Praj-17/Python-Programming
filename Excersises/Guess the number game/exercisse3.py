n = 18
attempts = 9

print("guess a number, in less than 9 attempts ")
while (attempts >0) :
    inp = int(input())
    if(n>inp):
        print("greater")
    elif(n<inp):
        print("lesser")
    else:
        print("correct")   
        print("you took ",attempts, "attempts" )
        break
    attempts = attempts -1
    print("no of guesses left =", 9-attempts)
   
if(attempts ==  0):
    print("game over")


     
