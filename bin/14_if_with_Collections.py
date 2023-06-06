print("if-with list/tuple/set/Any other collections")
print("-" * 20)
# --------------------

my_courses = ["Perl", "Java-1", "python", "Java-2", "C++"]
print("my_courses:", my_courses, end="\n\n")

if "Java-1" in my_courses:
    print("Course 'Java-1' present")

print("#" * 40, end="\n\n")
####################################



print("if-with dictionary")
print("-" * 20)
# --------------------

my_dictionary = {"course": "python", "duration": 4, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.keys()
# dict_keys(['course', 'duration', 'mode'])
if "course" in my_dictionary.keys():
    print("Key 'course' Found")

# my_dictionary.values()
# dict_values(['python', 4, 'online'])
if "python" in my_dictionary.values():
    print("Value 'python' present")

# my_dictionary.items()
# dict_items([('course', 'python'), ('duration', 4), ('mode', 'online')])
if ('course', 'python') in my_dictionary.items():
    print("Item '('course', 'python')' Present")

print("#" * 40, end="\n\n")
####################################