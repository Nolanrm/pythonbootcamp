class Quiz:
    def __init__(self,q_list):
        self.question_number = 0
        self.correct_answers = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        else:
            return True


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number} {current_question.text} (true/false): ').lower()

        if answer == current_question.answer.lower():
            self.correct_answers += 1
            print(f'Correct! \nTotal Current Score: {self.correct_answers}/{self.question_number}')
        else:
            print(f'Incorrect! \nTotal Current Score: {self.correct_answers}/{self.question_number}')


