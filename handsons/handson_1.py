### CODE HERE ###
def registration_form():
    print("Registration Form\n")
    first_name = input("First Name: ")
    surname = input("Last Name: ")
    birth_year = input ("Birth Year: ")

    print("\nWelcome {} {}!\nYour registration is complete!\nYour temporary password is {}".format(first_name, surname, first_name+'*'+birth_year))

registration_form()
