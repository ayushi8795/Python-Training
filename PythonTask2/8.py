string = input("Enter String: ")
letter = 0
digit = 0
for item in string:
    if item.isalpha() == True:
        letter = letter+1
    elif item.isdigit() == True:
        digit = digit+1
print("Letters: ",letter)
print("Digit: ",digit)