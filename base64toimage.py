import os,base64
with  open("1.txt","r") as f:
    imgdata = base64.b64decode(f.read())
file = open('1.jpg', 'wb')
file.write(imgdata)
file.close()