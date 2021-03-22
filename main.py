from data import questions
from quiz import Question
from quiz import Quiz

question_bank = []
for question in questions:
    new_question = question['question']
    new_answer = question['correct_answer']
    current_question = Question(new_question, new_answer)
    question_bank.append(current_question)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")