from quizgame.game import QuizGame
from quizgame.questions import QuizQuestion
from random import shuffle

def show_menu():
    print("Menu:")
    print("1. Start a New Quiz")
    print("2. View Instructions")
    print("3. Exit")

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
            game.start_game(questions)
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
