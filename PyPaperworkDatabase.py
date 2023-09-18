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

def copy_file_names(folder_path):
    for fileName in os.listdir(folder_path):
        filesInFolder.append(fileName)
    return filesInFolder

def first_split(firstBreak):
    stripped = firstBreak.pop(0)
    stripped = stripped[0 : -4]
    stripped = stripped.split('_')
    return stripped

def add_to_db(contentAdd):
    if len(contentAdd) == 2:
        valID          = ''
        val1           = "'" + contentAdd[0] + "'"
        val2           = "'" + contentAdd[1] + "'"
        valPages       = 0
        today          = date.today()
        valLink        = 'CurDir() + "ContentAdd[0]" + "ContentAdd[1]" + "PDF"'
        valNote        = "NULL"
        valDate        = 0
        valThisIsABill = "NULL"
        cont1 = cursor.execute("INSERT INTO Scanned_paperwork (ID, Type, Paperwork_name, Number_of_Pages, Date_scanned, Link_to_paperwork, Notes, Date_of_paperwork, Is_This_a_Bill)"
                       "VALUES (valID, val1, val2, valPages, today, valLink, valNote, valDate, ValThisIsABill);"
                       )
    elif len(contentAdd) == 3:
        valID          = ''
        val1           = contentAdd[0]
        val2           = contentAdd[1]
        valPages       = 0
        today          = date.today()
        valLink        = 'add'
        valNote        = "NULL"
        valDate        = contentAdd[2]
        valThisIsABill = "NULL"
        cursor.execute("INSERT INTO Scanned_paperwork (ID, Type, Paperwork_name, Number_of_Pages, Date_scanned, Link_to_paperwork, Notes, Date_of_paperwork, Is_This_a_Bill)"
                       "VALUES (valID, val1, val2, valPages, today, valLink, valNote, valDate, ValThisIsABill);")
    else:
        print("Error with content length")

#Get Full List
filesInFolder = copy_file_names(r"F:\ScannedRandomPaperwork\NeedToAddToDatabase")

#Iterate through full list split apart and add to db
def iter_through_full_list(filesInFolder):
    for i in filesInFolder:
        stripped = first_split(filesInFolder)
        print(stripped)

testStripped = first_split(filesInFolder)
testAdd = add_to_db(testStripped)