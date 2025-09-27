list_of_lists = [[], [9,10,11], [12,13,14,15,16], [17,18,19,20,21,22,23,24,25]]
print(list_of_lists)

length = len(list_of_lists)

list_number = int(input("Enter a list number (0-3): "))
list_of_lists = list_of_lists[list_number]

if length < 5:
    print(f"user enter {list_number}: short list")
elif 5 <= length <= 10:
    print(f"user enter {list_number}: medium list")
else:
    print(f"user enter {list_number}: long list")
