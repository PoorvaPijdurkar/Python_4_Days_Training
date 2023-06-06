print("Extract PICS - 1 -way")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_pics = in_string.index("/pics/")
start_index = index_of_pics + 6

# 1-way
# end_index = in_string.index("HTTP")
# end_index = end_index - 1

# 2-way
end_index = in_string.index(" ", start_index)

img = in_string[start_index:end_index]
print(img)

print("#"*40, end="\n\n")
####################################

print("Extract PICS - 2 -way")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = in_string.split()
print(sp)

raw_img = sp[6] # '/pics/wpaper.gif'

# Remove /pics/ 1-way
img_1 = raw_img[6:]

# Remove /pics/ 2-way
img_2 = raw_img.removeprefix("/pics/")

print(img_1, img_2, sep="\n")

print("#"*40, end="\n\n")
####################################