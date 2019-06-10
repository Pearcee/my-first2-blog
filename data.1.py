import pypyodbc # pip install pypyodbc
import csv

Driver ='{SQL Server}'
#Server = 'Apollo\\CapitaTest'
Server = 'INDI\REPORTSERVER'

Database = 'OpenHousingSQLViews'

cnxn  = pypyodbc.connect('Driver=' + Driver + '; Server='+ Server + '; Database=' + Database +';')
cursor = cnxn.cursor()

def selectTable(table):
    SQL = 'SELECT * FROM ' + table
    cursor.execute(SQL)

def saveTable(table):
    field_names = [i[0] for i in cursor.description]
    with open(table + '.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',' )
        spamwriter.writerow(field_names)
        for row in cursor:
            spamwriter.writerow(row)

def close():
    cursor.close()
    cnxn.close()

tablelist =  'sp_job_today' #rm_components', 'rm_appliance_make'  #, 'rm_appliance_model', 
for table in tablelist:
    print(table)
    selectTable(table)
    for i in cursor:
        print(i)


close()


'''

    saveTable(table)
'''