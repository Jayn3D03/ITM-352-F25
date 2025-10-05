# quiz 4 allow the user to slect the correct answer by its label
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
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives, 1):
        print(f"{label}. {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label - 1]
    
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")