
# --------------------
# PACKAGES
# --------------------
# - if we create more and more modules then we can keep/store/organize
#   in folders & sub folders - these folders are called PACKAGES
# - we can directly import from packages
# --------------------

print("1 - way to 'import'")
print("-"*20)
# --------------------

import mypackage.aws.mymodule
print("location:", mypackage.aws.mymodule.location)
print("log result:", mypackage.aws.mymodule.log_process_func_kw_arg(log_file_path="server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("2 - way to 'import'")
print("-"*20)
# --------------------

import mypackage.aws.mymodule as mm
print("location:", mm.location)
print("log result:", mm.log_process_func_kw_arg(log_file_path="server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("3 - way to 'import'")
print("-"*20)
# --------------------

from mypackage.aws.mymodule import location, log_process_func_kw_arg
print("location:", location)
print("log result:", log_process_func_kw_arg(log_file_path="server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("4 - way to 'import'")
print("-"*20)
# --------------------

from mypackage.aws.mymodule import location as lc, log_process_func_kw_arg as lpf
print("location:", lc)
print("log result:", lpf(log_file_path="server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("5 - way to 'import'")
print("-"*20)
# --------------------

from mypackage.aws.mymodule import *
print("location:", location)
print("log result:", log_process_func_kw_arg(log_file_path="server_log.txt"))

print("#"*40, end="\n\n")
####################################