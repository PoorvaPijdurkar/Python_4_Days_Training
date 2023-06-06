"""
conditional statement 'if': Based on the condition if we want to execute
block of statements

In some languages
if some_condition
{
    s1
        s2
    s3
}
s4

In python, we wont use {} to make block instead we use indentation
if some_condition
    s1
    s2
    s3
s4
"""
print("Only 'if'")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")

if x > 10:
    print("Value of x is greater than 10")

if x < 10:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
####################################



print("if-elif")
print("-"*20)
# --------------------
x = 10
if x == 10:
    print("Value of x is 10")

elif x > 10:
    print("Value of x is greater than 10")

elif x < 10:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
####################################


print("if-elif-else")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")

elif x > 10:
    print("Value of x is greater than 10")

else:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
####################################