#This is the chatbot project, not the other thing

name = input("Hello, I am a chatbot set up by bank_corp set up and welcome to bank_corp. What is your name? ")
age = input("And what is your age, " + name + "? ") #Asks for user's name and age
print(age + ", I remember when I was " + age + ". Good times. Anyways, is there anything you need help with?:")
while True: #used to loop at the end of an option or if an incorrect option was chosen
    main_choices = print("""
    [1. View balance]
    [2. Buy credit card]
    [3. Feedback on this chatbot]
    [0. Exit]
        """) #Shows options, one per line. I'm not using /n because it looks weird when I'm coding
    opening_message = input("To choose a question, reply with the number of the question you need help with. ") #User picks an option
    opening_number = int(opening_message) #converts number from a string to an interger.
    if opening_number == 1:
        pass
    elif opening_number == 2:
        pass
    elif opening_number == 3:
        feedback = input('What would you like to be improved? ')
    elif opening_number == 0:
        break #makes the while function false, ultimately ending the code
    else:
        opening_message = print("It appears the choice you've chosen was not an option, the options were:")