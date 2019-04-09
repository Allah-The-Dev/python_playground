import math

num_of_rows,num_of_char_in_row = tuple(map(int,input().split()))

string_center = ".|."
temp_no = 1                             #variable to tell no of special string

for num in range(num_of_rows):

    if num < int(num_of_rows/2):        #top
        num_of_spl_char = temp_no*3
        num_of_dash = int(math.floor(((num_of_char_in_row)-(num_of_spl_char))/2))
        string_out = num_of_dash*'-'+int((num_of_spl_char/3))*string_center+num_of_dash*'-'
        temp_no+=2
        print(string_out)

    elif num == int(num_of_rows/2):    #center
        num_of_dash = int((num_of_char_in_row-len('welcome'))/2)
        string_out = num_of_dash*'-'+'WELCOME'+num_of_dash*'-'
        print(string_out)
        temp_no-=2

    elif num > int(num_of_rows/2):     #bottom
        num_of_spl_char = temp_no*3
        num_of_dash = int(math.floor(((num_of_char_in_row)-(num_of_spl_char))/2))
        string_out = num_of_dash*'-'+int((num_of_spl_char/3))*string_center+num_of_dash*'-'
        temp_no-=2
        print(string_out)