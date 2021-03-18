# Author:       Emin Girgin
# Date:         March 17th, 2021
# Description:  This program will count the characters that user entered input.


# Creating a boolean loop to end script or allow user to enter bowling scores again
continue_counting = True

# Repeat the run of the program as long as the user wants to continue.
while continue_counting:

    # Input

    # Prompt the user to enter input to count characters

    user_input = input("Please enter text to count characters: ")

    # Output

    print(len(user_input))

    # Program will check user wants to re-enter values or kill the app

    # Prompt the user to start from the beginning again.
    user_choice = input("\nWould you like to enter another text to count characters? \n Please enter 'Y' to continue or 'N' to exit: ")



    # Continue until they enter either "Y" or "N".
    while user_choice:
        # If they enter "yes", don't prompt again, remove the user input and we'll start over.
        if user_choice.upper().strip() == "Y":
            user_choice = ""
            user_input = ""
        # If they enter "N", don't prompt again, set continue_counting to false so the program ends.
        elif user_choice.upper().strip() == "N":
            get_bowling_scores = False
            user_choice = ""
        # If user input different than 'Y' or 'N' prompt user to enter correct answer
        else:
            user_choice = input("\nPlease enter 'Y' or 'N'. Would you like enter text to count characters ? : ")
    
