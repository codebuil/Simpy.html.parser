import re
from bs4 import BeautifulSoup
import requests
import os

print("\x1bc\x1b[43;30m")

page = requests.get("https://github.com/codebuil?tab=repositories")
s=str(page.content)
ss=s.split("<")

starts=0
for n in ss:
    sss = n.split(">")
    mm=0
    for m in sss:
        if len(m)>=len("body"):
            if m.find("body"):
                starts=1
        if len(m)>=len("/body"):
            if m.find("/body"):
                starts=0
        if mm > 0:
            if starts!=0:
                print("        ",end="")
        mm+=1
        if starts != 0:
            print(m.strip())



