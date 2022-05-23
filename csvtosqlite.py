#This file's for transfering data from a csv file created from excel

import csv
import sqlite3

con = sqlite3.connect('FinalVersionSalinguahe/dialect.db')
c = con.cursor()

#create table error handling included
try:
    c.execute('''create table dialect (Tagalog text unique, 
                                        Bisaya text unique, 
                                        Cebuano text unique, 
                                        Ilocano text unique)''')
except:
    pass

#open csv file
with open('FinalVersionSalinguahe/csvdata.csv','r') as f:
    dataset = csv.reader(f)

    #insert csv data to database (duplicate filter implemented)
    for rows in dataset:
        try:
            c.execute("INSERT INTO dialect VALUES (?,?,?,?)",rows)
        except:
            pass

con.commit()

#query all for checking

def translate(From, To, Word):
    c.execute(f"SELECT {To} FROM dialect where {From} = '{Word}'")
    con.commit()
    print(c.fetchall())

translate("Tagalog","Bisaya","TAGALOG1")

con.close()