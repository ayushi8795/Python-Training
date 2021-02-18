def function():
    str1 = input("Enter the string to be reversed: ")
    str1 = list(str1)
    str1.reverse()
    str2 = ''.join(str1)
    print("Reversed String: ",str2)
function()
            