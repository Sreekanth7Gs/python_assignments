print("++++WELOME TO SIMPLE QUIZ++++")

Q1 = "Q1.What is the capital of India?"
choices = ("A. Chennai B. Bengaluru C. Delhi D. Mumbai")
count = 0  

print(Q1)
print(choices)
print("Give your choice")
user_choice = input().upper()

if user_choice == 'C':
    print("You are correct")
    count += 1
else:
    print("Wrong")
Q2 = ("Q2.Which is following city is from india?")
choices_2 = ("A. Madrid B.Paris C. Karachi D.Bengaluru")
print(Q2)
print(choices_2)
print("Give Your Choice")
user_choice = input().upper()

if user_choice == 'D' : 
      print("You are correct")
      count += 1
else:
    print("Wrong")
    
Q3 = "Q3.India is from which continent"
choices_3 ="A.Asia B.America C. Europe D. Africa"
print(Q3)
print(choices_3)
print(" Give Your Choice")
user_choice = input().upper()
if user_choice == 'A' : 
      print("You are correct")
      count += 1
else:
    print("Wrong")
    
Q4 = "Q4. How many days are there in a week?"
choices_4 = "A.3 B.7 C.12 D.4" 
print(Q4)
print(choices_4)
print(" Give Your Choice")
user_choice = input().upper()
if user_choice == 'B' : 
      print("You are correct")
      count += 1
else:
    print("Wrong")
    
Q5 = "Q5.Which animal is known as the king of the jungle?"    
choices_5 = "A.Lion B.Tiger C.Elephant D.Fox"
print(Q5)
print(choices_5)
print(" Give Your Choice")
user_choice = input().upper()
if user_choice == 'A':  
      print("You are correct")
      count += 1
else:
    print("Wrong")
Q6 = "Q6.Name the National bird of India?"
choices_6 = "A.Peacock B.Pigeon C.Parrot D.owl"
print(Q6)
print(choices_6)
print(" Give Your Choice")
user_choice = input().upper()
if user_choice == 'A' : 
      print("You are correct")
      count += 1
else:
    print("Wrong")
Q7 = "Q7.Name the National animal of India?"
choices_7 = "A.Tiger B.Lion C.Fox D.Elephant"
print(Q7)
print(choices_7)
print(" Give Your Choice")
user_choice = input().upper()
if user_choice == 'A':  
      print("You are correct")
      count += 1
else:
    print("Wrong")
Q8 = "Q8.Which animal is known as the 'Ship of the Desert?"
choices_8 = "A.Horse B.Camel C.Zebra D.Deer"
print(Q8)
print(choices_8)
print(" Give Your Choice")
user_choice = input().upper()
if user_choice == 'B' : 
      print("You are correct")
      count += 1
else:
    print("Wrong")
    
print ("** -- THANK YOU --**")   
print(f" You Answered {count} out of 8 are correct ")





