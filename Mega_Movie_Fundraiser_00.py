#import statements

#functions to go here

# checks that ticket name is not blank

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank")
            

name = not_blank("Name: ")

#Set up dictionaries / lists needed to hold data

#Ask user if they have used the program before and show

#Loop to get ticket details

    #Get name (can't be blank)

    #Get age (between
