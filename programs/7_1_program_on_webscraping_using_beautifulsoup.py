print("# Task-1: Get data from website using urllib-Keep it in variable")
import urllib.request as ur

my_web_file_handle = ur.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

web_content = my_web_file_handle.read()

my_web_file_handle.close()

web_content = web_content.decode()
print(web_content)

print("# Task-2: Extract info using beautifulsoup")
print("-"*20)
# --------------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")
print(soup)
print("#"*40, end="\n\n")

print("Head tag")
print("-"*20)
# --------------------

print(soup.head)
print("#"*40, end="\n\n")
####################################

print("Title tag")
print("-"*20)
# --------------------

print(soup.head.title) # <TITLE>A Web server log file explained</TITLE>

print("#"*40, end="\n\n")
####################################


print("Title tag text")
print("-"*20)
# --------------------

print(soup.head.title.text) # A Web server log file explained

print("#"*40, end="\n\n")
####################################

print("1st link tag")
print("-"*20)
# --------------------

print(soup.head.link) # <LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">

print("#"*40, end="\n\n")
####################################

print("all link tags")
print("-"*20)
# --------------------

print(soup.head.find_all('link'))

print("#"*40, end="\n\n")
####################################

print("log data")
print("-"*20)
# --------------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
####################################

print("log data in raw format")
print("-"*20)
# --------------------

print(repr(log_data))

print("#"*40, end="\n\n")
####################################