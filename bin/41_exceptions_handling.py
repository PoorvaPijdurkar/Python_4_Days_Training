"""
Exceptions handling
"""

# print("Without handling exceptions")
# print("-"*20)
# # --------------------
#
# a = 10
# b = 0
# c = a/b # Program will terminate here abruptly
# print("c:",c)
#
# print("#"*40, end="\n\n")
# ####################################

print("try-except")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    c = a/b # Program will not termintate here, instead control will be passed to 'except' block
    print("c:",c)
except:
    print("Some error in try block =, so reached except block")
    print("Write logic to solve error occurred in try")
    # import sys
    # sys.exit(0) # If we want to terminte the program

print("#"*40, end="\n\n")
####################################