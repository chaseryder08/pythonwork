dict_lib = {"chase@gmail.com":["chasey223","pass123"],"Joe14abs@yahoo.com":["Joesph1245","goober1"]}
user=""
password=""
email_add="" 
entries = []

#check if valid email
def is_valid_email(email_add):
    if '@' not in email_add and "." not in email_add:
        print("Your email should include \"@ \" and  \".\" ")
        return False      
    if '@' not in email_add:
        print("Your email should include \" @ \" ")
        return False         
    if '.' not in email_add:
        print("Your email should include \" . \" ")
        return False
    return True

def is_valid_user(user):
    if len(user) < 8:
        print("Your username must be atleast 8 characters")
        return False
    return True

def is_valid_pass(password):
    SpecialSym ='!@#$%^&*()_+-='
    val = True
      
    if len(password) < 6:
        print('Your password should be at least 6 characters')
        val = False
          
    if len(password) > 20:
        print('Your password should be not be greater than 8 characters')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of special symbol')
        val = False
    if val:
        print("good pass")
        return val


    #for email, cred in dict_lib.items():
      #  for user in cred[0]:
          #  if user == user:
              # print(f"{user_name} is already taken - create another username")

def create_account(email_add, user, password):            

    while True:
        email_add = input("Enter your email address: ")
        if is_valid_email(email_add):
            print("You entered a valid email address")
            break
        print("You entered an invalid email address")

    while True:
        user = input("Enter a username: ")
        if is_valid_user(user):
            print("You entered a valid username")
            break
        print("You entered an invalid username")    

    while True:
        password = input("Enter a password: ")
        if is_valid_pass(password):
            print("You entered a valid password")
            break
        print("You entered an invalid password")
       

    print(email_add)
    print(user)
    print(password)

    dic = {"email": email_add, "username": user, "password": password}
    entries.append(dic)
    print(entries)
    


def login(user, password):
    while True:
        check_user = input("Enter your user name: ")
        if check_user == user:
            break
        else:
            check_user= input("Invalid user - Try again ")

    #Check password - 3 tries then loop back to user*
    counter = 0       
    while counter<3:
        check_password = input("Enter your password: ")
        if check_password == password:
            break
        else:
            print("Invalid password - Try again ")
            counter+=1
    #If used 3 tries, restart ask for username
    if counter==3:
        print("You have no attemps left - please start again.")
        return True
    
    #SUCCESSFUL LOGIN
    print("You have successfully logged in -- Thank you!")
    exit()


#asks user to login or create account
start = input("Do you have an account with us? ").lower()

while True:
    if start == "yes":
        login(user, password)
    elif start == "no":
        create_account(email_add, user, password)
    else:
        start = input("That is an invalid entry - Please type either 'yes' or 'no' ")


