import urllib.request
import re
import os




def localHost_info():
    fp = urllib.request.urlopen('http://localhost:9805/')
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    print(mystr)



localHost_info()