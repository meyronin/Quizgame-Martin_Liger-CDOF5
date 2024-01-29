from quizgame.game import QuizGame
from quizgame.questions import QuizQuestion
from random import shuffle

if __name__ == "__main__":
    game = QuizGame()
    questions = [
        QuizQuestion("What is 2 + 2?", ["a) 3", "b) 4", "c) 5"], "b"),
        QuizQuestion("What is the capital of France?", ["a) London", "b) Paris", "c) Berlin"], "b"),
    ]
    shuffle(questions)
    game.start_game(questions)
