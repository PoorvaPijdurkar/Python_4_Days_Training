"""
How to store the data inside the objects
and also how to get the data from object

1-way to store/get

Here we will come to know about,
1) CLASS VARIABLES
2) INSTANCE VARIABLES
"""

class Employee:
    pass

# Create 2 objects
e1 = Employee()
e2 = Employee()

# -----------------
# Store the values in all 2 objects
# -----------------
Employee.company_name = "XYZ Company"
# Inside 'Employee' object, it will create varoiable 'company_name'
# and store the value "XYZ Company"
e1.name = "emp-1"
# Inside 'e1' object, it will create variable 'name'
# and store the value "emp-1"
e2.name = "emp-2"
# Inside 'e2' object, it will create variable 'name'
# and store the value "emp-2"
# -----------------

# -----------------
# Access values
# -----------------
print("company Name:", Employee.company_name)
print("emp-1 name:", e1.name)
print("emp-2 name:", e2.name)
# -----------------




# -----------------
# What is there inside objects
# -----------------
print("\n\n")
print("Inside 'Employee' object:", dir(Employee), sep="\n", end="\n\n")
print("Inside 'e1' object:", dir(e1), sep="\n", end="\n\n")
print("Inside 'e2' object:", dir(e2), sep="\n", end="\n\n")
# -----------------