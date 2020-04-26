print("Welcome to the Simple Calculator")
num1 = input("Please enter your first number")
num2 = input("Please enter your second number")
Operation = input("Please select your operation : + - * /")
if Operation == "+" :
    print(float(num1) + float(num2))
elif Operation == "-" :
    print(float(num1) - float(num2))
elif Operation == "*" :
    print(float(num1) * float(num2))
elif Operation == "/" :
    if num1 == "0" :
        print(1)
    elif num2 == "0" :
        print("Infinity")
    else :
        print(float(num1) / float(num2))
else :
    print("Invalid Input. Please select the correct Input")

print("Thanks for using simple calculator")