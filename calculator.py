# calculator.py

# This calculator code is based on an old high school assignment I had.
# The original version used 'from art import logo' to show an ASCII banner,
# but I removed that dependency so it runs without installing anything extra.
# I refactored it to be modular and usable through main.py via run_calculator().


# basic math functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    # original assignment didn't handle divide-by-zero, so I added this check
    if n2 == 0:
        print("Error: you can't divide by zero.")
        return None
    return n1 / n2


# dictionary mapping symbols to functions (same approach as the original assignment)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# refactored function to make the calculator reusable from main.py
def run_calculator():
    print("\n=== Calculator ===")  # replaces the old ASCII logo

    # get first number
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid number, try again.")
        return

    should_continue = True

    while should_continue:
        # show available operators
        print("Pick an operation:")
        for symbol in operations:
            print(symbol)

        op = input("Operation: ").strip()

        # validate operator
        if op not in operations:
            print("Invalid operation, try again.")
            continue

        # get second number
        try:
            num2 = float(input("Enter next number: "))
        except ValueError:
            print("Invalid number, try again.")
            continue

        # perform calculation
        result = operations[op](num1, num2)

        # handle divide-by-zero result
        if result is None:
            continue

        print(f"{num1} {op} {num2} = {result}")

        # from the original assignment logic (slightly improved)
        next_step = input(
            f"Type 'y' to keep going with {result}, 'n' for new calc, or 's' to stop: "
        ).lower()

        if next_step == "y":
            num1 = result
        elif next_step == "n":
            # equivalent to restarting calculator()
            should_continue = False
            run_calculator()
        else:
            print("Returning to main menu...")
            should_continue = False



