def print_formatted(number):
    # your code goes here
    
    max_width = len(str(bin(number))[2:])

    for i in range(1,number+1):
        print(f'{i:{max_width}d} {i:{max_width}o} {i:{max_width}X} {i:{max_width}b}')   

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# print(len("   17    21    11 10001")) 
# print(len("   17    21    11 10001"))
# 
#    
# n = int(input())
# width = len(f"{n:b}")
# for i in range(1,n+1):
#     print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
