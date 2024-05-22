# Checks if the user has entered yes (Y) or no (N)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"

        elif response in ["no", "n"]:
            return "no"

        else:
            print("Please enter Yes or No!")
            print()