text = 'Hello World'
key = 3
crypt = ''
for i in text:
    try:
        crypt += chr(ord(i) ^ ord(key))
    except TypeError:
        crypt += chr(ord(i) ^ key)

print(crypt)

with open("crypt.txt","w") as file:
    file.write(crypt)

decrypt = ''

with open("crypt.txt","r") as file:
    for j in file.read():
        try:
            decrypt += chr(ord(j) ^ ord(key))
        except:
            decrypt += chr(ord(j) ^ key)


print(decrypt)
