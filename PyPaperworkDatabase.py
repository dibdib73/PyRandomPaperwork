#PyPaperworkDatabase
import os

filesInFolder = []

def copy_file_names(folder_path):
    for fileName in os.listdir(folder_path):
        filesInFolder.append(fileName)


copy_file_names(r'F:\ScannedRandomPaperwork')
print(filesInFolder)