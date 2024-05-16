def quiz():
    # Initializes variables
    question_num = 0
    history = []
    round_won = 0
    round_lost = 0

    # asks the user how hard they would like the quiz to be
    difficulty = int_check("What level of difficulty do you want to play? 1 to 3, with 3 being the hardest: ",
                           low=1, high=3)

    # loops while question_num is lower than amount of questions - chosen at the start
    while question_num < amount_questions:

        print()
        print(f"Question {question_num + 1}:")

        # Generates the numbers for the question and difficulty
        if difficulty == 3:
            num_1 = random.randint(1, 25)
            num_2 = random.randint(1, 25)
        elif difficulty == 2:
            num_1 = random.randint(1, 15)
            num_2 = random.randint(1, 15)
        else:
            num_1 = random.randint(1, 10)
            num_2 = random.randint(1, 10)

        # the list for the types of question
        math_type = ["multiplication", "adding", "subtraction", "division"]

        # generates the question type
        question_type = random.choice(math_type)

        # generates the question format
        if math_type == "subtraction":
            num_1 = num_1 + num_2
            question_format = f"What is {num_1} - {num_2}? "
            answer = num_1 - num_2

        elif question_type == "adding":
            question_format = f"What is {num_1} + {num_2}? "
            answer = num_1 + num_2

        elif question_type == "multiplication":
            question_format = f"What is {num_1} x {num_2}? "
            answer = num_1 * num_2

        else:
            # makes sure that the number being divided is always going to result in a whole number
            num_1 = num_1 * num_2
            question_format = f"What is {num_1} divided by {num_2}? "
            answer = num_1 / num_2

        # The user gets to ask the question
        user_answer = int_check(question_format, low=1)

        # makes the answer an integer
        answer = int(answer)

        # if the user types the exit code they are able to leave the game
        if user_answer == "xxx":
            print("Thanks for playing my basic math quiz!")
            print()
            break

        # sets correct to yes if the answer is correct
        elif user_answer == answer:
            round_won += 1
            feedback = f"You got the answer right, it was {answer}"
            history_item = f"Question {question_num + 1}: You got the answer right, it was {answer} ✅."

        # sets correct to no
        else:
            round_lost += 1
            feedback = f"You got the answer wrong, it was {answer}"
            history_item = f"Question {question_num + 1}: You got the answer wrong, it was {answer} ❌."

        # adds the round result into a list
        history.append(history_item)

        # prints the feedback/result of the round
        print(feedback)

        question_num += 1

    # if the user doesn't answer a single question it doesn't display stats/history
    if question_num == 0:
        print("Sorry you have not answered a single question thus there is no history"
              "or statistics we can show you.")
        exit()

    # asks the user whether they would want to see the game history
    view_history = yes_no("Do you want to view the game history?")
    print()

    # displays the game history if the user wants to see it
    if view_history == "yes":
        print("\n⌛⌛⌛ Game History ⌛⌛⌛ ")
        print()
        # Outputs the game history
        for item in history:
            print(item)

    # Asks the user if they want to view the game stats
    print()
    view_stats = yes_no("Do you want to view the stats? ")
    print()

    # If yes, displays the game stats
    if view_stats == "yes":
        # Calculates the win percentage
        question_correct = round_won / question_num * 100

        # Calculates loss percentage:
        question_wrong = round_lost / question_num * 100

        print(f"Out of {question_num} questions:")
        print()
        print(f"- {question_correct:.2f}% of questions correct")
        print()
        print(f"- {question_wrong:.2f}% of questions wrong")
        print()