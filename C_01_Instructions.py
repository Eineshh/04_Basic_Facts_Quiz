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


# Display's the instructions
def instructions():
    print('''
🌟🌟 Instructions 🌟🌟

Welcome to my quiz 😊, it seems like it's your first time playing...

📌 The objective of this quiz is to test your knowledge in the basic equations of math,

📌 This quiz will contain math operations such as multiplication, division, addition, and subtraction,


🎗️ ️ To begin with, choose the desired number of questions or press <enter> for 
   ️  endless questions,

🎗️ Next, choose the difficulty between 1 - 3 (Easy (1) / Medium (2) / Hard (3) as it 
    will determine the complexity of the questions given,

🎗️ If you're wanting to challenge yourself, I highly suggest you to pick difficulty 3!,

🎗️ Your goal is to answer the questions correctly within the three attempts given 
    or face getting the question wrong,

🎗️ You may choose to exit the quiz at any time by entering "xxx",

🎗️ Once you've completed the quiz, your results are displayed with the option of 
    viewing the history of your questions too.


🌟 Have Fun! :) 🌟''')


# Main routine
print("✨ Basic Facts Quiz ✨")

# loop for testing purposes
print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
