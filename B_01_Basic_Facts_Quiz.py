# Allows for random numbers to be generated
import random


# Function to check if the user has entered yes (Y) or no (N)
def yes_no(question):
    # Loops until the user has entered a valid response
    while True:
        # Get the user's response and converts it to a lowercase response
        response = input(question).lower()
        # Check if the response entered is either "Yes" or "Y"
        if response in ["yes", "y"]:
            return "yes"
        # Check if the response entered is either "No" or "N"
        elif response in ["no", "n"]:
            return "no"
        # Print's an error message is a valid response was not entered
        else:
            print("Please Enter Yes or No!")
            print()


# Function to display the instructions
def instructions():
    print('''
🌟🌟 Instructions 🌟🌟

Hello.. Welcome to my quiz! 😊, it seems like it's your first time playing...

📌 The objective of this quiz is to test your knowledge of basic math equations,

📌 This quiz will contain math operations such as multiplication, division, addition, and subtraction,

🎗️ ️To begin with, choose the desired number of questions or press <enter> for 
   ️endless questions,

🎗️ Next, choose the difficulty between 1 - 3 (Easy (1) / Medium (2) / Hard (3)) as it 
   will determine the complexity of the questions given,

🎗️ If you're wanting to challenge yourself, I highly suggest you pick difficulty 3!,

🎗️ Your goal is to answer the questions correctly within the three attempts given 
   or face getting the question wrong,

🎗️ You may choose to exit the quiz at any time by entering "xxx",

🎗️ Once you've completed the quiz, your results are displayed with the option of 
   viewing the question history too!.

🌟 Have Fun! :) 🌟''')


# Function to check for an integer between the inclusive numbers
def int_check(question, low=None, high=None, exit_code="xxx"):
    # Set's up the error message between the inclusive numbers
    if low is None and high is None:
        error = "Please Enter an Integer!"
    elif low is not None and high is None:
        error = f"Please Enter an Integer That is More Than or Equal to {low}!"
    else:
        error = f"Please Enter an Integer That is Between {low} and {high} (Inclusive)!"

    # Loop's until the user has entered a valid response
    while True:
        # Store's the user's response
        response = input(question)

        # Check's if the response is blank
        if response.strip() == "":
            return None

        # Check's if the exit code has been entered (xxx)
        elif response == exit_code:
            return response

        # Convert's the user's response to an integer
        try:
            response = int(response)
            # Check's if the response is between the inclusive numbers
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response
        # Print's an error if the response is not an integer
        except ValueError:
            print(error)


# Main routine..

# Initialize the variables
total_won = 0
total_lost = 0
quiz_history = []
question_number = 0

# Print's the header / title
print("✨ Welcome to Einesh's Basic Facts Quiz! ✨")

# Asks the user if they'd like the instructions using the yes/no function
print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# Display's the instructions if "Y" has been entered
if want_instructions == "yes":
    instructions()

# Asks the user for the number of questions whilst ensuring it's an integer
print()
number_questions = int_check("How many questions would you like? (<enter> for Endless Questions): ", low=1,
                             exit_code="xxx")

# If the user wants to quit, print a message and exit
if number_questions == "xxx":
    print("You Quit!")
