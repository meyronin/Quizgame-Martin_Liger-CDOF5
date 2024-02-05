from quizgame.game import QuizGame
from quizgame.questions import QuizQuestion
from random import shuffle
import threading

def show_menu():
    print("Menu:")
    print("1. Start a New Quiz")
    print("2. View Instructions")
    print("3. Exit")

def answer_question(question, time_limit=10):
    print(question.prompt)
    for option in question.options:
        print(option)
    
    answer = None
    timer = threading.Timer(time_limit, print, ["Time's up!"])
    try:
        timer.start()
        answer = input(f"Answer within {time_limit} seconds: ")
    finally:
        timer.cancel()
    
    return answer == question.answer

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            game = QuizGame()
            questions = [
                QuizQuestion("What is 2 + 2?", ["a) 3", "b) 4", "c) 5"], "b"),
                QuizQuestion("What is the capital of France?", ["a) London", "b) Paris", "c) Berlin"], "b"),
            ]
            shuffle(questions)
            
            for question in questions:
                if not answer_question(question):
                    print("Incorrect or no answer provided in time.")
                else:
                    print("Correct!")
            
            game.end_game()

        elif choice == "2":
            print("Instructions:")
            print("Answer the questions to the best of your ability.")
            print("Each correct answer earns you a point.")
            print("Have fun!\n")
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
