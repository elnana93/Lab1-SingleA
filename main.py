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

from calculator import run_calculator  # my refactored calculator module

# kept the original function, but now used through the menu system
def say_hello():
    return "hello"

# refactored version of main.py using a menu instead of auto-execution
def main_menu():
    print("hello class")  # same initial behavior as the original

    while True:
        print("\n=== Main Menu ===")
        print("1. Say hello (original behavior)")
        print("2. Open calculator (old high school code)")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            # original logic now happens here
            result = say_hello()
            print(result)

        elif choice == "2":
            # new modular feature
            run_calculator()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

# Python standard entry point
if __name__ == "__main__":
    main_menu()

name = input("Enter your name: ")
number = int(input("Enter your favorite number: "))

# Create a playful message using string multiplication and formatting
message = f"Hello {name}! " + ("🎉" * number)

# Display the result
print(message)

    