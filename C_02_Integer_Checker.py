# Check's if the user has entered a valid integer
def int_check(question, low=None, high=None, exit_code="xxx"):

    # Sets up the error message

    if low is None and high is None:
        error = "Please Enter an Integer"

    # Checks if the number entered is an integer
    elif low is not None and high is None:
        error = f"Please Enter an integer That is More Than or Equal to {low}"

    # Checks if the number entered is between a high and low number (inclusive)
    else:
        error = f"Please Enter an Integer That is Between {low} and {high} (Inclusive)"

    while True:
        response = input(question)

        if response.strip() == "":
            return None

        elif response == exit_code:
            return response

        try:
            response = int(response)
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response
        except ValueError:
            print(error)