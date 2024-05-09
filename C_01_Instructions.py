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
            print("Please enter Yes or No!")


# displays instructions
def instruction():
    print('''
✦✦✦ Instructions ✦✦✦

Welcome to the Basic Facts Quiz!

To begin with, choose the desired rounds or press <enter>
for endless questions,

(You may choose to end the round by entering <xxx>),

Next, choose the game difficult (Easy, Medium & Hard) as it will determine
the complexity of your question!,

Your goal is to answer the question correctly within 
the three attempts given,

At the end of the game, your quiz statistics are displayed with
the option of viewing the quiz history,

Have Fun! :)
    ''')


# Main routine
print("✨ Basic Facts Quiz ✨")

# loop for testing purposes
print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
