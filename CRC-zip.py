import binascii
import string

crc = 0x7d7741f1

for a in range(0,1000000):
    s = str(a)
    # s = str(a).rjust(5,'0')     #从0开始，补齐4位
    if binascii.crc32(s.encode('utf-8')) == crc:
        print(s)
        exit(0)