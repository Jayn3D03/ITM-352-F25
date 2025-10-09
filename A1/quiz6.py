# quiz 6 allow the user to select the correct answer by its label
# improve look and usability
# keep track of correct answers
# loop until user provides valid input
# randomize the order of the answers and questions
# name: Chloe Cornforth
# date: 10/08/2025

from string import ascii_lowercase
import random

#quiz questions. for each question, list possible answers and the correct answer
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles per hour?": ["12", "13", "24", "36", "48"],
    "What is the capital of Texas?": ["Austin", "Dallas", "Houston", "Waco"],
    "The last supper was a famous painting by which artist?": ["Da Vinci", "Michelangelo", "Raphael"],
    "Which classic novel opens with the line 'Call me Ishmael'?": ["Moby Dick", "Pride and Prejudice", "1984", "To Kill a Mockingbird"]
}

number_correct = 0
NUM_QUESTIONS_PER_QUIZ = 5
num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
# randomly select questions for the quiz
questions = random.sample(list(QUESTIONS.items()), num_questions)

for num, (question, alternatives) in enumerate(questions, 1):
    print(f"\nQuestion {num}:")
    print(f"{question}")

    correct_answer = alternatives[0]
    labelled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, len(alternatives))))
    for label, alternative in labelled_alternatives.items():
        print(f"{label}. {alternative}")

# loop until user provides valid answer
    while (answer_label := input("\nChoice: ")) not in labelled_alternatives:
        print(f"Please answer one of {', '.join(labelled_alternatives)}")
    answer = labelled_alternatives.get(answer_label)
    
    if answer == correct_answer:
        print("* Correct! *")
        number_correct += 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}):")

print(f"\nYou got {number_correct} out of {len(questions)} questions correct.")