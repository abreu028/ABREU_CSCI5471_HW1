import os

# open and read the cipher text file
with open("hw1p4.txt","rb") as f:
    fulltext=f.read()

text1=fulltext[:1024] # first cipher text
text2=fulltext[1024:] # second cipher text
mm = [] # the cipher texts xored together
for i in range(1024):
    mm.append(text1[i]^text2[i])

# getting the files from the database
path = "/project/web-classes/Fall-2025/csci5471/hw1/db/"
texts = [] # array of texts

#adding them to an array
for file in os.listdir(path):
    with open(os.path.join(path, file), 'rb') as f:
        texts.append(f.read())
counter = 0 # the number of valid texts
validtext = [] # all of the valid texts xored with mm
for i in range(len(texts)):
    temp = []
    counterbool = False # reset counter bool
    for j in range(1024):
        # xor the jth char of mm with the jth char of the text
        tempbit = mm[j]^texts[i][j]
        if (tempbit<65 and tempbit !=32) or (tempbit>122):
            counterbool = True # invalid character so turn counter bool
        temp.append(tempbit) # add the bit to temp array
    if counterbool:
        counter+=1
    else:
        validtext.append(temp)

# if the number of valid texts is less than 5 just print them out
if len(validtext)<=5:
    for j in range(len(validtext)):
        print("Possible plain text")
        for i in range(1024):
            print(chr(validtext[j][i]),end='')
        print()
        print()
        print("Possible Corresponding plaintext")
        for i in range(1024):
            print(chr(validtext[j][i]^mm[i]),end='')
        print()
        print()
