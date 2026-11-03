f = open("abc.txt", "r")
content = f.read()
print(content)
print(f.name)
print(f.mode)

f.close()