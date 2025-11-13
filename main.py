#This is the chatbot project
#I feel like Im trying to make this fpr people who recently graduated or are about to graduate and don't know how banks work

#Prompt:
# You are working for a bank/financial institution/credit card company and you need to create a chatbot 
# that will help new customers choose what kind of account they want and help get them started signing up
#DOESNT SAY LOGIN


def user_money_the_function(): #This is function is to track cash after setting up an account, later converts from UMTF to UMTV
#Probably don't need to say this, but this was originally just user_money
#but I couldn't think of better variable names and I didn't want user_money = user_money()
    while True:
        try: # So it doesn't crash when non-number is entered
            user_money_input = input("One more question, how much money do you have? This is important for later. $") #used during count balance to open account
            user_money_float = float(user_money_input) #string --> float for numbers
            return user_money_float # links the money with the function
        except ValueError as e: #as e so only when error
            print("You need to type as a number and rounded down to the nearest whole number, no letters or symbols beside allowed.")


def username_list(): #This function is to stop duplicate usernames
    usernames = []
    try:
        with open("username.txt", "r") as file:#For a while, I accidently had this as usernames instead of username.
        #I googled searched ways to save and this was the only one I found that didn't use 3rd-party or my storage
            for line in file:
                parts = line.strip().split(", ")
                for part in parts:
                    if part.startswith("Username:"):
                        username_str = part.split(": ")[1]
                        usernames.append(username_str)
    except FileNotFoundError: #If file is missing for whatever reason
        pass
    return usernames


class account:
    def __init__(self, username, password, account_type, user_money):
        self.username = username
        self.password = password
        self.account_type = account_type
        self.user_money = user_money


