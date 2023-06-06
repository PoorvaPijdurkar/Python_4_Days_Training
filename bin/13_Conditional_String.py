print("if-with strings")
print("-"*20)
# --------------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

if my_string != "Java" and my_string != "C++":
    print("Not Java/C++")

if not my_string.startswith("Perl"):
    print("Not Perl")

if "tho" in my_string:
    print("Substring 'tho' found")

print("#"*40, end="\n\n")
####################################