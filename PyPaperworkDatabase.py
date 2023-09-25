#PyPaperworkDatabase
import os
import pyodbc
from datetime import date

'''Starting with connection to database using pyodbc. Then modifiing the database.'''
connStr = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=F:\ScannedRandomPaperwork\A_ScannedPaperworkInThisFile.accdb;')
conn = pyodbc.connect(connStr)
# Execute a SELECT statement
cursor = conn.cursor()

'''Modification of database'''
filesInFolder  = []
firstBreak     = ""

#List of all items in folder of items to add to database.
def copy_file_names(folder_path):
    for fileName in os.listdir(folder_path):
        filesInFolder.append(fileName)
    return filesInFolder

#Function creating list of items from Linked_to_paperwork items.
#Return a new list of items from the tupels inside of the list. Easier to deal with later.
def ms_file_name():
    linkList = []
    selectStmt = "SELECT Link_to_paperwork FROM Scanned_paperwork"
    cursor.execute(selectStmt)
    namesOfLinks = cursor.fetchall()
    for nl in namesOfLinks:
        for i in nl:
            s = i.rsplit("#")[0]
            linkList.append(s)
    return linkList

#Convert the results from "iter_through_full_list function" and "ms_file_name function" to sets
def search_for_duplicates(folderFiles, msFiles):
    setFolderFiles = set(folderFiles)
    setMsFiles     = set(msFiles)
    diffItems = setFolderFiles.difference(setMsFiles)
    diffItems = list(diffItems)
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
def first_split(firstBreak):
    stripped = firstBreak.pop(0)
    stripped = stripped[0 : -4]
    stripped = stripped.split('_')
    return stripped

#Add the items from "first_split function" to database.
#And check for correct item names.
def add_to_db(contentAdd):
    if len(contentAdd) < 3:
        print("Name must start with originization name, then type of paperwork,\nand end with date. Must be separated with an underscore")

    elif len(contentAdd) == 3:
        val1 = contentAdd[1]
        val2 = contentAdd[0]
        val3 = date.today()
        valDate = val3.strftime('%m/%d/%y')
        testVals = (val1, val2, valDate)
        exeStatment = ("INSERT INTO Scanned_paperwork (Type, Paperwork_name, Date_scanned)"
                "VALUES (?, ?, ?);")
        cursor.execute(exeStatment, testVals)
        cursor.commit()

    else:
        print("Error with content length")

filesInFolder = copy_file_names(r"F:\ScannedRandomPaperwork\NeedToAddToDatabase")
msFiles       = ms_file_name()
listWODups    = search_for_duplicates(filesInFolder, msFiles)
iterFullList  = iter_through_full_list(listWODups)
