print("Welcome to ND22's MathB")
print(" ")
print("Possible commands:")
print("!add")
print("!subtract")
print("!multiply")
print("!divide")
print(" ")

while True:

    command = input("Command: ")
    print(" ")

    # Addition

    if command == "!add":
        num1 = input("Enter a number: ")
        print(" ")
        num2 = input("Enter another number: ")
        result = float(num1) + float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)

    # Subtraction
  
    if command == "!subtract":
        num1 = input("Enter a number: ")
        print(" ")
        num2 = input("Enter another number: ")
        result = float(num1) - float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)

    # Multiplication

    if command == "!multiply":
        num1 = input("Enter a number: ")
        print(" ")
        num2 = input("Enter another number: ")
        result = float(num1) * float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)
  
    # Division

    if command == "!divide":
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
        result = float(num1) / float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)
       
        
    else:
        print(" ")

