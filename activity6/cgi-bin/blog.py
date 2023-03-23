#!/usr/bin/python3
# coding: utf8

import os
import cgi
import json
import time

form = cgi.FieldStorage()

try:
    with open("messages.json", "r") as infile:
        messages = json.load(infile)
except:
    messages = []

messages.append({
    "author": form["author"].value,
    "message": form["message"].value,
    "time": time.strftime("%d/%m/%Y, %H:%M:%S")
})

with open("messages.json", "w") as outfile:
    json.dump(messages, outfile, indent=2, ensure_ascii=False)


print("Content-type: text/html; charset=utf-8")
print()
print("<html><head><title>Messages</title></head><body>")
print("<h1 align='center'>Messages</h1>")
for message in messages:
    print("Author: " + message["author"] + "<br>")
    print("Message: " + message["message"] + "<br>")
    print("Time: " + message["time"] + "<br><br><br>")
print("</body></html>")
