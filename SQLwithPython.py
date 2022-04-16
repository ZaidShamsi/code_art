import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "learnAndEarn1000"
)

mycursor = mydb.cursor()

mycursor.execute('show databases')

alldbs = mycursor.fetchall()

print('All databases names are:-')
for dbnames in alldbs:
    print(dbnames)

mycursor.execute('use sql_store')

mycursor.execute('show tables')

print('\n\nAll tables in DB sql_store are:-')
tables = mycursor.fetchall()

for tbnames in tables:
    print(tbnames)

mycursor.execute('show columns from customers')

columns = mycursor.fetchall()

print('\n\nColumn names in table customers are:-')
for i in columns:
    print(i)
