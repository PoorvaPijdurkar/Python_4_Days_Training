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
'''
-------
r[ea]d
-------
red
rad
-------
r[ea]{1,2}d
-------
red
rad
read
raed
-------
r[ea]+d
-------
red
rad
read
raed
-------
r[ea]*d
-------
rd
red
rad
read
raed
-------
r*d
-------
d
rd
rrd
rrrrd
-------

[r]*d
-------
d
rd
rrd
rrrrd
-------
r[ea]?d
-------
rd
red
rad
-------
'''
print("Extract IP, DATE, PICS")
print("-" * 20)
# --------------------
import re

for each_line in list_of_lines:
    match_result = re.match(
        '(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*',
        each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        print(ip, dt, img)

# COMMENT
'''
Make this "pics/wpaper.gif" portion optional so that it will match
the lines which is not having pics

(pics/([0-9a-z]+\.(gif|jpg)))?
'''

print("#" * 40, end="\n\n")
####################################