#  ROCK PAPER SCISSORS 
#Prajwal jain
import random
import time
mypoints = 0
cpupoints = 0
matches = 0
list = ["rock", "paper", "scissors"]
while (matches<10):
    print("Please input ur choice")
    print("r for ROCK")
    print("s for SCISSORS")
    print("p for PAPERS")
    User_choice = input()
    cpu_choice = random.choice(list)
    if User_choice == cpu_choice:
        matches +=1
        print("Match draw!😑")
    else:
        if User_choice == "r" and cpu_choice =="paper": 
            cpupoints +=1
            print("You lost!😥😥")
        elif User_choice == "r" and cpu_choice =="scissors":
            mypoints +=1
            print("You won!🤩🥳 ")
        elif User_choice == "p" and cpu_choice =="scissors":
            cpupoints +=1
            print("You lost!😥😥")
        elif User_choice == "p" and cpu_choice =="rock": 
            mypoints +=1
            print("You won!🤩🥳 ")
        elif User_choice == "s" and cpu_choice =="rock":
            cpupoints +=1
            print("You lost!😥😥")
        elif User_choice == "s" and cpu_choice =="paper":
             mypoints +=1
             print("You won!🤩🥳 ")
        elif User_choice != "p" or User_choice != "r"  or User_choice != "s" :
            print("Invalid input pls!!\n pls input ")
            print("r for ROCK")
            print("s for SCISSORS")
            print("p for PAPERS")
    
    print("The C.P.U chose", (cpu_choice) )
    matches +=1
print("Wins = ", mypoints)
print("Loss = ", cpupoints)
print("Draw = ", 10-cpupoints-mypoints)
print("The window will close after 20 seconds")
time.sleep(20)

            
    
    

    
        