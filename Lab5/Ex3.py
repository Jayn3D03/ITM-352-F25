# define a list of survey responses values
survey_responses = (5, 7, 3, 8)

# define a tuple of survey respondant IDs
survey_ids = (1012, 1035, 1021, 1052)

# create a dictionary by zipping together the list and tuple
# IDs as keys and responses as values
survey_dict = dict(zip(survey_ids, survey_responses))
print("survey response values", survey_responses)
print("survey respondant IDs", survey_ids)
print("survey dictionary", survey_dict)

print(f"the respondent {survey_ids[2]} gave a response of {survey_dict[survey_ids[2]]}")