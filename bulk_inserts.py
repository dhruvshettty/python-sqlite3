'''
Python code showcasing Bulk Insert
using executemany() or a For Loop
'''

import sqlite3
connection = sqlite3.connect("friends.db")

# Create cursor object
c = connection.cursor()

# Execute SQL
# Creating table
create_table = "CREATE TABLE friends ('first_name', 'last_name', 'closeness');"
c.execute(create_table)

# Bulk Insert
friends = [
	("Joey", "Tribbiani", 10),
	("Rachel", "Green", 8),
	("Phoebe", "Buffay", 5),
	("Ross Geller", "Adams", 6),
	("Monica", "Geller", 7),
	("Chandler", "Bing", 9)
]

# Method 1 of Bulk Insert
c.executemany("INSERT INTO friends VALUES (?,?,?)", friends)

# Method 2 of Bulk Insert
for friend in friends:
	c.execute("INSERT INTO friends VALUES (?,?,?)", friend)
	print("INSERTING NOW!")

# Commit changes and close
connection.commit()
connection.close()