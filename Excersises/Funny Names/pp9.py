#FUNNY NAMES
n = int(input("Pls input the number of names you want to put\n"))
firstname1 = []
lastname1 = []
for i in range (n):
    name = input("Pls input the names one by one\n")
    names = name.split()
    firstname = names[0]
    lastname = names[1]
    firstname1.append(firstname)
    lastname1.append(lastname1)
print(f"The first names are{firstname1} ")
print(f"The last names are{lastname1} ")