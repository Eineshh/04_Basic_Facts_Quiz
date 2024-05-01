# checks users have entered yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes or No")


# displays instructions
def instruction():
    print('''
✦✦✦ Instructions ✦✦✦

first off choose the desired rounds

answer question

:)
    ''')


# Main routine
print("✨ Area and Perimeter Quiz ✨")

# loop for testing purposes
print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
