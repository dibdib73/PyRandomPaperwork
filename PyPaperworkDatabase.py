#PyPaperworkDatabase
import os
import pyodbc

'''Starting with connection to database using pyodbc. Then modifiing the database.'''
connStr = (
    r"DRIVER = {Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=F:\ScannedRandomPaperwork\A_ScannedPaperworkInThisFile.accdb;"
)
conn = pyodbc.connect(connStr)
# Execute a SELECT statement
cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table")

# Fetch all rows
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)


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



filesInFolder = copy_file_names(r'F:\ScannedRandomPaperwork')
strippedTest = first_split(filesInFolder[1])

print(strippedTest)