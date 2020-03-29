'''
Python code showing SQL Injection
'''

import sqlite3
conn = sqlite3.connect("users.db")

username = input("Please enter your username: ")
password = input("Please enter your password:")
# This method is prone to SQL Injection
query= f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
c.execute(query)
result = c.fetchone()
if(result):
	print("Welcome Back")
else:
	print("Wrong password")

''' 
SQL Injection would be done by using
' OR 1=1 --
as password
'''

# Preventing SQL Injection
query= "SELECT * FROM users WHERE username= ? AND password= ?"
c.execute(query,(username,password))
result = c.fetchone()
if(result):
	print("Welcome Back")
else:
	print("Wrong password")

# Closing connection
conn.close()