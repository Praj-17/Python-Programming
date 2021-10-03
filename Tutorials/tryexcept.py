f1 = open("MAIN1.py")

try:
    f = open ("does.txt")
except Exception as e: print(e)
finally:
    print("Run this anyway")
    f1.close()


   
print("imp line")
