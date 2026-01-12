import random

def math_game():
    score = 0
    print("--- Welcome to the Addition Challenge! ---")
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

if __name__ == "__main__":
    math_game()