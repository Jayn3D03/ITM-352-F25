celebrities_tuple = ("Taylor Swift", "Lionel Messi", "Max Verstappen", "Keanu Reeves", "Angelina Jolie")
age_tuple = (34, 36, 26, 60, 48)
#celebrities_list = []
#age_list = []

#for celeb in celebrities_tuple:
    #celebrities_list.append(celeb)

celebrities_list = [celeb for celeb in celebrities_tuple]

#for age in age_tuple:
    #age_list.append(age)

age_list = [age for age in age_tuple]

celebrities_dictionary = {
    "celebrities": celebrities_list,
    "ages": age_list
}
print(celebrities_dictionary)