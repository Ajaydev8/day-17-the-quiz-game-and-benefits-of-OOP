from data import question_data
from question_model import Question

question_bank = []

for key in question_data:
    question = key["text"]
    answer = key["answer"]
    new_q = Question(q_text=question, q_answer=answer)
    question_bank.append(new_q)
print(question_bank[0].text)

