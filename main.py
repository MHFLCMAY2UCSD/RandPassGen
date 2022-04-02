from PasswordGen import *


def main():

    game_on = True
    while game_on:
        print("Hello, Please enter the email of the password you want to generate.")
        while True:
            try:
                user_input = str(input())

                # Checking for white spaces
                toggle = False
                for i in user_input:
                    if i == " ":
                        toggle = True

                if toggle:
                    print(
                        "Sorry please enter their might be spaces in what you entered.  Please try again.")
                else:
                    well = confirming(user_input)
                    if well:
                        break
                    else:
                        print(
                            "Please enter your email address to generate a password: ")
            except ValueError:
                print("This is not a valid input.  Please try again.")

        print("Please enter the length of the password you would like to create between 8 - 16: ")
        while True:
            try:
                user_password_length = int(input())
                if user_password_length < 8 or user_password_length > 16:
                    print(
                        "Sorry please enter a integer between 8 - 16.  Please try again.")
                else:
                    break
            except ValueError:
                print("This is not a valid input.  Please try again.")

        # Constructor Call
        used = Password(user_password_length)

        # Get Password
        password = used.random_ascii()

        output_string = user_input + " - " + password + '\n'

        ifstream = open("stuff.txt", 'a+')
        ifstream.write(output_string)
        ifstream.close()

        game_on = keep_playing()


def confirming(name: str):
    print("Is this the correct email address?: ", name, "?")

    # priming read
    user_input = str(input())
    user_input = user_input.upper()
    while user_input != "YES" and user_input != "NO":
        print("Please enter either yes or no: ")
        user_input = str(input())
        user_input = user_input.upper()
    return user_input == "YES"


def keep_playing():
    print("Create another password?")
    question = str(input().upper())
    while question != "NO" and question != "YES":
        print("Please enter either yes or no: ")
        question = str(input()).upper()

    if question == "YES":
        return True
    else:
        return False


main()
