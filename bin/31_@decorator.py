print("Using Decorator Design Pattern - FINAL DECORATOR")
print("-"*20)
# --------------------


def my_decorator(my_func):
    def decorated_func(x,y):
        print("Result is")
        my_func(x,y) # add1(10,20)
        print("End of the result", end="\n\n")
    return decorated_func

@my_decorator
def add1(a,b):
    print(a+b)

add1(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(add1) # my_func=add1
# inner_func(10,20) # x=10, y=20
# -------------

@my_decorator
def add2(a,b):
    print(a+b+b)

add2(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(add2) # my_func=add2
# inner_func(10,20) # x=10, y=20
# -------------

@my_decorator
def sub1(a,b):
    print(a-b)

sub1(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(sub1) # my_func=sub1
# inner_func(10,20) # x=10, y=20
# -------------
@my_decorator
def sub2(a,b):
    print(a-b-b)

sub2(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(sub2) # my_func=sub2
# inner_func(10,20) # x=10, y=20
# -------------


print("#"*40, end="\n\n")
####################################