import sqlite3

def translate(From, To, Word):
    con = sqlite3.connect('FinalVersionSalinguahe/dialect.db')
    c = con.cursor()
    c.execute(f"SELECT {To} FROM dialect where {From} = '{Word.upper()}'")
    con.commit()
    try:
        return c.fetchall()[0][0]
    except:
        return Word  
    con.close()

print(translate("Tagalog","Bisaya","Tagalog78"))

