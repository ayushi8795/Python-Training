even_list =[]
odd_list =[]
for i in range(1,11):
    num = int(input("Enter number in range 1 to 50: "))
    if num>50:
        break
    else:
        if num%2 == 0 and len(even_list)<=5:
            even_list.append(num)
        elif num%2 != 0 and len(odd_list)<=5:
            odd_list.append(num)
even = sum(even_list)
odd = sum(odd_list)
print("even_list: ",even_list)
print("Addition of even_list: ",even)
print("odd_list: ",odd_list)
print("Addition of odd_list: ",odd)
print("Maximum of List: ",max(even,odd))