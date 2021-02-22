while True:
    num = input("Enter the number: ")
    if len(num) > 4 or len(num) < 4:
        raise Exception ("The length is too short/long !!! Please provide only four digits")