import os
import shutil
import sys

class FolderMethods:
    def __init__(self, path):
        self.path = path + "../" + "descrambledFiles"

    def removeFolderIfExists(self):
        if os.path.isdir(self.path):
            shutil.rmtree(self.path)

    def checkIfFolderExistsAndCreate(self):
        self.removeFolderIfExists()
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

class Descramble:
    
        pass


folderpath = input("Insert the folder you want to descramble\n> ")

if folderpath[-1] != "/":
    folderpath += "/"

folder = FolderMethods(folderpath)

folder.checkIfFolderExistsAndCreate()

with open(folderpath+'scrambledFile.txt', 'rb') as file:
    while 1:
        firstLine = file.readline().decode('utf-8')[:-1]
        print(firstLine)

        if firstLine == "|%|endoffile|%|":
            sys.exit(0)

        outputFile = open(folderpath+"../descrambledFiles/"+firstLine, "wb")
        
        while 1:
            line = file.readline()

            if line == "|%|anotherfile|%|\n".encode('utf-8'):
                print('end')
                break

            outputFile.write(line)