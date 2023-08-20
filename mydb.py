# Install Mysql on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
# https://codemy.com/git



import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql123#',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS salescompany")

print("All done!")

