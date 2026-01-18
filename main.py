# Original main.py created by Elnana.93
# Original main.py just printed hello once
# Need to refactor it so that I can run different modules
#
# ORIGINAL CODE:
# print("hello class")
#
# def say_hello():
#     return "hello"
#
# result = say_hello()
# print(result)
# (Output would be)
# hello class
# hello

import random
from calculator import run_calculator  # my refactored calculator module


# kept the original function, but now used through the menu system
def say_hello():
    return "hello"


# Joey's math game feature, refactored to be called from the menu
def math_game():
    score = 0
    print("\n--- Welcome to the Addition Challenge! ---")
    print("Type 'exit' to quit the game.")

    while True:
        # 1. The computer picks two secret numbers
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        correct_answer = num1 + num2

        # 2. The computer asks you the question
        user_input = input(f"\nWhat is {num1} + {num2}? ")

        # 3. If you type 'exit', the game stops
        if user_input.lower() == 'exit':
            print(f"\nGame Over! Your final score: {score}")
            break

        # 4. The computer checks if you are right
        try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                score += 1
                print(f"Correct! 🎉 Score: {score}")
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            # This happens if you type letters instead of a number
            print("Please enter a number or type 'exit'!")


# Your name/number “fun message” wrapped into a function
def fun_message():
    name = input("Enter your name: ")
    try:
        number = int(input("Enter your favorite number: "))
    except ValueError:
        print("That wasn't a number, going back to menu.")
        return

    # Create a playful message using string multiplication and formatting
    message = f"Hello {name}! " + ("🎉" * number)

    # Display the result
    print(message)


# refactored version of main.py using a menu instead of auto-execution
def main_menu():
    print("hello class")  # same initial behavior as the original

    while True:
        print("\n=== Main Menu ===")
        print("1. Say hello (original behavior)")
        print("2. Open calculator (old high school code)")
        print("3. Play Joey's math game")
        print("4. Fun message")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            # original logic now happens here
            result = say_hello()
            print(result)

        elif choice == "2":
            # new modular feature
            run_calculator()

        elif choice == "3":
            math_game()

        elif choice == "4":
            fun_message()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


# Python standard entry point
if __name__ == "__main__":
    main_menu()
