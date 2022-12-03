from D17_data import question_data
from D17_question_model import Question
from D17_quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()
# print(question_bank)
# print(question_bank[0].text, question_bank[0].answer)
# print(question_bank[1].text, question_bank[1].answer)
# print(question_bank[2].text, question_bank[2].answer)
