#PyPaperworkDatabase
import os
import pyodbc
from datetime import date
from datetime import datetime
from typing import List, Set

'''Starting with connection to database using pyodbc. Then modifiing the database.'''
#TODO:Ask user for location of Database and folder of paperwork to scan.
connStr = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=F:\ScannedRandomPaperwork\A_ScannedPaperworkInThisFile.accdb;')
conn    = pyodbc.connect(connStr)
cursor  = conn.cursor()

'''Modification of database'''
filesInFolder: List[str]  = []

#List of all items in folder of items to add to database.
def copy_file_names(folder_path: str) -> List[str]:
    for fileName in os.listdir(folder_path):
        filesInFolder.append(fileName)
    return filesInFolder

#Function creating list of items from Linked_to_paperwork items.
#Return a new list of items from the tupels inside of the list. Easier to deal with later.
def ms_file_name() -> List[str]:
    linkList   = []
    selectStmt = "SELECT Link_to_paperwork FROM Scanned_paperwork"
    cursor.execute(selectStmt)
    namesOfLinks = cursor.fetchall()
    for nl in namesOfLinks:
        for i in nl:
            s = i.rsplit("#")[0]
            linkList.append(s)
    return linkList

#Convert the results from "iter_through_full_list function" and "ms_file_name function" to sets
def search_for_duplicates(folderFiles: List[str], msFiles: Set[str]) -> List[str]:
    setFolderFiles = set(folderFiles)
    setMsFiles     = set(msFiles)
    diffItems      = setFolderFiles.difference(setMsFiles)
    diffItems      = list(diffItems)
    return diffItems

#Iterate through full list from "search_for_duplicates function".
#stripped is calling "first_split function".
#Add stripped list to database using "add_to_db function".
def iter_through_full_list(filesInFolder):
    while 0 < len(filesInFolder):
        stripped = first_split(filesInFolder)
        add_to_db(stripped)

#Pop first item from "iter_through_full_list function" list.
#Strip the .pdf off the end.
#Create a new list of items by separating text by using underscore as a marker.
def first_split(firstBreak) -> list:
    stripped = firstBreak.pop(0)
    stripped = stripped[0 : -4]
    stripped = stripped.split('_')
    return stripped

#Add the items from "iter_through_full_list function" to database.
#And check for correct amount of items.
def add_to_db(contentAdd):
    if len(contentAdd) == 3:
        val1     = contentAdd[1]
        val2     = contentAdd[0]
        val3     = date.today()
        val4     = contentAdd[2]
        valDate  = val3.strftime('%m/%d/%y')
        val4Date = datetime.strptime(val4, '%m%d%y')
        Vals     = (val1, val2, valDate, val4Date)
        exeStatment = ("INSERT INTO Scanned_paperwork (Type, Paperwork_name, Date_scanned, Date_of_paperwork)"
                "VALUES (?, ?, ?, ?);")
        cursor.execute(exeStatment, Vals)
        cursor.commit()
    else:
        print("Name must start with originization name, then type of paperwork,\nand end with date. Must be separated with an underscore")

filesInFolder = copy_file_names(r"F:\ScannedRandomPaperwork\NeedToAddToDatabase")
print(filesInFolder)
msFiles       = ms_file_name()
listWODups    = search_for_duplicates(filesInFolder, msFiles)
iterFullList  = iter_through_full_list(listWODups)
