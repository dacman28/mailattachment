# mailattachment
I wrote this script so that I could pipe emails into a python script from the "/etc/aliases" file. The problem I was running into was that the python scripts that were available assumed that you could "walk" through the parts of the email and that wasn't working with the emails I had. This script takes the incoming email as a string and uses regex to parse through relevant sections and then saves them to a file. You will have to customize it based on your needs but it should be able to parse csv and pdf files out of the box.