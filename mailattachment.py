#!/usr/bin/python
import sys
import email
import re
import base64




email = sys.stdin.readlines()

message = str(email)
savelocation = #Insert where files will be saved.
msg = email.message_from_string(message)
for p in msg.walk():
    text = p.get_payload()
    if "Content-Type: text/csv" in text: #Get's content that you are looking for
        index = text.index("Content-Type: text/csv")
        attach = text[index:]
        edit = re.search(r'name="[^",]*', attach)
        #Gets rid of the junk
        attachment = re.search(r"\\n', '\\n',(.*)\\n', '\\n',", attach)
        attachment = attachment.group(0)
        attachment = re.sub(r"\\n', ",'', attachment)
        attachment = re.sub(r"'|\\n|,", '', attachment)
        filename = edit.group(0)[6:]
        ###My Attachment was base64 encoded so I had to add this
        attachment += "===" #Adds padding so Python doesn't freak out
        attachment = base64.b64decode(attachment)
        with open(savelocation+filename, "wb") as file:
            file.write(attachment)
    elif text.index("Content-Type: application/pdf"):
        index = text.index("Content-Type: application/pdf")
        attach = text[index:]
        edit = re.search(r'name="[^",]*', attach)
        #Gets rid of the junk
        attachment = re.search(r"\\n', '\\n',(.*)\\n', '\\n',", attach)
        attachment = attachment.group(0)
        attachment = re.sub(r"\\n', ",'', attachment)
        attachment = re.sub(r"'|\\n|,", '', attachment)
        filename = edit.group(0)[6:]
		###My Attachment was base64 encoded so I had to add this
		attachment += "===" #Adds padding so Python doesn't freak out
		attachment = base64.b64decode(attachment)
        with open(savelocation+filename, "wb") as file:
            file.write(attachment)
