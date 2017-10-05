import sqlite3
import os

conn=sqlite3.connect("practice.db")
curs=conn.cursor()
print(curs.execute("select name from sqlite_master where type='table'"))
print(curs.fetchall())

#curs.execute("Create TABLE zoo (name VARCHAR(20)PRIMARY KEY,pass VARCHAR(20))")

#curs.execute('''INSERT INTO zoo VALUES("shibata","datasection418")''')
#print(curs.execute('''SELECT * from zoo where name={} '''.format("foo' or name=name-- ")))
#name="foo'                                                                  v or name=name-- "
name="shibata"
password="datasection418"#"foo' or name=name-- "
text="select * from zoo where name='%s' and  pass='%s'" % (name,password)
print(text)

print(curs.execute(text))

#print(curs.execute("SELECT * from zoo where name={} ".format(name)))

print(curs.fetchall())

conn.commit()

curs.close()
#print(os.getcwd())