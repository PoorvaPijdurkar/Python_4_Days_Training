

print("Function with no return value: None")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with no return statement: None")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with one line expression in return ")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return (10+30)/(1+2) # return the result


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################