no_of_stamp=int(input())
set_of_countries=set()
for _ in range(no_of_stamp):
    set_of_countries.add(input().lower())
print(len(set_of_countries))