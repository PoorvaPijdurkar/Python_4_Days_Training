

print("try-except-else-finally")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    c = a/b
    print("c:",c)
    # Example: DB connection logic here
except:
    # Handle only DB connection Error Here
    print("Some error in try block, so reached except block")
else:
    # If DB connection success then execute queries here
    print("Executing Else Block")
finally:
    print("Executing Finally Block")
    # Example:Close DB connection here
    # any cleanup activity we can use this


# if "try" success/failed but finally will execute
# if "except" success/failed but finally will execute
# if "else" success/failed but finally will execute
# So, finally will always execute

print("#"*40, end="\n\n")
####################################