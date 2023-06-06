"""
GEt data from web
and
extract using regular expression
"""

# --------------------
# Split into smaller
# --------------------
# Task-1: Get data from website using urllib-Keep it in variable
# Task-2: Extract log data using beautifulsoup
# Task-3: Extract info using regular expression
# --------------------

print("# Task-1: Get data from website using urllib-Keep it in variable")
print("-"*20)
# --------------------

import urllib.request as ur

# Step-1: Connect
# --------------------
my_web_file_handle = ur.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

# Step-2: Read
# --------------------
web_content = my_web_file_handle.read()

# Step-3: Disconnect
# --------------------
my_web_file_handle.close()

web_content = web_content.decode()
print(web_content)

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

print("#"*40, end="\n\n")
####################################

print("# Task-3: Extract info using regular expression")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    # match_result = re.match('which pattern?', 'on which string')
    match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*',each_line)
    print("Each Line:", each_line)
    print("Match result:", match_result, end="\n\n")

# COMMENT - 2
'''
Regular Expression

# IDENTIFIERS
\d -> represents any one digit b/n 0-9
\D -> represents any one non-digit. except 0-9
. -> represent any ONE ANY character
\. -> represent strictly DOT
[.] -> represent strictly DOT
[0-9] -> represents any one digit b/n 0-9. Here we can specify range like 0-5

# QUANTIFIERS
\d{3} -> internally it will make \d\d\d
\d{1,3} -> internally it will make (\d|\d\d|\d\d\d)

# MOPDIFIERS
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 times
'''

# COMMENT - 1
'''
IP Address line pattern, 
which means we need to tell how ip address line looks like?

IP Address line looks like
FROM THE BEGINNING
1 to 3 digits then DOT
then
1 to 3 digits then DOT
then
1 to 3 digits then DOT
then
1 to 3 digits then SOME CHARACTERS PRESENT TILL THE END
'''

print("#"*40, end="\n\n")
####################################