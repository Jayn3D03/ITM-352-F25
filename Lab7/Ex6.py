data = ["hello", 10, "goodbye", 3, "good night", "good morning"]
try:
    data.append(input("Enter something to add to the list: "))
except Exception as e:
    print(f"An error occurred: {e}")

for item in data:
    if type(item) == str:
        string_count += 1
print(f"There are {string_count} strings in the data list.")