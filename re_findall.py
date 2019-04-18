import re
# print(re.finditer(r'\w','http://www.hackerrank.com/'))
# #<callable-iterator object at 0x0266C790>
# print(list(map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))))
# #['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

#?= lookahead assertion
list=re.findall(r'(?=([^aeiou][aeiou]{2,}[^aeiou]))',input(),re.I)
# print(list)

if len(list)==0:
    print('-1')
else:
    for item in list:
        print(item[1:len(item)-1])