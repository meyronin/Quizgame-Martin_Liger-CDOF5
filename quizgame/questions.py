# quizgame/questions.py
class QuizQuestion:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_option.lower()