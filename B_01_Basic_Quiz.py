import random


# checks users have entered yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks the users response
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

To begin with, choose the desired questions or press <enter>
for endless questions,

(You may choose to end the quiz by entering <xxx>),

Next, choose the quiz difficult (Easy, Medium & Hard) as it will determine
the complexity of your question!,

Your goal is to answer the question correctly within 
the three attempts given,

At the end of the quiz, your statistics are displayed with
the option of viewing the history too,

Have Fun! :) ''')


# Check that users have entered a valid integer
def int_check(question, low=None, high=None, exit_code="xxx"):
    # sets up an error message
    if low is None and high is None:
        error = "Please enter an integer"
        print()

    # if the number needs to be more than an
    # integer (ie: rounds / high number)
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
        print()

    # if the number needs to be between a low and a high
    else:
        error = (f"Please enter and integer that"
                 f"is between {low} and {high} (inclusive)")
        print()

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks that the integer is not lower than the low num
            if low is not None and response < low:
                print(error)

            # checks that the integer is not higher than the high num
            elif high is not None and response > high:
                print(error)

            # returns the response if the response entered meets the criteria
            else:
                return response

        except ValueError:
            print(error)


# displays the users questions
def quiz_questions():

    # Initializes variables
    num_questions = 0
    question_won = 0
    question_lost = 0
    quiz_history = []

    # asks the user how hard they would like the quiz to be
    difficulty = int_check("Choose the difficulty, (1 -Easy, 3 -Hard): ",
                           low=1, high=3)

    # loops while num_questions is lower than amount of questions - chosen at the start
    while num_questions < desired_questions:

        print()
        print(f"⭐ Question {num_questions + 1} ⭐: ")

        # Generates the numbers for the question and difficulty
        if difficulty == 3:
            num_1 = random.randint(1, 30)
            num_2 = random.randint(1, 30)
        elif difficulty == 2:
            num_1 = random.randint(1, 20)
            num_2 = random.randint(1, 20)
        else:
            num_1 = random.randint(1, 10)
            num_2 = random.randint(1, 10)

        # Displays the operation involved
        math_operation = ["addition", "subtraction", "multiplication", "division"]

        # generates the question type
        question_type = random.choice(math_operation)

        # generates the question format
        if math_operation == "subtraction":
            num_1 = num_1 + num_2
            question_format = f"What's {num_1} - {num_2}?: "
            answer = num_1 - num_2

        elif question_type == "addition":
            question_format = f"What is {num_1} + {num_2}?: "
            answer = num_1 + num_2

        elif question_type == "multiplication":
            question_format = f"What is {num_1} x {num_2}?: "
            answer = num_1 * num_2

        else:
            # makes sure that the number being divided is always going to result in a whole number
            num_1 = num_1 * num_2
            question_format = f"What is {num_1} divided by {num_2}?: "
            answer = num_1 / num_2

        # The user gets to ask the question
        users_answer = int_check(question_format, low=1)

        # makes the answer an integer
        answer = int(answer)

        # if the user types the exit code they are able to leave the game
        if users_answer == "xxx":
            print("Thanks for playing  quiz!")
            print()
            break

        # sets correct to yes if the answer is correct
        elif users_answer == answer:
            question_won += 1
            feedback = f"You got the answer right, it was {answer}"
            question_history = f"Question {num_questions + 1}: You got the answer right, it was {answer} ✅."

        # sets correct to no
        else:
            question_lost += 1
            feedback = f"You got the answer wrong, it was {answer}"
            question_history = f"Question {num_questions + 1}: You got the answer wrong, it was {answer} ❌."

        # adds the round result into a list
        quiz_history.append(question_history)

        # prints the feedback/result of the round
        print(feedback)

        num_questions += 1

    # if the user doesn't answer a single question it doesn't display stats/quiz_history
    if num_questions == 0:
        print("Sorry you have not answered a single question thus there is no quiz_history"
              "or statistics we can show you.")
        exit()

    # asks the user whether they would want to see the game quiz_history
    quiz_history = yes_no("Do you want to view the game quiz_history?")
    print()

    # displays the game quiz_history if the user wants to see it
    if quiz_history == "yes":
        print("\n⌛⌛⌛ Quiz History ⌛⌛⌛ ")
        print()
        # Outputs the game quiz_history
        for item in quiz_history:
            print(item)

    # Asks the user if they want to view the game stats
    print()
    quiz_stats = yes_no("Do you want to view the stats? ")
    print()

    # If yes, displays the game stats
    if quiz_stats == "yes":
        # Calculates the win percentage
        question_correct = question_won / num_questions * 100

        # Calculates loss percentage:
        question_wrong = question_lost / num_questions * 100

        print(f"Out of {num_questions} questions:")
        print()
        print(f"- {question_correct:.2f}% of questions correct")
        print()
        print(f"- {question_wrong:.2f}% of questions wrong")
        print()


# Main routine

# Displays the title
print("✨ Basic Facts Quiz ✨")


# loop for testing purposes
print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# displays instructions
if want_instructions == "yes":
    instruction()

# asks the user how many questions they want
desired_questions = int_check("How many questions would you like?: ", low=1, exit_code="xxx")

if desired_questions == "xxx":
    print("Sorry you have not answered a single question thus there is no history"
          "or statistics we can show you.")
    exit()

# Starts the quiz
quiz_questions()
