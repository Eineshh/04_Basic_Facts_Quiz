# checks for an integer with optional upper / lower limits and exit code for infinite mode / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an Integer"

    # if the number needs to be more than an integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = f"Please enter an Integer that is more than / equal to {low}"

    # if the number needs to between low & high
    else:
        error = f"Please enter an Integer that is between {low} and {high} (inclusive)"

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)
