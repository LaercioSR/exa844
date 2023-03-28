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

print('<div>')
print('<h1 align="center">Message Form</h1>')
print('<hr />')
print('<br />')
print('<form method="POST" action="/cgi-bin/blog.py" align="center">')
print('  Author: <br />')
print('  <input type="text" size="64" name="author" /><br /><br />')
print('  Message: <br />')
print('  <textarea rows="3" cols="64" name="message"></textarea><br /><br />')
print('  <input type="submit" value="Submit" />')
print('  <input type="reset" value="Reset" />')
print('</form>')
print('<hr />')
print('</div>')

print('<br />')
print('<br />')
print('<br />')
print('<br />')
print("<h1 align='center'>Messages</h1>")
print('<hr />')
print('<div align="center">')
for message in sorted(messages, key=lambda d: d["time"], reverse=True):
    print("<b>Author:</b> " + message["author"] + "<br>")
    print("<b>Message:</b> " + message["message"] + "<br>")
    print("<b>Time:</b> " + message["time"] + "<br><br><br>")
print('</div>')
print('<hr />')
print("</body></html>")
