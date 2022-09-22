print("Welcome to ND22 Calculator")
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

    if command == "!add":
        num1 = input("Enter a number: ")
        print(" ")
        num2 = input("Enter another number: ")
        result = float(num1) + float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)
        
    if command == "!subtract":
        num1 = input("Enter a number: ")
        print(" ")
        num2 = input("Enter another number: ")
        result = float(num1) - float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)
        
    if command == "!multiply":
        num1 = input("Enter a number: ")
        print(" ")
        num2 = input("Enter another number: ")
        result = float(num1) * float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)
        
    if command == "!divide":
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
        result = float(num1) / float(num2)
        
        print(" ")
        print("Answer is...")
        print(result)
       
        
    else:
        print(" ")
