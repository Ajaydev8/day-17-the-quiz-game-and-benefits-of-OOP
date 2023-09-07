class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self, q_list):
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            user_answer = input(f"{current_question.text} (TRUE/FALSE)?: ").title()
            self.question_number += 1


