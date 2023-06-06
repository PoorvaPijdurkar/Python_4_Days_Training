import urllib.request as ur

my_web_file_handle = ur.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

web_content = my_web_file_handle.read()

my_web_file_handle.close()

web_content = web_content.decode()

from bs4 import BeautifulSoup

soup = BeautifulSoup(web_content, "html.parser")
log_data = soup.body.pre.text

print("list of lines")
print("-"*20)
# --------------------

list_of_lines = log_data.split("\n")
print(list_of_lines)

print("#"*40, end="\n\n")
####################################

# BELOW CODE IS COPIED FROM PROGRAM-4
print("# Task-2: Create Empty files 'web_report.txt' and 'web_report.csv' with heading")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_txt_file_handle = open("web_report.txt", "w")
my_csv_file_handle = open("web_report.csv", "w")

# Step-2: Write Heading
# --------------------
print("IP", "PICS", sep="\t", file=my_txt_file_handle, flush=True)
print("IP", "PICS", sep=",", file=my_csv_file_handle, flush=True)


# Step-3: Disconnect
# --------------------
# We will close at the end

print("""
Files web_report.txt and web_report.csv
created with header, please check
""")

print("#"*40, end="\n\n")
####################################

print("Write to files")
print("-"*20)
# --------------------

for each_line in list_of_lines:
    if each_line.startswith("123"):
        sp = each_line.split()
        ip = sp[0]
        raw_img = sp[6]
        # if raw_img.endswith("jpg") or raw_img.endswith("png") or raw_img.endswith("gif")
        # OR
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"
        print(ip, img, sep="\t", file=my_txt_file_handle, flush=True)
        print(ip, img, sep=",", file=my_csv_file_handle, flush=True)

my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Files web_report.txt and web_report.csv
created with data. Please check
""")

print("#"*40, end="\n\n")
####################################