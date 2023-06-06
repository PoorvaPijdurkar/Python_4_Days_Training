print("Custom Exception Class-1")
print("-"*20)
# --------------------

# Minimum requirement to create exception class is,
# it should be sub class of 'Exception' class
# OR if some class is already subclass of 'Excpeiont' then we can also
# create sub class of that class like ZeroDivisionError, NameError etc

class MyError(Exception):
    pass # Eventhough it empty, it is valid exception class

try:
    a = 10
    b = 0
    if b == 0:
        raise MyError
    c = a/b
    print("c:",c)
except MyError:
    print("This MyError")


print("#"*40, end="\n\n")
####################################

print("Custom Exception Class-2")
print("-"*20)
# --------------------

# Requirement: Pass some message while raising the exception

class MyError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
try:
    a = 10
    b = 0
    if b == 0:
        raise MyError("Here b value is 0 so raising MyError")
    c = a/b
    print("c:",c)
except MyError as me:
    print("This MyError and details are:", me.error_message)


print("#"*40, end="\n\n")
####################################