# quiz 7 allow the user to select the correct answer by its label
# include answer options
# allow user to select correst answer by its label
# improve look and usability
# keep track of correct answers
# loop until user provides valid input
# randomize the order of the answers and questions
# refactor to use functions
# read quiz questions from a json file
# name: Chloe Cornforth
# date: 10/08/2025

from string import ascii_lowercase
import random
import json

#quiz questions. for each question, list possible answers and the correct answer
question_file = open('questions.json')
QUESTIONS = json.load(question_file)
question_file.close()

# prepare the questions for the quiz
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    # randomly select questions for the quiz
    return random.sample(list(questions.items()), num_questions)

# get an answer from the user ensuring it is valid
def get_answer(question, info):
    print(f"\n{question}")
    # Randomize options here
    labelled_alternatives = dict(zip(
        ascii_lowercase,
        random.sample(info["options"], len(info["options"]))
    ))
    for label, alternative in labelled_alternatives.items():
        print(f"{label}. {alternative}")

    # loop until user provides valid answer
    while (answer_label := input("\nChoice: ")) not in labelled_alternatives:
        print(f"Please answer one of {', '.join(labelled_alternatives)}")
    return labelled_alternatives.get(answer_label)

# ask the question and return 1 if correct, 0 if not, write out answers and explanations
def ask_questions(question, info):
    correct_answer = info["answer"]
    answer = get_answer(question, info)
    if answer == correct_answer:
        print("* Correct! *")
        print("Explanation:", info.get("explanation", ""))
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}:")
        print("Explanation:", info.get("explanation", ""))
        return 0

number_correct = 0
NUM_QUESTIONS_PER_QUIZ = 10

# main quiz loop
questions = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)
for num, (question, info) in enumerate(questions, 1):
    print(f"\nQuestion {num}:")
    number_correct += ask_questions(question, info)

# writes out final score
print(f"\nYou got {number_correct} out of {len(questions)} questions correct.")

import json
import os

file_name = "score_history.json"

# makes sure the file exists and loads existing scores
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        score_history = json.load(file)
else:
    score_history = []

# append the new score
score_history.append({
    "score": number_correct,
    "total": len(questions)
})

# write score to the file
file = open(file_name, "w")
json.dump(score_history, file, indent=2)
file.close()