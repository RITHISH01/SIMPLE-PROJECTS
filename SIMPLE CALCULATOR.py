import math
#*************************************simple calculator project***********************************************
#MENU
print("SELECT OPERATION TO PERFORM:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.SQUARE ROOT")
print("6:RAISE TO POWER")
#GETTING THE DESIRED OPERATION FROM THE USER
operation=input()

if operation=="1":#PERFORM ADDITION
    num1=int(input("ENTER THE FIRST NUMBER:"))
    num2=int(input("ENTER THE SECOND NUMBER:"))
    print("THE SUM IS: "+str(int(num1)+int(num2)))
elif operation=="2":#PERFORM SUBTRACTION
    num1 = int(input("ENTER THE FIRST NUMBER:"))
    num2 = int(input("ENTER THE SECOND NUMBER:"))
    print("THE DIFFERENCE IS: "+str(int(num1)-int(num2)))
elif operation=="3":#PERFORM MULTIPLICATION
    num1 = int(input("ENTER THE FIRST NUMBER:"))
    num2 = int(input("ENTER THE SECOND NUMBER:"))
    print("THE PRODUCT IS: "+str(int(num1)*int(num2)))
elif operation=="4":#PERFORM DIVISON
    num1 = int(input("ENTER THE FIRST NUMBER:"))
    num2 = int(input("ENTER THE SECOND NUMBER:"))
    print("THE RESULT IS: "+str(int(num1)/int(num2)))
elif operation=="5":#PERFORM SQUARE ROOT
    num= int(input("ENTER THE NUMBER:"))
    print("THE SQAURE ROOT OF THE NUMBER IS %f: " %(math.sqrt(num)))
elif operation=="6":#SQUARE A NUMBER
    num= int(input("ENTER THE NUMBER:"))
    print("THE RESULT IS: %d " %(pow(num,2)))
else:
    print("invalid entry")
