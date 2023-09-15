#PyPaperworkDatabase
import os

def copy_file_names(folder_path):
    for fileName in os.listdir(folder_path):
        print(fileName)

copy_file_names(r'"F:\ScannedRandomPaperwork"')