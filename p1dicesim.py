#dice simulator
import random

# print(x)

#check number and print dice face
def dice():

    x = "y"
    while x == "y": #loops
        number = random.randint(1,6) #develop random number

        if number == 1:
            print ("---------")
            print ("|       |")
            print ("|   0   |")
            print ("|       |")
            print ("---------")
        if number == 2:
            print ("---------")
            print ("|       |")
            print ("| 0   0 |")
            print ("|       |")
            print ("---------")
        if number == 3:
            print ("---------")
            print ("|   0   |")
            print ("|   0   |")
            print ("|   0   |")
            print ("---------")
        if number == 4:
            print ("---------")
            print ("| 0   0 |")
            print ("|       |")
            print ("| 0   0 |")
            print ("---------")
        if number == 5:
            print ("---------")
            print ("| 0   0 |")
            print ("|   0   |")
            print ("| 0   0 |")
            print ("---------")
        if number == 6:
            print ("---------")
            print ("| 0   0 |")
            print ("| 0   0 |")
            print ("| 0   0 |")
            print ("---------")
        x = input("enter y to roll the dice again or else to exit : ")
    
    if(x == "y"):
        dice()
    else:
        pass
dice()