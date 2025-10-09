# quiz 7 allow the user to select the correct answer by its label
# include answer options
# allow user to select correst answer by its label
# improve look and usability
# keep track of correct answers
# loop until user provides valid input
# randomize the order of the answers and questions
# refactor to use functions
# name: Chloe Cornforth
# date: 10/08/2025

from string import ascii_lowercase
import random

#quiz questions. for each question, list possible answers and the correct answer
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12", "13", "24", "36", "48"],
    "What is the capital of Texas": ["Austin", "Dallas", "Houston", "Waco"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"],
    "Which class novel opens with the line 'Call Me Ishmael'": ["Moby Dick", "The Great Gatsby", "1984", "To Kill a Mockingbird"]
}

# prepare the questions for the quiz
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    # Randomly select a subset of questions for the quiz
    return random.sample(list(questions.items()), num_questions)

# get an answer from the user ensuring it is valid
def get_answer(question, alternatives):
    print(f"\n{question}")
    labelled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, len(alternatives))))
    for label, alternative in labelled_alternatives.items():
        print(f"{label}. {alternative}")

# loop until user provides valid answer
    while (answer_label := input("\nChoice: ")) not in labelled_alternatives:
        print(f"Please answer one of {', '.join(labelled_alternatives)}")
    return labelled_alternatives.get(answer_label)

def ask_questions(questions, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, len(alternatives))
    answer = get_answer(question, ordered_alternatives)

    if answer == correct_answer:
        print("* Correct! *")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

number_correct = 0
NUM_QUESTIONS_PER_QUIZ = 5

# main quiz look
questions = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)
for num, (question, alternatives) in enumerate(questions, 1):
    print(f"\nQuestion {num}:")
    number_correct += ask_questions(question, alternatives)

    
print(f"\nYou got {number_correct} out of {len(questions)} questions correct.")