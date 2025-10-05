# quiz 2 put answers into a list
# name: Chloe Cornforth
# date: 10/03/2025

QUESTIONS = [
    { "What is the airspeed of an unladen swallow in miles per hour?": "12" },
    { "What is the capital of Texas?": "Austin" },
    { "The last supper was a famous painting by which artist?": "Da Vinci" }
]

for question, correct_answer in QUESTIONS():
    answer = input(f"{question}: ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")