else:
    # Asks the user for the difficulty and checks the response is an int
    desired_difficulty = int_check("Choose the difficulty ( Easy (1) / Medium (2) / Hard (3) ): ", low=1, high=3)

    # Calculates the loop of the questions
    question_loop = range(1, number_questions + 1) if number_questions else None

    # Loop's the question until everything has been answered
    while True:
        if question_loop and question_number >= len(question_loop):
            break
        question_number += 1

        # Generates the difficulty based on the level chosen
        if desired_difficulty == 3:
            num_1 = random.randint(1, 30)
            num_2 = random.randint(1, 30)
        elif desired_difficulty == 2:
            num_1 = random.randint(1, 20)
            num_2 = random.randint(1, 20)
        else:
            num_1 = random.randint(1, 10)
            num_2 = random.randint(1, 10)

        # List's the math operations in the quiz
        math_operations = ["addition", "subtraction", "multiplication", "division"]
        operation = random.choice(math_operations)

        # Generates the questions & answer based off the operation
        if operation == "subtraction":
            num_1 = num_1 + num_2
            question = f"What's {num_1} - {num_2}? "
            answer = num_1 - num_2

        elif operation == "addition":
            question = f"What's {num_1} + {num_2}? "
            answer = num_1 + num_2

        elif operation == "multiplication":
            question = f"What's {num_1} x {num_2}? "
            answer = num_1 * num_2

        else:
            num_1 = num_1 * num_2
            question = f"What's {num_1} ÷ {num_2}? "
            answer = num_1 // num_2

        # Display's the question banner and number
        if number_questions is None:
            print(f"\n⭐ Question {question_number} (Infinite Mode) ⭐")
        else:
            print(f"\n⭐ Question {question_number} of {number_questions} ⭐")

        # Reset's the attempt chances per question
        attempts = 0

        # Record's the wrong answer in the attempts
        wrong_answers = set()

        # Print's the number of attempts remaining
        while attempts < 3:
            if attempts > 0:
                print(f"\nAttempt {attempts + 1}:")

            # Record's the user's answer
            users_answer = int_check(question, low=1)

            # End's the quiz if the exit code has been entered
            if users_answer == "xxx":
                print("You've Ended the Quiz!")
                break

            # Display's if the question has been answered correctly
            if users_answer == answer:
                print(f"🎉 You got the answer right, it was {answer}")
                total_won += 1
                # Records the results for the quiz history
                quiz_history.append(
                    f"Question {question_number}: {question:<18} ({answer:>3}) - 🎉 You got the answer right! ✅")
                break

            else:
                # Display's if the incorrect answer has been previously provided
                if users_answer in wrong_answers:
                    print("💔 You already provided this incorrect answer!")
                else:
                    attempts += 1
                    wrong_answers.add(users_answer)
                    print("💔 You got the answer wrong. Please try again!")

        # End's the code once the exit code is entered
        if users_answer == "xxx":
            break

        # Display's if the question has been incorrectly answered after 3 attempts
        if attempts == 3:
            print(f"😿 Sorry, You ran out of attempts. The correct answer was {answer}")
            total_lost += 1
            # Records the results for the quiz history
            quiz_history.append(
                f"Question {question_number}: {question:<18} ({answer:>3}) - 💔 You ran out of attempts   ❌")

    # Calculate's the scores for the quiz results
    total_questions = total_won + total_lost
    correct_percentage = (total_won / total_questions) * 100 if total_questions > 0 else 0
    wrong_percentage = (total_lost / total_questions) * 100 if total_questions > 0 else 0

    # Generates personalized messages (based on the user's average score)
    if correct_percentage == 100:
        score_message = "🥳 You've gotten a score of 100%! - That's amazing!"
    elif correct_percentage >= 80:
        score_message = f"😻 You've gotten a score of {correct_percentage:.2f}%! - Great job!"
    elif correct_percentage >= 50:
        score_message = f"🙂 You've gotten a score of {correct_percentage:.2f}%! - Good Effort!"
    else:
        score_message = f"😔 You've gotten a score of {correct_percentage:.2f}%! - Continue Practicing!"

    # Display's the quiz results and score message
    print("\n📊📊 Quiz Results 📊📊")
    print(f"Questions Correct: {total_won}/{total_questions} ({correct_percentage:.2f}%)")
    print(f"Questions Wrong  : {total_lost}/{total_questions} ({wrong_percentage:.2f}%)")
    print(f"{score_message}")

    # Check if the user wants the quiz history using the yes/no function
    print()
    history_feedback = yes_no("Would you like to view the Quiz History?: ")
    # Display's quiz history if "Y" is entered
    if history_feedback == "yes":
        print("\n💫💫 Quiz History 💫💫")
        for item in quiz_history:
            print(item)

    # Display's a “Thank You” message at the end of the quiz
    print()
    print("😻 Thank You for Playing My Quiz! 😻")
