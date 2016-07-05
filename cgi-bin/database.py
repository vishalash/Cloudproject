#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='ash12', database='fabbadal')
cursor = mariadb_connection.cursor()

name1=raw_input()
email1=raw_input()
try:
  cursor.execute("INSERT INTO user (name,email) VALUES (%s,%s)", (name1,email1))
except mariadb.Error as error:
  print("ERROR: {}".format(error))


mariadb_connection.commit()

cursor.execute("SELECT name,email FROM user WHERE name=%s",(name1,))


for name, email in cursor:
    print("name: {}, email: {}").format(name,email)

mariadb_connection.close()

raw_input()
