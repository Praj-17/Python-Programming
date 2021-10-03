#your age in 2090
userinp = int(input("pls input your age or year of birth "))
if userinp <200:
    isage = True
elif userinp > 1900:
    isyear = True
    isage = False
elif userinp in range (200, 1900):
    isage = False
    isyear = False
    print("pls input a valid age or year of birth")
if isage == True:
   fage = userinp + 69
   if fage > 100: "you are way to old, keep it up!"
   if fage <0: print("you have not even born yet")
   print("your age in 2090 will be", fage )
elif isyear == True:
    fage = 2090 - userinp
    if fage > 100: "you are way to old, keep it up!"
    if fage <0: print("you have not even born yet")
    print("your age in 2090 will be", fage)