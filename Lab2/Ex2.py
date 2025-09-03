#Ask the user their birth year and calculate their age by subtracting from the current year
#Name: Chloe Cornforth
#Date: 09/03/2025

birth_year = input("Please enter your birth year as a four didgit number: ")
#need to check that they really entered an integer
birth_year_int = int(birth_year)

#this should be changed to extract the year automatically from the current date
current_year = 2025

#this doesn't take into account the day and month. need to fix
age = current_year - birth_year_int
print("Your entered", birth_year)
print("Your age is", age)
