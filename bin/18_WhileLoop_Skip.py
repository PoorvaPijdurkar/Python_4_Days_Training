

print("# Case-2: How to skip current iteration & go for next iteration")
print("-"*20)
# --------------------

my_courses = ["Perl", "Java-1", "python", "Java-2", "C++"]
print("my_courses:", my_courses, end="\n\n")

index_no = 0
while index_no < len(my_courses):
    if not my_courses[index_no].startswith("Java"):
        index_no = index_no + 1
        continue
    # Below code applicable for Java Courses
    print("This Java Course Name is:", my_courses[index_no])
    print("This is one version of java")
    print("This java course duration is 4 days", end="\n\n")
    index_no = index_no + 1


# for each_course in my_courses:
#     if not each_course.startswith("Java"):
#         continue
#     # Below code applicable for Java Courses
#     print("This Java Course Name is:", each_course)
#     print("This is one version of java")
#     print("This java course duration is 4 days", end="\n\n")

print("#"*40, end="\n\n")
####################################