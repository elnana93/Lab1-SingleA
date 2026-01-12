def get_zodiac_sign(day, month):
    # Convert month to lowercase to handle different input styles
    month = month.lower()

    if month in ('december', 'dec'):
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month in ('january', 'jan'):
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month in ('february', 'feb'):
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month in ('march', 'mar'):
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month in ('april', 'apr'):
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'may':
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month in ('june','jun'):
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month in ('july', 'jul'):
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month in ('august', 'aug'):
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month in ('september', 'sep'):
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month in ('october', 'oct'):
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month in ('november', 'nov'):
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    else:
        return "Invalid month entered."
    
    return astro_sign


# --- Main Program ---
def menu():
    print("\n\n***** ZODIAC SIGN FINDER *****")
    print("\nSelect from the menu below:")
    print("   1. Find Zodiac Sign")
    print("   2. Quit")

while True:
    menu()
    choice = input("Enter choice (1 or 2): ")

    if choice == '2':
        print("Existing... Goodbye, Dusty!!!")
        break

    if choice == '1':
        try:
            user_month = input("Enter your birth month (e.g., March or Mar): ").strip()
            user_day = int(input("Enter your birth day (e.g., 25): "))

            sign = get_zodiac_sign(user_day, user_month)
            print(f"\nYour Zodiac sign is: **{sign}**")
        except ValueError:
            print("Please enter a valid number for the day.")
            continue
    else:
        print("Invalid Choice, you Dusty!!!. Please pick 1 or 2")
