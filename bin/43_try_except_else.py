

print("try-except-else")
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

# if "try" success then execute "else" block and skip "except" block
# if "try" failed then execute "except" block and skip "else" block

print("#"*40, end="\n\n")
####################################