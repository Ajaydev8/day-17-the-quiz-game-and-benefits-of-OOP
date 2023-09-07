from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    question = key["text"]
    answer = key["answer"]
    new_q = Question(q_text=question, q_answer=answer)
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)

new_question = quiz_brain.next_question(question_bank)
print(new_question)
