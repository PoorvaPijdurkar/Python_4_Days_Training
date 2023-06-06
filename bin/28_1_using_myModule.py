"""
In this program, we are using variables, functions & classes
defined in mymodule.py
"""

print("about 'import'")
print("-" * 20)
# --------------------
from mypackage.aws import mymodule

# - import will create one EMPTY object called 'mymodule'
# - import will execute mymodule.py
# - when we execute mymodule.py, 2 objects are getting created
#   1) location 2) log_process_func_kw_arg
# - import will keep both objects inside EMPTY object 'mymodule'
# - From mymodule object we can access it
print(dir(mymodule))

print("#" * 40, end="\n\n")
####################################
