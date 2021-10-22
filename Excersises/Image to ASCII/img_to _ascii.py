import pywhatkit
image = "i14.jpeg"
a = pywhatkit.image_to_ascii_art(f"{image}")
print(a)
with open("art12.txt", 'x') as f:
    f.write(a)