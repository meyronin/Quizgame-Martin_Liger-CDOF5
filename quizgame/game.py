# quizgame/game.py
class QuizGame:
    def __init__(self):
        self.score = 0

    def ask_question(self, question):
        print(question.question)
        user_answer = input("Your answer: ")
        if question.check_answer(user_answer):
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer was:", question.correct_option)

    def start_game(self, questions):
        print("Welcome to the Quiz Game!")
        for question in questions:
            self.ask_question(question)
        print("Game Over! Your final score is:", self.score)