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
cursor.execute("SELECT * FROM Scanned_paperwork")

'''Modification of database'''
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

def add_to_db(contentAdd):
    if len(contentAdd) == 2:
        val1 = contentAdd[0]
        val2 = contentAdd[1]
        today = date.today()
        cursor.execute("INSERT INTO Scanned_paperwork (Type, Paperwork_name, Date_scanned, Link_to_paperwork)"
                       "VALUES (val1, val2, today, firstBreak)"
                       )

#Get Full List
filesInFolder = copy_file_names(r"F:\ScannedRandomPaperwork\NeedToAddToDatabase")

#Iterate through full list split apart and add to db

strippedTest = first_split(filesInFolder[1])

