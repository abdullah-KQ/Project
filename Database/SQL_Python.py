import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "sqluser1",
    password = "password"
)
 
# Printing the connection object
print(mydb)