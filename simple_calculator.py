num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("select the operation to perform:")
choices = "A.Addition B. Subtraction C. Multiplication D. Division"
print(choices)
user_choices = input().upper()
if user_choices == 'A':
   Addition = num1 + num2
   print ("Result: ",Addition)
elif user_choices == 'B':
   Subtraction = num1 - num2
   print("Result: ",Subtraction)
elif user_choices == 'C':
   Multiplication = num1*num2
   print("Result: ",Multiplication)
elif user_choices == 'D':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        Division = num1 / num2
        print("Result:", Division)
else:
    print(" INVALID ")
     
   