print("Sign in")

phone_number = input("Enter your number: ")
password = input("Enter your password: ")

login_success = False

for i in range(3):

    print("\nLog in")

    phone_number_1 = input("Enter your number: ")
    password_1 = input("Enter your password: ")

    if password_1 == password and phone_number_1 == phone_number:
        print("Welcome")
        login_success = True
        break

    else:
        print("Wrong number or password. Try again.")


if login_success:

    language = input("\nLanguage you like: ")

    hindi_list = (
        "Delhi Crime",
        "Sacred Games",
        "Amar Singh Chamkila"
    )

    english_list = (
        "Game of Thrones",
        "Breaking Bad",
        "From",
        "Dark"
    )

    if language == "hindi":
        print("Suggestions:", hindi_list)

    elif language == "english":
        print("Suggestions:", english_list)

    else:
        print("Please select English or Hindi")

    print("Home page")

else:
    print("You have used all 3 attempts.")

