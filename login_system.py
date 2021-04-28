########################################################################################################################
#Start of Program - asks if user has account
########################################################################################################################
dict_lib = {"chase@gmail.com":["chasey223","pass123"],"Joe14abs@yahoo.com":["Joesph1245","goober1"]}
user=""
password=""
email_add="" 

########################################################################################################################
#Check credential entry is up to snuff
########################################################################################################################

def check_email(email_add):
    for x in email_add:
        if ('@' not in email_add):
           print("Your email should include \" @ \" - Try again") 
           break 
        elif '.' not in email_add:
            print("Your email should include \" . \" - Try again ")
            break
        elif '@' not in email_add and "." not in email_add:
           print("Your email should include \"@ \" and  \".\" - Try again")
           break
        else:
            return True

def check_user(user):
    if len(user)<8:
        print("Your username must be atleast 8 characters")
    else:
        return True
        
def check_pass(password):
    while True:
        for x in password:
            count = 0
            if x in spec_chars:
                count+=1
                if count>=3:
                    print("Successful password!")
                    return False
            else:
                print("You must have atleast 3 special characters in your password")
                return True     

########################################################################################################################

def create_account(email_add, user, password):
    email_add = input("Enter your email address: ")

    #Check IF False - reenter input -
    if not (check_email(email_add)):
        while True:
            email_add = input("Enter your email address: ")
            if check_email(email_add):
                print("VALID EMAIL ADDRESS " + email_add)
            return False

    
    user = input("Create a username : ")
    if not (check_user(user)):
        while True:
            user = input("Create a username : ")
            if check_user(user):
                print("VALID USERNAME + ", user)
            return False

    password = input("Create a password : ")
    if not (check_pass(password)):
        password = input("Your password needs to have atleast 8 letters and 3 special characters - Try again : ")
        if check_user(user):
            print("VALID USERNAME : " + password)
        return password
        False

########################################################################################################################
#Login check of username and password
########################################################################################################################

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

start = input("Do you have an account with us? ").lower()

########################################################################################################################
#user must either enter yes or no 
########################################################################################################################

while True:
    if start == "yes":
        login(user, password)
    elif start == "no":
        create_account(email_add, user, password)
    else:
        start = input("That is an invalid entry - Please type either 'yes' or 'no' ")

########################################################################################################################
#User creates new account
########################################################################################################################

spec_chars = "[@_!#$%^&*()<>?/\|}{~:]"
elist = []
dict = {}

def dataAdd(email_add, user, password):
    dict[email_add] = [user, password]
    #dict[1]=uinfo[0][2]
    return dict

#Ask person for username password or create account


#email username
#password - check if they are both correct
#store in text file
#Page - create account or login?
#save and validate against text file


start()