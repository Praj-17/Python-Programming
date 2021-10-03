
choice = 0
Userfound = False
passwordfound = False
position = 0
KeepLooping = True
def SignIn(): 
    print()
    print("-------------SIGN IN MENU---------")
    print("Create an UserName")
    username = input()
    file_user = open("Usernames.txt", "r")
    contents = file_user.read()
    users = contents.split(",")
    for i in users:
        if(i ==username):
            Userfound = True
        break
    else:
        Userfound == False
    file_user.close()
    if(Userfound == True):
        print("Username Already Exists")
    else:
        file_user = open("Usernames.txt", "a")
        file_user.write(username+",")
        print("enter the password")
        password = input()
        file_password = open("Passwords.txt", "a")
        file_password.close()
        file_user.close()
def LogIn():
    print()
    print("Enter The Username")
    username = input()
    print("Enter the password")
    password = input()
    file_user = open("Usernames.txt", "r")
    file_password = open("Passwords.txt", "a")
    User_contents = file_user.read()
    password_contents = file_user.read()
    User_list = User_contents.split(',')
    password_list=password_contents.split(',')

    for user in User_list:
        if(user==username):
            position = User_list.index(user)
            Userfound = True
            break
        else: Userfound = False
    
    if(Userfound == True):
        if(password_list[position]==password):
            print("Successfull login")
        else: ("Incorrect password")
    else:
        print("Invalid Username ")
    file_password.close()
    file_user.close() 
while(KeepLooping):
    print()
        
    print("-------------WELCOME----------")
    print("Choose an option using numbers a input")
    print("1.SignUp")
    print("2.Login")
    print("3.Exit")
    try:
         choice = int(input())
         if(choice>3):
             print("Enter the number as 1 or 2 or 3")
         elif(choice<1):
            print("Enter the number as 1 or 2 or 3")
         else:
             if(choice ==1):SignIn()
             elif(choice ==2):LogIn()
             else:KeepLooping = False
             
             
    except:
        print("Enter  a number")
        
        
    
        
        
                         
    
    