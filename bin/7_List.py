print("List PART-3")
print("Methods inside 'list' class")
print("-"*20)
# --------------------

print(dir(list), end="\n\n")

# OR
# print(dir(my_list))

print("#"*40, end="\n\n")
####################################

print("List PART-4")
print(" 'append' method")
print("-"*20)
# --------------------

my_list = [10, 12.5, "Python", [100, 200]]
print("my_list:", my_list, end="\n\n")

my_list.append("Java")
my_list[3].append(300)

print("my_list after append:", my_list)

print("#"*40, end="\n\n")
####################################