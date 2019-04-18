import re

#---------------------------------
#groupdict() 
# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# print(m.groupdict())
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
#----------------------------------

#in the below statement (.*?) will do the not greedy search
match=re.match(r'(.*?)([a-zA-Z0-9])\2',input())
if match == None:
    print('-1')
else:
    print(match.group(2)[0])