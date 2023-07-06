# calculator
its a simple calculator.I made it in grade 12th have a look.
print("\t\t\tcomputer science project\nCALCULATOR\t\t\t")
#\n  newline charater  /t tab space 
print("-------------------------------------------------------------")
print("a - ADDITION","s - SUBSTRACTION","m - MULTIPLICATION","d - DIVISION","q-to the power")
print("--------------------------------------------------------------")
print("maximum 5 numbers can be entered")
no=int(input("enter total number  with which you want to do operation:-"))
       
if no==2:
       number_1=float(input("enter number:"))
       number_2=float(input("enter number:"))
elif no==3:
        number_1=float(input("enter number:"))
        number_2=float(input("enter number:"))
        number_3=float(input("enter number:"))
elif no==4:
        number_1=float(input("enter number:"))
        number_2=float(input("enter number:"))
        number_3=float(input("enter number:"))
        number_4=float(input("enter number:"))
elif no==5:
        number_1=float(input("enter number:"))
        number_2=float(input("enter number:"))
        number_3=float(input("enter number:"))
        number_4=float(input("enter number:"))
        number_5=float(input("enter number:"))
else:
        print("minimum  number with which operation can be done is 2 and maximum number with which operation can be done is 5")
"a - ADDITION"
"s - SUBSTRACTION"
"m - MULTIPLICATION"
"d - DIVISION"
"q-to the power"
user_input = input("enter the operation alphabet:")
if user_input == "a" and no==2:
        number_3=0
        number_4=0
        number_5=0
if user_input == "a" and no==3:
        number_4=0
        number_5=0
if user_input == "a" and no==4:
        number_5=0
if user_input == "s" and no==2:
        number_3=0
        number_4=0
        number_5=0
if user_input == "s" and no==3:
        number_4=0
        number_5=0
if user_input == "s" and no==4:
        number_5=0
if user_input == "m" and no==2:
        number_3=1
        number_4=1
        number_5=1
if user_input == "m" and no==3:
        number_4=1
        number_5=1
if user_input == "m" and no==4:
        number_5=1
if user_input == "d" and no==2:
        number_3=1
        number_4=1
        number_5=1
if user_input == "d" and no==3:
        number_4=1
        number_5=1
if user_input == "d" and no==4:
        number_5=1
if user_input == "a":
    output = number_2 + number_1+ number_3+ number_4+ number_5
    print(output)
    print("addition is performed")
elif user_input == "s":
    output = number_2 - number_1-number_3- number_4- number_5
    print(output)
    print("subtraction is performed")
elif user_input == "m":
    output = number_2 * number_1* number_3* number_4* number_5
    print(output)
    print("multiplication is performed")
elif user_input == "d":
    output = number_1 / number_2/ number_3/ number_4/ number_5
    print(output)
    print("division is performed")
elif user_input == "q":
    output = number_2 ** number_1
    print(output)
    print("exponent  is performed")

else:
    print ("invalid entry")




