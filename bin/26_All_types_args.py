

print("All types of args in ONE function")
print("-"*20)
# --------------------


# We can combine both positional & named arguments in single function
def add(a, b=10, *c, d, e=20, **f):
    return a + b + sum(c) + d + e + sum(f.values())


add_result_1 = add(10, d=20)
# a = 10, b = 10, c = ()
# d = 20, e = 20, f = {}
print("add_result_1:", add_result_1) # 60

add_result_2 = add(10, 20, 30, 40, 50, d = 60, e=70, x=80, y=90, z=100)
# a = 10, b = 20, c = (30, 40, 50)
# d = 60, e = 70, f = {x:80, y:90,z:100}
print("add_result_2:", add_result_2) # 550

print("#"*40, end="\n\n")
####################################