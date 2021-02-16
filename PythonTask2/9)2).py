number = -1
again = "yes"
while number != 5 and again != "no":
    number = int(input("Guess the lucky number: "))
    if number != 5:
        print ("That is not the lucky number")
        again = input("Would you like to guess again? Type yes or no ")
