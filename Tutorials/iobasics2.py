# File io basics
"""
"r"- open file for reading - default
"w"- open file for writing
"x"- creates file if not exists
"a"- Add more content to a file
"t"- text mode - default
"b"- binary mode
"+"- read + write
"""

"""
#FILE Reading
f = open("E:\codes\CODE\PYTHON\\text.txt", "rt")
#content = f.read()
#print(content)
print(f.readline()) #it prints first line
print(f.readline()) #it prints second line
print(f.readline()) #it prints third line
for line in f:
    print(line, end = "")
print(f.readlines())
f.close() 
"""
"""
#File Writing
f = open("E:\codes\CODE\PYTHON\\text.txt", "w")
f.write("Prajwal is writing a code")
f.write("Prajwal is writing a code\n")
a = f.write("Prajwal is writing a code\n")
f.write("Prajwal is writing a code\n")
print(a)
print(f.tell())
print(f.readline)
print(f.seek(10))
print(f.tell())
print(f.seek(0))
f.close()  
"""
#With Blocks
f = open("E:\codes\CODE\PYTHON\\text.txt", "rt")
print(f.readline())

f.close()
with open("E:\codes\CODE\PYTHON\\text.txt") as f:
    a = f.read(10)
    print(a)

