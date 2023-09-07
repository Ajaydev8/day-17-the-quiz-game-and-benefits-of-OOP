class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list


    def next_question(self, q_list):
        for question in q_list:
            q_list[self.question_number].text = question
            new_question = input(f"{question} (TRUE/FALSE)?: ")
            self.question_number += 1



