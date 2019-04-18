# S, N = input(), int(input()) 
# for part in zip(*[iter(S)] * N):
#     d = dict()
#     print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

for part in zip(*[iter('abcdefghijkl')]*4):
	print(part)

#equivalent to 
s = 'abcdefghijkl'
it = iter(s)
for part in zip(it, it, it,it):
    print(part)


print(zip(*[iter('abcdefghijkl')]*4))
#amazing concept
#first 4 times the same iterator
#then getting one item from each iterator

#like
it1,it2,it3,it4=tuple([iter('abcdefghijkl')]*4)
# for item in it1:
#     print('it1:',item)
# for item in it2:
#     print('it2:',item)
# for item in it3:
#     print('it3:',item)
# for item in it4:
# #     print('it4:',item)
# print(it1)
# print(it1.next())
# print(it2)
# print(it2.next())
# print(it3)
# print(it3.next())
# print(it4)
# print(it4.next())