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

print("Extract IP")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)

# COMMENT
'''
- put () for ip address portion - called group
'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*'
- group number starting from 1
'''
print("#"*40, end="\n\n")
####################################




print("Extract IP, DATE")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT
'''
26/Apr/2000

26
-------
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
[0-9]\d # Strictly 2 digits
\d[0-9] # Strictly 2 digits

\d{1,2} # minimum 1 digit, maximum 2
[0-9]{1,2} # minimum 1 digit, maximum 2
\d?\d # minimum 1 digit, maximum 2
[0-9]?[0-9] # minimum 1 digit, maximum 2
\d?[0-9] # minimum 1 digit, maximum 2
[0-9]?\d # minimum 1 digit, maximum 2
-------

Apr
-------
[a-zA-Z]{3}
[A-Z][a-z]{2}
(Jan|Feb|Mar)
-------
'''
print("#"*40, end="\n\n")
####################################





print("Extract IP, DATE, PICS: PARTIAL OUTPUT - 1")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/pics/([0-9a-z]+\.(gif|jpg)).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(4)
        print(ip, dt, img)

# COMMENT
'''
\s -> one SPACE
\S -> any one character except SPACE
'''

print("#"*40, end="\n\n")
####################################