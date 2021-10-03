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

#FILE WRITING
f = open("text.txt")
content = f.read()
print(content)

