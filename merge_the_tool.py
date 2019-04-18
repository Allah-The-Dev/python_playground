def merge_the_tools(string, k):
    for i in range(0,len(string),3):
        list_of_char=list(string[i:i+3])
        #removing duplicate keys from a list
        #using dictionary keys
        string_to_print=''.join(list(dict.fromkeys(list_of_char)))
        print(dict.fromkeys(list_of_char))   
        print(string_to_print)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)