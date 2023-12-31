import json
import typing
import os
#TODO: import JSON
#TODO: Look for JSON file
#TODO: If no JSON file create a file
#TODO: If there is a JSON file iterate through location in file (numbered)
#TODO: Ask user what file location is to be worked on

def look_for_json(fileN: str, wherefile: str) -> str:
    wherefile = wherefile + '.json'
    wherePath = os.listdir(wherefile)
    a = fileN in wherePath
    if a == True:
        print('Yes this file is in this dirctory.')
    else:
        ans = print('This file does not exist. Do you want to create one? (y) or (n)')
        if ans.lower() == 'y':
            createdFile = create_json(fileN, wherefile) # If file doesn't exist create file with createfile function.
            return createdFile
        elif ans.lower() != 'y' or ans.lower() != 'n':
            print('Answer must be "y" or "n" only.')
        else:
            print('Good bye.')

def create_json(jsonName: str, jsonLoc: str ) -> str:
    jsonPath = os.path.join(jsonLoc, jsonName)
    return jsonPath

class json_read_write(self, jsonName, jsonLoc):
    jsonName = self.jsonName
    jsonLoc = self.jsonLoc
    def write_to_json(self):
        with open(self.jsonName, 'w+') as writeJson:
            dbname = {'Name': self.jsonName, "Directory": self.jsonLoc}
            writeJson.write(dbname)
    def read_json_file(self):
        with open(self.jsonName, 'r') as readJson:
            listDbs = readJson.readlines()

wherefile = r'F:\ScannedRandomPaperwork\NeedToAddToDatabase'
fileN = r'Fidelity_Retirement_0701202.pdf'
dbFile = look_for_json(fileN, wherefile)