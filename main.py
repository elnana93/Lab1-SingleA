# Original main.py created by Elnana.93
# Modified to optimize functionality: integrate exisiting cose with custom module(s)
#
# Original Code:
# print("hello class")

# def say_hello():
#     return "hello"

# result = say_hello()
# print(result)

#importing my zodia program module
from zodia import zodiac_main

def say_hello():
    return "\n\nhello"

def main():
    while True:
        result = say_hello()
        print(result)

        choice = input("\nWould you like to play the Zodiac Game? [Y|N]: ")

        if choice in ('N', 'n'):
            print("Existing... Goodbye, Dusty!!!")
            break

        if choice in ('Y', 'y'):
           zodiac_main()
        else:
            print("Invalid Choice, you Dusty!!!. Please type Y or N")
    
main()
