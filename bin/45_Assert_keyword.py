print("assert")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    assert b > 0
    # If condition fails then throw AssertionError
    c = a/b
    print("c:",c)
except AssertionError:
    print("This AError")


print("#"*40, end="\n\n")
####################################






print("raise")
print("-"*20)
# --------------------
# 'assert' will always throw assertion error
# in 'raise', we can specify type of error to throw

try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDivisionError
    c = a/b
    print("c:",c)
except AssertionError:
    print("This AError")


print("#"*40, end="\n\n")
####################################





print("raise")
print("-"*20)
# --------------------

# 'assert' will always throw assertion error
# in 'raise', we can specify type of error to throw

try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDivisionError
    c = a/b
    print("c:",c)
except ZeroDivisionError:
    print("This AError")


print("#"*40, end="\n\n")
####################################