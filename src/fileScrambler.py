import os
import shutil


class FolderMethods:
    def __init__(self, path):
        self.path = path + "scrambledFolder"

    def removeFolderIfExists(self):
        if os.path.isdir(self.path):
            shutil.rmtree(self.path)

    def checkIfFolderExistsAndCreate(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

class Scramble:
    
        pass


folderpath = input("Insert the folder you want to scramble\n> ")

if folderpath[-1] != "/":
    folderpath += "/"

folder = FolderMethods(folderpath)

folder.removeFolderIfExists()

files = []

for filename in os.listdir(folderpath):
    fileobj = open(folderpath+filename, "rb")
    files.append(fileobj)

folder.checkIfFolderExistsAndCreate()

targetFile = open(folderpath+"scrambledFolder/scrambledFile.txt", "wb")

for file in files:
    targetFile.write((os.path.basename(file.name)+"\n").encode('utf-8'))
    for line in file.readlines():
        targetFile.write(line)
    targetFile.write("\n|%|anotherfile|%|\n".encode('utf-8'))
targetFile.write("|%|endoffile|%|\n".encode('utf-8'))