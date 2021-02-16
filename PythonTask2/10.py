counter = 1
while counter <= 5:
    number = int(input("Guess the " + str(counter) + ". number "))
    if number != 5:
        print("Try again.")
        counter = counter +1
    elif number ==5:
        print("Good guess!")
        counter = counter +1
print ("Game over")