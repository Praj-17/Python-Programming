# Health Management system
# 3 clients - Prajwal , Aihsu and saumya
def getdate():
    import datetime
    return datetime.datetime.now()
def  User_input_1():
    print("Enter the client name\n 1. Prajwal \n 2.Aishu \n 3. Saumya")
    inp_1 = int(input())
    return inp_1
def User_input_2():
     print("What do you want to log?? \n 1. food \n 2. Excercise")
     inp_2 = int(input())
     return  inp_2 
def Write_files(f):
             t = getdate()
             f.write("\n[")
             f.write(str(t))
             f.write("]\n")
             f.write(input("Write What you ate\n"))
    
def Open_files(inp_1, inp_2):
    if inp_1 == 1 and inp_2 ==1:
        with open ("Prajwal_foodlog.txt", "a") as f:
            Write_files(f)
    elif inp_1 ==1 and inp_2 ==2:
        with open ("Prajwal_Excerciselog.txt", "a") as f:
            Write_files(f)
    elif inp_1 == 2 and inp_2 ==1:
        with open ("Aishu_foodlog.txt", "a") as f:
            Write_files(f)
    elif inp_1 == 2 and inp_2 ==2:
        with open ("Aishu_Excerciselog.txt", "a") as f:
            Write_files(f)
    elif inp_1 == 3 and inp_2 ==1:
        with open ("saumya_foodlog.txt", "a") as f:
            Write_files(f)
    elif inp_1 == 3 and inp_2 ==2:
        with open ("saumya_excerciselog.txt", "a") as f:
            Write_files(f)
            
a = User_input_1()
b  = User_input_2()
Open_files(a,b)

