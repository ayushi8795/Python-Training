from sys import argv
argv[1] == "intro.txt"
try:
   with open(argv[1],'r') as file:
      data = file.readlines() 
      for line in data: 
         word = line.split() 
         print (word) 
except FileNotFoundError:
   print("enter name again")
   


