#Create a script that converts all items of the range to strings
my_range = range(1, 21)
map_obj = map(str, my_range)
str_list = []

for i in map_obj:
    # print(i, type(i))
    str_list.append(i)
print(list(my_range))
print(list(str_list))
