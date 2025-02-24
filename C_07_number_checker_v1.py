# Functions go here

def num_check(question, change_to, exit_code="xxx"):
    """Checks users enter an integer / float that is more than
    zero (or the optional exit code)"""

    error = "Oops - please enter an integer more than zero."

    while True:
        response = input(question).lower()

        # check for exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

# loop for testing purposes


while True:
    print()

    my_float = num_check("Please enter a number (float) more than 0: ", float)
    print(f"Thanks. You chose {my_float}")
    if my_float == "xxx":
        break

    print()
    my_int = num_check("Please enter an integer more than 0",
                       int, "")
    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")
