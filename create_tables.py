import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()
# we will create new table with an auto-incrementing id
create_table= "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)" #we don't need to specify id of an user as INTEGER will automatically assign id by auto incrementation column
cursor.execute(create_table)
create_table= "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY,name text,price float)" #real is like float with decimal point
cursor.execute(create_table)
#cursor.execute("INSERT INTO items VALUES ('test',10.99)")
connection.commit()

connection.close()