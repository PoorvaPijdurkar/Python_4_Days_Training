"""
How to communicate(Read/Write) with external files(Text files)
Text files like .txt, .csv, .log, .mylog, .yourlog etc
Finally file which can be opened in NOTEPAD
"""

'''
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
'''

'''
We have functions for each step
Step-1: Connect to file
    - open function
Step-2: Read/Write
    - To Write: 1)write 2) writelines 3) print function
    - To Read: 1) read 2) readline 3) readlines 4) list/tuple/set/dictionary classes to read file
Step-3: Disconnect
    - flush() # Send data from buffer to file. It will NOT CLOSE the connection
    - close() # close will 1st call flush() then disconnect or close the connection 
'''
print("All write operations")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
# my_file_handle = open("provide file name or file path here", "provide mode here")
my_file_handle = open("my_out_file.txt", "w")
# mode "w": It will create new file
# mode "w": It will ERASE the complete data if present in the file
# mode "w": Write only

# Step-2: Write
# --------------------

# Our data
x = 10
s = "Python\n"

# Convert other type of data into string becasue 1)write & 2) writelines
#   methods expects data in strings
x = str(x) + "\n"

# 1) write : Use this option when we have data in single string which
#   we want to write to file. Means, write will take single string of any length
my_file_handle.write(x) # It will Send data to buffer
my_file_handle.write(s) # It will Send data to buffer
my_file_handle.flush() # It will send data present in buffer to file (my_out_file.txt)

# 2) writelines: Use this option when we have data in any collection
#   like list/tuple etc. Means, writelines will take collection of values
my_data_in_list = [x, s]
my_file_handle.writelines(my_data_in_list)
my_file_handle.flush()

# 3) print function
# not required to add \n
x = x.strip() # remove\n or extra spaces
s = s.strip() # remove\n or extra spaces
print(x, s, 20, "Java", sep="\n", end="", file=my_file_handle, flush=True)
# 20-> not required to convert to string

# Step-3: Disconnect
# --------------------
my_file_handle.close()

print("""
All write operations completed.
Please check my_out_file.txt
""")

print("#"*40, end="\n\n")
####################################