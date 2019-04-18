n = int(input())
s = set(map(int, input().split()))

no_of_commands=int(input())

commands =[input() for _ in range(no_of_commands)]

for command in commands:
    if command[0]=='p':
        s.pop()
    elif command[0]=='r':
        s.remove(int(command.split()[1]))
    elif command[0]=='d':
        s.discard(int(command.split()[1]))

sum_of_set_no=0
for item in s:
    sum_of_set_no+=item
print(sum_of_set_no)