import json
import typing
import os
#TODO: import JSON
#TODO: Look for JSON file
#TODO: If no JSON file create a file
#TODO: If there is a JSON file iterate through location in file (numbered)
#TODO: Ask user what file location is to be worked on

fileN = r'Fidelity_Retirement_07012023.pdf'
#input("What is the database name? ")
wherefile = r'F:\ScannedRandomPaperwork\NeedToAddToDatabase'
#input("Where is the file location? ")

def look_for_json(fileN: str, wherefile: str) -> str:
    wherePath = os.listdir(wherefile)
    a = fileN in wherePath
    if a == True:
        print('Yes this file is in this dirctory.')
    else:
        print('There is no file like this here.')

def create_json(jsonName: str, jsonLoc: str ) -> str:
    return None

look_for_json(fileN, wherefile)
"""class json_read_write(self, jsonName, jsonLocation):
     jsonName = self.jsonName
    jsonLocation = self.jsonLocation
    def write_to_json(self):
        return None
    def read_json_file(self):
        return None """