def create_checking_account(user_money_the_variable): #UMTV used for the > and <
    print("Our checking account interest rate is, on average, increase of 0.1% per month and it is a minimum of $100 to open an account")
    try:
        if user_money_the_variable >= 100: #>= and not > because what if user number is 100
            while True:
                checking_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if checking_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break
            checking_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new checking account? you have ${user_money_the_variable:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > user_money_the_variable:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(checking_username + " and " + checking_password + " are your username and password")
            new_account = account(checking_username, checking_password, "checking", user_money_the_variable)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You have ${new_account.user_money} in your account. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have ${umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing
        

    except TypeError as e: #Happens during 2nd attempt, 
        if umtv_but_updated >= 100: #>= and not > because what if user number is 100
            while True:
                checking_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if checking_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break     
            checking_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new checking account? you have ${umtv_but_updated:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > umtv_but_updated:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(checking_username + " and " + checking_password + " are your username and password")
            new_account = account(checking_username, checking_password, "checking", umtv_but_updated)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You now have ${new_account.user_money}. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have {umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing


def create_saving_account(user_money_the_variable): #Its just copy and paste from checkings with changing checkings to savings
    print("Our savings account interest rate is, on average, increase of 0.4% per month and it is a minimum of $100 to open an account")
    try:
        if user_money_the_variable >= 100: #>= and not > because what if user number is 100
            while True:
                saving_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if saving_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break
            saving_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new saving account? you have ${user_money_the_variable:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > user_money_the_variable:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(saving_username + " and " + saving_password + " are your username and password")
            new_account = account(saving_username, saving_password, "saving", user_money_the_variable)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You have ${new_account.user_money} in your account. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have ${umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing
        

    except TypeError as e: #Happens during 2nd attempt, 
        if umtv_but_updated >= 100: #>= and not > because what if user number is 100
            while True:
                saving_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if saving_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break     
            saving_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new savings account? you have ${umtv_but_updated:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > umtv_but_updated:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(saving_username + " and " + saving_password + " are your username and password")
            new_account = account(saving_username, saving_password, "saving", umtv_but_updated)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You now have ${new_account.user_money}. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have {umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing

 
def create_MM_account(user_money_the_variable): #Its just copy and paste from checkings with changing checkings to MM
    print("Our MM account interest rate is, on average, increase of 4.5% per month and it is a minimum of $1500 to open an account")
    try:
        if user_money_the_variable >= 100: #>= and not > because what if user number is 100
            while True:
                MM_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if MM_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break
            MM_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new Money Market account? you have ${user_money_the_variable:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > user_money_the_variable:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(MM_username + " and " + MM_password + " are your username and password")
            new_account = account(MM_username, MM_password, "Money Market", user_money_the_variable)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You have ${new_account.user_money} in your account. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have ${umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing
        

    except TypeError as e: #Happens during 2nd attempt, 
        if umtv_but_updated >= 100: #>= and not > because what if user number is 100
            while True:
                MM_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if MM_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break     
            MM_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new Money Market account? you have ${umtv_but_updated:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > umtv_but_updated:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(MM_username + " and " + MM_password + " are your username and password")
            new_account = account(MM_username, MM_password, "Money Market", umtv_but_updated)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You now have ${new_account.user_money}. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have {umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing


def create_CD_account(user_money_the_variable): #Its just copy and paste from checkings with changing checkings to Certificate of deposit
    print("Our Certificate of Deposit interest rate is, on average, increase of 0.4% per month and it is a minimum of $100 to open an account")
    try:
        if user_money_the_variable >= 100: #>= and not > because what if user number is 100
            while True:
                CD_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if CD_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break
            CD_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new Certificate of Deposit? you have ${user_money_the_variable:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > user_money_the_variable:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(CD_username + " and " + CD_password + " are your username and password")
            new_account = account(CD_username, CD_password, "Certificate of Deposit", user_money_the_variable)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You have ${new_account.user_money} in your account. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have ${umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing
        

    except TypeError as e: #Happens during 2nd attempt, 
        if umtv_but_updated >= 100: #>= and not > because what if user number is 100
            while True:
                CD_username = input('What do you want your username to be? ')
                existing_users =  username_list() # ffunction->Variable converter
                if CD_username in existing_users: #Checks if username is available
                    print("Username is already taken")
                else:
                    break     
            CD_password = input('And your password? ')
            while True: #Loops until valid deposit ammount
                try:
                    initial_deposit = input(f"How much do you want to add to your new Certifcate of Deposit? you have ${umtv_but_updated:.2f}. ")
                    initial_deposit = float(initial_deposit) # String -> Float so > and < can be used
                    if initial_deposit < 100:
                        print("You need atleast $100 to make an account")
                    elif initial_deposit > umtv_but_updated:
                        print("Your initial_deposit exceeds the ammount of money you have")
                    else: #If money in correct range, account creatition process continues
                        break
                except ValueError: #letters were typed instead of numbers at initial_deposit
                    print("Enter a number and not letters")
            print(CD_username + " and " + CD_password + " are your username and password")
            new_account = account(CD_username, CD_password, "Certificate of Deposit", umtv_but_updated)
            #umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            new_account.user_money = initial_deposit #Updates user's money
            print(f"{new_account.account_type} account created for {new_account.username}")
            print(f"You now have ${new_account.user_money}. ") #new_account is the variable while user_money is a trait.
            try:
                with open("username.txt", "a") as file:#creates list of usernames
                    account_data = f"Username: {new_account.username}, Password: {new_account.password}, AccountType: {new_account.account_type}, Balance: {new_account.user_money}"
                    file.write(account_data +'\n')#\n so its not all on one line
                print("Account details saved")
            except IOError as e:
                print(f"An error occurred when attempting to save: {e}")
            umtv_but_updated = user_money_the_variable - initial_deposit #updates money
            print(f'You now have {umtv_but_updated} to get accounts with. ')
            return new_account and umtv_but_updated #try random stuff and hope it works strat works???
        else:
            print('You do not have enough money to open an account.')
            return None #Returns nothing


def view_users():  #not username_list, uList checks for duplicate usernames while vUsers prints the list
    information = []
    try:
        with open("username.txt", "r") as file:#For a while, I accidently had this as usernames instead of username.
        #I googled searched ways to save and this was the only one I found that didn't use 3rd-party or my storage
            for line in file:
                parts = line.strip().split(", ")
                for part in parts:
                    if part.startswith("Username:"):
                        username_str = part.split(": ")[1]
                        information.append(username_str)
                        print(username_str)
                    elif part.startswith("AccountType:"):
                        ACCtypes_str = part.split(": ")[1]
                        information.append(ACCtypes_str)
                        print(ACCtypes_str)
                    elif part.startswith("Balance:"):
                        Balance_str = part.split(": ")[1]
                        information.append(Balance_str)
                        print(Balance_str + '\n --------------------')    
    except FileNotFoundError as e: #If file is missing for whatever reason
        pass
    return information


def explain(): #I feel like the target audiance is people who don't know how banks work.
    #I also didn't know what the diffrent types were prior to the projet so I felt like I needed to add this.
    #I learned the account types from from www.bankrate.com/banking/types-of-bank-accounts/
    print("""
    Before reading, you need to know an interest is your money, 
    wether that be at the begining at the deposit or current ammount, times a number that differs by bank.
    Interest increases the ammount of money you have, basically an investment
          
    1. A checking account has easy access to your money, but low interest.
    2. A savings account has high interest but a monthly imit on deposits and withdraws.
    3. A money market (MM) account is a combination of a checkings account and savings account;].
        It has a higher interest than checkings and savings similiar restrictions as savings, but requires more money to start up
    4. A certificate of deposit or CD is a deposit that has the highest interest rate between the options and
        lasts over a set time that you can't withdraw without losing money.
    5. Prints a list of all accounts, with their account types balances, but not their passwords for account safety.
          Its more of a developer thing but it can be used to check for avalible usernames.
    6. This is the current explanation you are reading
    0. This ends the chatbot conversation
                """)
   

def main_screen(user_money_the_variable):
    while True: #used to loop at the end of an option or if an incorrect option was chosen
        main_choices = print("""
        [1. Create a checking account]
        [2. Create a savings account]
        [3. Create a money market account]
        [4. Create a Certificate of Deposit]
        [5. Show a list of all users]
        [6. Explain what these options mean]
        [0. Exit]
        """) #Shows options, one per line. I'm not using /n because it looks weird when I'm coding. 
        try:
            opening_message = input("To choose a question, reply with the number of the question you need help with. ") #User picks an option
            opening_number = float(opening_message) #converts number from a string to an float. Not integer because ValueError wouldn't work
        except ValueError as e:
            print('You have to use numbers and not letters')
            main_screen(user_money_the_variable)#Had an error here where I forgot to add umtv

        if opening_number == 1: #Checking account
            user_money_the_variable = create_checking_account(user_money_the_variable) #UMTV updates after 1 is done with umtv
        elif opening_number == 2: #Savings account
            user_money_the_variable = create_saving_account(user_money_the_variable) #same as 1 but instead of 1 its 2
        elif opening_number == 3: # Money Market Account
            user_money_the_variable = create_MM_account(user_money_the_variable) #same as 2 but instead of 2 its 3
        elif opening_number == 4: # Certificate of Deposit
            user_money_the_variable = create_CD_account(user_money_the_variable) #same as 3 but instead of 3 its 4
        elif opening_number == 6: #explains the diffrences between accounts
            explain()
        elif opening_number == 5: #Views all the accounts made
            view_users()
        elif opening_number == 0: #Ends the program
            break #makes the while function false, ultimately ending the code
        else:
            opening_message = print("It appears the choice you've chosen was not an option, the options were:")


##############################################
############T##E##R##M##I##N##A##L############
##############################################
###MADE##TO#MAKE#THE##CODE#OUTLINE#READABLE###
##############################################

name = input("Hello, I am a chatbot set up by bank_corp set up and welcome to bank_corp. What is your name? ")
age = input("And what is your age, " + name + "? ") #Asks for user's name and age
print(age + ", I remember when I was " + age + ". Good times.")
user_money_the_variable = user_money_the_function() #function->variable converter
print("Thanks for answering, what kind of account do you want to open: ")            
user_money_the_variable = main_screen(user_money_the_variable)#User_money_the_variable updates through main
print('Thanks for creating an account, or multiple, or none, until next time.')