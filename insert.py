import sqlite3
connection = sqlite3.connect("insert.db")

# Create cursor object
c = connection.cursor()

# Execute SQL
# Create Table
c.execute("CREATE TABLE my_info (first_name TEXT, last_name TEXT, age INTEGER, gender TEXT);")
insert_query = '''INSERT INTO my_info VALUES ('Dhruv', 'Shetty', 21, 'Male')'''		# Using ''' insertion
c.execute(insert_query)

# Bad way of insertion (using f string)
form_first = "Lorem"
query = f"INSERT INTO my_info (first_name) VALUES ('{form_first}')"
c.execute(query)

# Better way
form_first = "Ipsum"
query = "INSERT INTO my_info (first_name) VALUES (?)"
c.execute(query, (form_first,))

# OR via creating a tuple
data = ("Steve", "Irwin", 47, 'Male')
query = "INSERT INTO my_info VALUES (?,?,?,?)"
c.execute(query, data)

# Commit changes
connection.commit()
connection.close()