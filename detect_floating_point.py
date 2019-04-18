import re

no_of_test_cases=int(input())
list_of_test_cases=[input() for _ in range(no_of_test_cases)]

for string in list_of_test_cases:
    pattern=r'^[+-]?\d*\.\d+$'
    list_1=re.match(pattern,string)
    print(bool(list_1))
    