class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.total = len(q_list)

    def next_question(self, q_list):
        is_on = True
        while is_on:
            if self.question_number < len(self.question_list):
                current_question = self.question_list[self.question_number]
                user_answer = input(f"{current_question.text} (TRUE/FALSE)?: ").title()
                if current_question.answer == user_answer:
                    self.question_number += 1
                    self.score += 1
                    print("you got it right!")
                    print(f"The correct answer was {current_question.answer}")
                    print(f"Your current score is {self.score}/{self.total}")
                elif current_question.answer != user_answer:
                    self.question_number += 1
                    print("you got it Wrong!")
                    print(f"The correct answer was {current_question.answer}")
                    print(f"Your current score is {self.score}/{self.total}")
            else:
                print(f"Your final score is {self.score}/{self.total}")
                is_on = False


