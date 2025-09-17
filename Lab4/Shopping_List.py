#start w/ an empty list
shopping_list = []
shopping_list.append("apples")
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.insert(0, "eggs") #insert eggs at index 0
print(shopping_list)

shopping_list.pop()
print("aftter removing last item:" , shopping_list)