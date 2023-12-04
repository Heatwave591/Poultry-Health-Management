import sqlite3
connect = sqlite3.connect("db1.db")
cursor = connection.cursor()

command1 = '''CREATE TABLE ALLDATA(Tempreture FLOAT, Pressure FLOAT, Humidity FLOAT, Gas FLOAT)'''
cursor.excecute(command1)

cursor.excecute(INSERT INTO ALLDATA VALUES('Tempdata. txt',readfile('D:\
Telibhrama\Tempdata.txt')))

cursor.excecute("SELECT * FROM ALLDATA")

result = cursor.fetchall()
print(result)