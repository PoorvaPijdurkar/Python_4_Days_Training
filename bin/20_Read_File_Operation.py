print("Read operations: 1) read")
print("-"*20)
# --------------------
# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
file_content = my_file_handle.read()
# read(): will return COMPLETE file content in single string
print("file_content:", file_content)
print("file_content in RAW FORMAT:", repr(file_content))

# Step-3: Disconnect
# --------------------
my_file_handle.close()

print("#"*40, end="\n\n")
####################################



print("Read operations: 2) readline")
print("-"*20)
# --------------------
# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
file_content = my_file_handle.readline()
print("1st line:", file_content)

file_content = my_file_handle.readline()
print("2nd line:", file_content)

file_content = my_file_handle.readline()
print("3rd line:", file_content)

# Internally it uses pointer called 'seek' to track the lines
# seek(charater_index, line_no)

# Set seek to 0th position. ie beginning of the file
my_file_handle.seek(0)
file_content = my_file_handle.readline()
print("1st line:", file_content)

# Step-3: Disconnect
# --------------------
my_file_handle.close()
print("#"*40, end="\n\n")
####################################



print("Read operations: 3) readline by line using for-loop")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# --------------------
my_file_handle.close()

print("#"*40, end="\n\n")
####################################




print("Read operations: 4) readlines, list, tuple, set, dict")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
file_content = my_file_handle.readlines()
# return complete data in list
print("File_content using readlines():", file_content, end="\n\n")
# Seek reached EOF

# set seek to beginning of the file
my_file_handle.seek(0)
file_content = list(my_file_handle)
print("file_content in list:", file_content, end="\n\n")
# Seek reached EOF


# set seek to beginning of the file
my_file_handle.seek(0)
file_content = tuple(my_file_handle)
print("file_content in tuple:", file_content, end="\n\n")
# Seek reached EOF

# set seek to beginning of the file
my_file_handle.seek(0)
file_content = set(my_file_handle)
print("file_content in set:", file_content, end="\n\n")
# Seek reached EOF

# set seek to beginning of the file
my_file_handle.seek(0)
file_content = dict(enumerate(my_file_handle))
print("file_content in dict:", file_content, end="\n\n")
# Seek reached EOF

# Step-3: Disconnect
# --------------------
my_file_handle.close()

# COMMENT:
# Example-1
# >>> L = [10, 20, 30]
# >>> dict(L)
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     dict(L)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
#
# Example-2:
# >>> M = [(0,10), (1,20), (2,30)]
# >>> dict(M)
# {0: 10, 1: 20, 2: 30}
#
# Example-3:
# >>> L
# [10, 20, 30]
# >>> e = enumerate(L)
# >>> list(e)
# [(0, 10), (1, 20), (2, 30)]
# >>>

print("#"*40, end="\n\n")
####################################