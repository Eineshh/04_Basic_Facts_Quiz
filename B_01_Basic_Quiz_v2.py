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


# displays the instructions
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

    # checks if the number is an integer
    elif low is not None and high is None:
        error = f"Please enter an integer that is more than / equal to {low}"
        print()

    # checks if the number is between a high and low number
    else:
        error = f"Please enter an integer that is between {low} and {high} (inclusive)"
        print()

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks if the integer is higher than the lower number
            if low is not None and response < low:
                print(error)

            # checks if the integer is lower than the higher number
            elif high is not None and response > high:
                print(error)

            # returns response
            else:
                return response

        except ValueError:
            print(error)


# displays the users questions
def quiz_questions():

    # initialize the variables
    question_won = 0
    question_lost = 0
    num_questions = 0
    quiz_history = []

    # asks user the desired difficulty of the questions
    difficulty = int_check("Choose the difficulty (1 -Easy, 2 -Medium, 3 -Hard): ", low=1, high=3)

    # loops the question 
    while True:
        print()
        print(f"⭐ Question {num_questions + 1} ⭐: ")

        if difficulty == 3:
            num_1 = random.randint(1, 30)
            num_2 = random.randint(1, 30)
        elif difficulty == 2:
            num_1 = random.randint(1, 20)
            num_2 = random.randint(1, 20)
        else:
            num_1 = random.randint(1, 10)
            num_2 = random.randint(1, 10)

        math_operations = ["addition", "subtraction", "multiplication", "division"]
        operation = random.choice(math_operations)

        if operation == "subtraction":
            num_1 = num_1 + num_2
            question = f"What's {num_1} - {num_2}?: "
            answer = num_1 - num_2
        elif operation == "addition":
            question = f"What's {num_1} + {num_2}?: "
            answer = num_1 + num_2
        elif operation == "multiplication":
            question = f"What's {num_1} x {num_2}?: "
            answer = num_1 * num_2
        else:
            num_1 = num_1 * num_2
            question = f"What's {num_1} ÷ {num_2}?: "
            answer = num_1 // num_2

        users_answer = int_check(question, low=1)
        answer = int(answer)

        if users_answer == "xxx":
            print("You chickened out of the quiz!")
            print()
            break

        elif users_answer == answer:
            question_won += 1
            feedback = f"You got the answer right, it was {answer}"
            question_history = f"Question {num_questions + 1}: You got the answer right, it was {answer} ✅."

        else:
            question_lost += 1
            feedback = f"You got the answer wrong, it was {answer}"
            question_history = f"Question {num_questions + 1}: You got the answer wrong, it was {answer} ❌."

        quiz_history.append(question_history)
        print(feedback)
        num_questions += 1

    if num_questions == 0:
        print("Sorry you haven't answered the quiz")
        return

    quiz_stats = yes_no("Do you want to view the stats? ")
    if quiz_stats == "yes":
        question_correct = question_won / num_questions * 100
        question_wrong = question_lost / num_questions * 100
        print(f"Out of {num_questions} questions:")
        print(f"- {question_correct:.2f}% of questions correct")
        print(f"- {question_wrong:.2f}% of questions wrong")

    see_history = yes_no("Would you like to view the quiz history?: ")
    if see_history == "yes":
        print("\n💫💫 Quiz History 💫💫")
        for item in quiz_history:
            print(item)


print("✨ Basic Facts Quiz ✨")

print()
want_instructions = yes_no("Would you like to read the instructions?: ")
if want_instructions == "yes":
    instruction()

desired_questions = int_check("How many questions would you like?: ", low=1, exit_code="xxx")
if desired_questions == "xxx":
    print("Sorry you have not answered a single question, thus there is no history or statistics to show.")
else:
    quiz_questions()
