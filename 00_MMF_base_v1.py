#import statements



#functions go here

#*********Main Routine*********



#set up dictionaries / lists needed to hold data


#ask user if they have used the program


#loop to get ticket details

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
                  "please enter your name")

#Main routine goes here

name = not_blank("Name: ")
name = ""
count = 0

MAX_TICKETS = 5


while name != "xxx" and count < MAX_TICKETS:

    print("You have {} seats "
    "left".format(MAX_TICKETS - count))


    #Get details
    name = input("Name: ")
    count += 1
    print()


if count == MAX_TICKETS:
    print("You have sold all the available tickets!")

else:
    print("""You have sold {} tickets.
There are {} places still available"""
          .format(count, MAX_TICKETS - count))



    




    #get name(can't be blank)



    #get age (between 12-13)


    #calculate ticket price


    #loop to ask for snacks


    #calculate snack price


    #ask for payment method (and apply surcharge if necessary)


#calculate total sales and profit
