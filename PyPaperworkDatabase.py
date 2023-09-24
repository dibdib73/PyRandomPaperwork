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
filesInFolder = []
firstBreak = ""

#Create a list of all items in folder of items to add to database.
def copy_file_names(folder_path):
    for fileName in os.listdir(folder_path):
        filesInFolder.append(fileName)
    return filesInFolder

#Pop first item from "iter_through_full_list function" list. Use those items to add to database.
def first_split(firstBreak):
    stripped = firstBreak.pop(0)
    stripped = stripped[0 : -4]
    stripped = stripped.split('_')
    return stripped

#Iterate through full list "from copy_file_names function" split apart and add to db
def iter_through_full_list(filesInFolder):
    for i in filesInFolder:
        stripped = first_split(filesInFolder)
        print(stripped)

#Add the items from "iter_through_full_list function" to database. And check for correct item names.
def add_to_db(contentAdd):
    if len(contentAdd) == 2:
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



#Function creating list of items from Linked_to_paperwork items.
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

def search_for_duplicates(folderFiles, msFiles):

#TODO: Find way to Hyperlink in SQL for link to file
#TODO: 

#Get Full List of names of files in NeedToAddToDatabase folder.
#filesInFolder = copy_file_names(r"F:\ScannedRandomPaperwork\NeedToAddToDatabase")

#FIXME: This is test for function first_split. Rename or delete.
#testStripped = first_split(filesInFolder)
#linksToPaperwork = ms_file_name()