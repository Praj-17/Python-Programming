f = open("E:\codes\CODE\PYTHON\\text.txt" )
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline()) 
print(f.tell())
f.seek(10)
print(f.readline())
print(f.tell())
f.close()

with open("E:\codes\CODE\PYTHON\\text.txt" ) as f:
    f.readline()
