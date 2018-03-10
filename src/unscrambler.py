import os
import shutil
import sys

class FolderMethods:
    def __init__(self, path):
        self.path = path + "/descrambledFiles/"

    def removeFolderIfExists(self):
        if os.path.isdir(self.path):
            shutil.rmtree(self.path)

    def checkIfFolderExistsAndCreate(self):
        self.removeFolderIfExists()
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

class Unscramble:
    
        pass


filePath = sys.argv[1]

folderPath = "/".join((filePath.split('/')[:-1]))

folder = FolderMethods(folderPath)

folder.checkIfFolderExistsAndCreate()

with open(filePath, 'rb') as file:
    while 1:
        firstLine = file.readline().decode('utf-8')[:-1]

        if firstLine == "|%|endoffile|%|":
            sys.exit(0)

        outputFile = open(folder.path+firstLine, "wb")
        
        while 1:
            line = file.readline()

            if line == "|%|anotherfile|%|\n".encode('utf-8'):
                break

            outputFile.write(line)