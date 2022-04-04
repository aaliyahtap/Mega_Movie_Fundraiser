#import statements



#functions go here


#checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)
        
        #if name is not blank, program continues
        if response != "":
            return response
        #if name is blank, show error(and repeat loop)
        else:
            print("Sorry, this can't be blank, "
                  "please enter your name.")




#*********Main Routine*********



#set up dictionaries / lists needed to hold data


#ask user if they have used the program


#loop to get ticket details

name = ""
count = 0

MAX_TICKETS = 5


while name != "xxx" and count < MAX_TICKETS:
    
    #shows the user how many seats are left
    if count < 4:
        print("You have {} seats "
        "left".format(MAX_TICKETS - count))
        
    #this will show the user that there is one seat left.
    else:
        print("There is ONE seat left!")


    #Get details
    name = not_blank("Name: ")
    count += 1
    print()


if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
    
#shows the user how many tickets are sold and how many are left
else:
    print("""You have sold {} tickets.
There are {} places still available"""
          .format(count, MAX_TICKETS - count))



#checks that ticket name is not blank







    #get name(can't be blank)



    #get age (between 12-13)


    #calculate ticket price


    #loop to ask for snacks


    #calculate snack price


    #ask for payment method (and apply surcharge if necessary)


#calculate total sales and profit
