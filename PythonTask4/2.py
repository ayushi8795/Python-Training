def function():
    str1 = input("Enter the strind data: ")
    upper = 0
    lower = 0
    for i in str1:
        if i.isupper() == True:
            upper = upper+1
        elif i.islower() == True:
            lower = lower+1 
        else:
            pass
    print("No. of Upper case Character: ",upper)
    print("No. of Lower case Character: ",lower)
function()
            