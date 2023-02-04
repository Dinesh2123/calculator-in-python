import math

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square root")
print("7. Logarithm")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    
    elif choice == '4':
        print(num1, "/", num2, "=", num1 / num2)
        
elif choice in ['5', '6', '7']:
    num = float(input("Enter number: "))
    
    if choice == '5':
        power = float(input("Enter power: "))
        print(num, "^", power, "=", pow(num, power))
    
    elif choice == '6':
        print("Square root of", num, "=", math.sqrt(num))
    
    elif choice == '7':
        log = float(input("Enter base of logarithm: "))
        print("log", log, "of", num, "=", math.log(num, log))
        
else:
    print("Invalid input")
