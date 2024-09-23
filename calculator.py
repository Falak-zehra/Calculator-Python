print("........Mini Calculator.....")

b = int(input("\nEnter first number"))

c = int(input("\n Enter second number"))
 

print("\n1. Addition\n 2. Substraction \n 3. Multiplication \n 4. Division\n")

a = input("Choose from 1 to 4\n")

if a == "Addition" or a == "addition" or a == "1" :
    print((b+c))
 
elif a == "Substraction" or a == "substraction " or a == "2":
    print(b-c)

elif a == "Multiplication" or a == "multiplication" or a ==" 3" :
    print(b * c)
elif a  == "Division " or a == "division" or a == "4":
    print(b/c)    
else:
    print("Wrong Input. Please choose from 1 to 4")


