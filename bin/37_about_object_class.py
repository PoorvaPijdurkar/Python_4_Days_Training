"""
3rd way to store and get data

Here we will come to know about
1) Constructor : __new__
2) Initializer: __init__
"""


class Employee:
    company_name = "XYZ Company"

    def __init__(self, name):
        self.name = name

    def get_emp_name(self):
        # All logic to get data in db/file etc will come here
        return self.name

    @classmethod
    def get_company_name(cls):
        # All logic to get data in db/file etc will come here
        return cls.company_name


# Create 2 objects
e1 = Employee("emp-1")
e2 = Employee("emp-2")

# -----------------
# print values
# -----------------
print("comapny name:", Employee.get_company_name())
# object 'Employee' will automatically pass as 1st argument

print("Emp - 1 Name:", e1.get_emp_name())
# object 'e1' will go as 1st argument

print("Emp - 2 Name:", e2.get_emp_name())
# object 'e2' will go as 1st argument

# -----------------