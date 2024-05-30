

print("calculator")

firstNumber = int(input("Enter your second number "))

secondNumber = int(input("Enter your second number "))


isOkay = True
while(isOkay):
    print("+ - * /")
    operation = input("Enter your chosesn operation \n")
    sum =0
    if operation == "+":
        sum = firstNumber + secondNumber
        isOkay = False
    elif operation == "-":
        sum = firstNumber - secondNumber
        isOkay = False
    elif operation == "*":
        sum = firstNumber * secondNumber
        isOkay = False
    elif operation == "/":
        sum = firstNumber / secondNumber  
        isOkay = False
    else:
        print("just choose in the following operation started")


print(str(firstNumber) + operation + str(secondNumber) + " = " + str(sum) ) 