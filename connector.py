import mysql.connector

#connect to db

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="users"
)
mycursor=mydb.cursor()