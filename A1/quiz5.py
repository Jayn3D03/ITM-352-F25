# quiz 5 allow the user to slect the correct answer by its label
#improve look and usuability
#keep track of correct answers
# look until user provides valid input
# name: Chloe Cornforth
# date: 10/03/2025

from string import ascii_lowercase

#quiz questions. for each question, list possible answers and the correct answer
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles per hour?": ["12", "24", "36", "48"],
    "What is the capital of Texas?": ["Austin", "Dallas", "Houston", "Waco"],
    "The last supper was a famous painting by which artist?": ["Da Vinci", "Michelangelo", "Raphael"]
}

number_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), 1):
    print(f"\nQuestion {num}:")
    print(f"{question}")

    correct_answer = alternatives[0]
    labelled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labelled_alternatives.items():
        print(f"{label}. {alternative}")

    answer_label = input("\nChoice: ")
    answer = labelled_alternatives.get(answer_label)
    
    if answer == correct_answer:
        print("Correct!")
        number_correct += 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")

print(f"\nYou got {number_correct} out of {len(QUESTIONS)} questions correct.")