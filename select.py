'''
Python code showcasing Select using
fetchall(), fetchone() or a For Loop
'''

import sqlite3
conn = sqlite3.connect("insert.db")

# Creating a cursor
c = conn.cursor()

# Execute SQL
# Reading data from insert.db
# Using FOR loop in printing
query = "SELECT * FROM my_info"
c.execute(query)
for result in c:
	print(result)

''' 
Note: cursor is executed again because it would
be at the end of the iterator
'''
# Using fetchall() gives a list
c.execute(query)
print(c.fetchall())

# Using fetchone() gives only first result
c.execute(query)
print(c.fetchone())

# Closing cursor
c.close()