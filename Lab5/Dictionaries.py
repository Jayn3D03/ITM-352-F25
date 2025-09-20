# create new dictionary

country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London",
}
print(country_capitals)

print(country_capitals["Germany"])
print(country_capitals.get("England"))

country_capitals["Italy"] = "Rome"
print(country_capitals)

#del country_capitals["Germany"]
#print(country_capitals)

#country_capitals.clear()
#print(country_capitals)

country_capitals["Italy"] = "Milan"
print(country_capitals)
print(len(country_capitals))

print("France" not in country_capitals)