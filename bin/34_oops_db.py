# -----------------
# Example: I need to store single database details
# -----------------

# 1-way # Storing in global scope
host='192.168.1.10'
port=1234
username="abc"
pasword="xyz"
db="mydb"

# 2-way # storing inside object
class dbDetails:
    pass

dbDetails.host='192.168.1.10'
dbDetails.port=1234
dbDetails.username="abc"
dbDetails.pasword="xyz"
dbDetails.db="mydb"
# -----------------


# -----------------
# Example: I need to store 2 database details
# -----------------

# 1-way # Storing in global scope
host_1='192.168.1.10'
port_1=1234
username_1="abc"
pasword_1="xyz"
db_1="mydb"

host_2='192.168.1.11'
port_2=1234
username_2="abc"
pasword_2="xyz"
db_2="mydb"

# 2-way # storing inside object
class dbDetails:
    pass

db1 = dbDetails()
db2 = dbDetails()

db1.host='192.168.1.10'
db1.port=1234
db1.username="abc"
db1.pasword="xyz"
db1.db="mydb"

db2.host='192.168.1.11'
db2.port=1234
db2.username="abc"
db2.pasword="xyz"
db2.db="mydb"

# -----------------