
import urllib.request as ur
# Step-1: Connect
# --------------------
my_web_file_handle = ur.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

# Step-2: Read
# --------------------
web_content = my_web_file_handle.read()
my_web_file_handle.close()
web_content = web_content.decode()
print("#"*40, end="\n\n")
####################################

print("# Task-2: Extract info using beautifulsoup")
print("-"*20)
# --------------------
from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")
log_data = soup.body.pre.text
list_of_lines = log_data.split("\n")
print(list_of_lines)
print("Extract IP, DATE, PICS, URL")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*(http[s]?://[0-9a-zA-Z./_]+).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url)

# COMMENT
'''

http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

https? = s is optional
http[s]? = s is optional
(https)? = 'https' is optional

http[s]?://[0-9a-zA-Z./_]+
'''

print("#"*40, end="\n\n")
####################################






# BELOW CODE IS COPIED FROM PROGRAM-4
print("# Task-2: Create Empty files 'regex_report.txt' and 'regex_report.csv' with heading")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_txt_file_handle = open("regex_report.txt", "w")
my_csv_file_handle = open("regex_report.csv", "w")

# Step-2: Write Heading
# --------------------
print("IP", "PICS", sep="\t", file=my_txt_file_handle, flush=True)
print("IP", "PICS", sep=",", file=my_csv_file_handle, flush=True)


# Step-3: Disconnect
# --------------------
# We will close at the end

print("""
Files regex_report.txt and regex_report.csv
created with header, please check
""")

print("#"*40, end="\n\n")
####################################

print("Write to files")
print("-"*20)
# --------------------

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*(http[s]?://[0-9a-zA-Z./_]+).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url, sep="\t", file=my_txt_file_handle, flush=True)
        print(ip, dt, img, url, sep=",", file=my_csv_file_handle, flush=True)


my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Files regex_report.txt and regex_report.csv
created with data. Please check
""")

print("#"*40, end="\n\n")
####################################