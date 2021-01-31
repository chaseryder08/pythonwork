def bday_dig():    
    boo = input("Enter your birthday - example: mm/dd/yyyy ")
    while boo.isdigit() != True:
        boo = input("Only enter numbers please -- try again..." )


    boo = [int(x) for x in boo]
    while boo[0] > 12 or boo[1] > 31 or boo[2] < 1900:
        if boo[0] > 12:
            print("You entered an incorrect month - please provide a month 1-12 : ")
        elif boo[1] > 31:
            print("You entered an incorrect day - please provide a day 1-31 : ")
        elif boo[2] < 1900:
            x= 2021 - boo[2] 
            print(f"Are you sure you are {x} years old? No way! Try again : ")
        boo = input("Enter your birthday - example: mm/dd/yyyy ").split('/')
        boo = [int(x) for x in boo]
    else:
        print("Thank you - you entered a correct birthdate")
        
            
        

'''
    while boo.isdigit() != True:
        boo = input("Only enter numbers please -- try again..." )
        if(boo.isdigit() == True):
            for x in boo:
                if ('/' not in boo):
                    boo = input("You need to use ' / ' in your bday - example: 08/08/1985" ) 
                    break    
                else:
                    return True'''

bday_dig()