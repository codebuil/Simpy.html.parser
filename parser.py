
import requests
import os

print("\x1bc\x1b[43;30m")

page = requests.get("https://github.com/codebuil?tab=repositories")
s=str(page.content)
ss=s.split("<")

starts=0
startss=0
startsss=0
startssss=0
for n in ss:
    sss = n.split(">")
    mm=0
    startss=0
    for m in sss:
        m=m.strip()
        if len(m)>=len("body") and mm==0:
            f=m.find("body")
            if f<2 and f>-1:
                starts=1
        if len(m)>=len("/body") and mm==0:
            f=m.find("/body")
            if f<2 and f>-1:
                starts=0
        if len(m)>=len("a ") and mm==0:
            f=m.find("a ")
            if f<2 and f>-1:
                startss=1
        if len(m)>=len("/a") and mm==0:
            f=m.find("/a")
            if f<2 and f>-1:
                startss=0
        if len(m)>=len("h3") and mm==0:
            f=m.find("h3")
            if f<2 and f>-1:
                startsss=1 
             
        if len(m)>=len("h3") and mm==0:
            f=m.find("/h3")
            if f<2 and f>-1:
                startsss=0  
        if starts != 0 and mm==0 and startss!=0 and startsss!=0:
            m=m.replace("\\r","")
            m=m.replace("\\n","")
            m1:int=m.find("href=")
            if m1>-1:
                m=m[m1:]
                m11=m.split("\"",m1)
                if len(m11)>1:
                    print("http://github.com"+m11[1].strip()+"->", end="")
                    
        if starts != 0 and mm>0 and startss!=0 and startsss!=0:
            m=m.replace("\\r","")
            m=m.replace("\\n","")
            print(m.strip())
        if len(m)>=len("Stars") and mm==1:
            f=m.find("Stars")
            if f<2 and f>-1:
                startssss=1 
        mm+=1
    startss=0    

