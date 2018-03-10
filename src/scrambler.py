import os
import shutil
import sys

class Scramble:
    
        pass


folderPath = sys.argv[1]

if folderPath[-1] != "/":
    folderPath += "/"

files = []

for filename in os.listdir(folderPath):
    fileobj = open(folderPath+filename, "rb")
    files.append(fileobj)

targetFile = open(folderPath+"scrambledFile.txt", "wb")

for file in files:
    targetFile.write((os.path.basename(file.name)+"\n").encode('utf-8'))
    for line in file.readlines():
        targetFile.write(line)
    targetFile.write("\n|%|anotherfile|%|\n".encode('utf-8'))
targetFile.write("|%|endoffile|%|\n".encode('utf-8'))
