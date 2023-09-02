class ArithmeticCalculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

    def floor_division(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a // b

    def modulo(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a % b

    def exponentiation(self, a, b):
        return a ** b

calculator = ArithmeticCalculator()

while True:
    print("Select an operation:\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Floor Division\n"
          "6. Modulo\n"
          "7. Exponentiation\n"
          "8. Exit")
    print(10*"*")
    option = int(input("Enter your option: "))
    print(10*"*")
    if option == 8:
        print("Thanks for using my calculator application")
        break
    
    if option in range(1, 8):
        a = eval(input("Enter first number: "))
        b = eval(input("Enter second number: "))
        
        if option == 1:
            result = calculator.addition(a, b)
        elif option == 2:
            result = calculator.subtraction(a, b)
        elif option == 3:
            result = calculator.multiplication(a, b)
        elif option == 4:
            result = calculator.division(a, b)
        elif option == 5:
            result = calculator.floor_division(a, b)
        elif option == 6:
            result = calculator.modulo(a, b)
        elif option == 7:
            result = calculator.exponentiation(a, b)
        print(10*"*")
        print("Result:", result)
        print(10*"*")
    else:
        print(10*"*")
        print("Invalid Option")
        print(10*"*")
