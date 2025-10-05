# quiz 3 put questions and answers into a dictionary
# name: Chloe Cornforth
# date: 10/03/2025

#quiz questions. for each question, list possible answers and the correct answer
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles per hour?": ["12", "24", "36", "48"],
    "What is the capital of Texas?": ["Austin", "Dallas", "Houston", "Waco"],
    "The last supper was a famous painting by which artist?": ["Da Vinci", "Michelangelo", "Raphael"]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"- {alternative}")
    
    answer = input(f"{question}: ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")