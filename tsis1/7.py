#STRINGS

txt = "Hello World"

print(len(txt)) #length of text

x1 = txt[0]
print("first character is: " + x1)

x2 = txt[2:5]
print("the characters from index 2 to index 4: "+ x2)

x3 = txt.strip()
print("the string without any whitespace at the beginning or the end: "+ x3)

x4 = txt.upper()
print("the value of txt to upper case: "+x4)

x5 = txt.lower()
print("the value of txt to lower case: "+x5)

x6 = txt.replace("H", "J")
print("Replace the character H with a J: "+x6)


