def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    l=[]
    for i in range(n):
        s = '-'.join(alpha[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3,'-'))
    # b=reversed(l[1:])  #this also works
    # print("\n".join(b), "\n".join(l), sep = "\n") #this also works
    print('\n'.join(l[::-1]+l))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)