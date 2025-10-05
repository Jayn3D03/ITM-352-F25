data = ("hello", 10, "goodbye", 3, "good night", "good morning")  # tuple, not list

try:
    data.append(input("Enter something to add to the tuple: "))
except Exception:
    user_input = input("Enter something to add to the tuple: ")
    data = (*data, user_input)

print("Appended tuple:", data)