#PyPaperworkDatabase
import os
import odbc

filesInFolder = []
firstBreak = ""

def copy_file_names(folder_path):
    for fileName in os.listdir(folder_path):
        filesInFolder.append(fileName)
    return filesInFolder

def first_split(firstBreak):
    stripped = firstBreak.split('.')
    stripped = stripped[0]
    stripped = stripped.split('_')
    return stripped



filesInFolder = copy_file_names(r'F:\ScannedRandomPaperwork')
strippedTest = first_split(filesInFolder[1])

print(strippedTest)