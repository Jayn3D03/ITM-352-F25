data = ("hello", 10, "goodbye", 3, "good night", "good morning")  # tuple, not list

try:
    data.append(input("Enter something to add to the tuple: "))
except Exception:
    user_input = input("Enter something to add to the tuple: ")
    data_list = list(data)
    data_list.append(user_input)
    data = tuple(data_list)

print("Appended tuple:", data)