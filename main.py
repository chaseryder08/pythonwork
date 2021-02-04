import django
import datetime as dt

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

def get_name(msg):
    while True:
        name = input(f"{msg}: ")
        if name.isalpha():
            print("You entered a valid name")
            return name.capitalize()
        print("You entered an invalid name")

# init entries
entries = []

#Intro to start - ask User if want to access program:
while True:
    start = input("Do you forget your friend's email addresses a lot? ").lower()
    if start == "yes":
        print("So do I! You are in luck I have an app that can fix this!")
        break
    if start == "no":
        print("Well your brain works quite well  -- congrats mate!")
        exit()
    print("Please answer 'yes' or 'no'")

# get name
user_name = get_name("Enter your first name")

while True:
    # get friend name
    friend_name = get_name("Enter the FIRST name of your friend")

    # get friend email
    while True:
        friend_email = input("Enter the email of your friend: ")
        if is_valid_email(friend_email):
            print("You entered a valid email address")
            break
        print("You entered an invalid email address")

    # get friend birthday
    while True:
        bday_str = input("Enter your friend's birthday - example: mm/dd/yyyy")
        try:
            dt_bday = dt.datetime.strptime(bday_str, "%m/%d/%Y")
            dt_bday = dt_bday.date()
            print("You entered a valid birthday")
            break
        except:
            print("You entered an invalid birthday")

    # create dict and add to all entries
    dic = {"user_name": user_name, "name": friend_name, "email": friend_email, "bday": dt_bday}
    entries.append(dic)
    print(entries)
    scheduler.enqueue_at(dt_bday.____, send_email, dic)

    # print message
    message = "Dear " + friend_name + ", Just wanted to wish you a happy birthday! Love your friend, " + user_name + "."
    print(message)

    # ask if more friends
    while True:
        add_more_friend = input("Do you want to add more friends?????? - (type 'yes' or 'no') ").lower()
        if add_more_friend == "yes":
            break
        if add_more_friend == "no":
            print("Okay. That's fine")
            exit()
        print("Please answer 'yes' or 'no'")

import smtplib
def send_email(dic):
    smtplib.send_email(dic["email"], "Happy Birthday")