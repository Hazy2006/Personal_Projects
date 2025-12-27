"""
Simple Calculator Application
A command-line calculator that performs basic arithmetic operations.
"""


class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def power(self, a, b):
        """Raise a to the power of b."""
        return a ** b
    
    def modulo(self, a, b):
        """Return the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero!")
        return a % b


def main():
    """Main function to run the calculator."""
    calc = Calculator()
    
    print("=" * 50)
    print("Simple Calculator".center(50))
    print("=" * 50)
    
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Modulo (%)")
        print("7. Exit")
        
        choice = input("\nSelect operation (1-7): ").strip()
        
        if choice == '7':
            print("Thank you for using the calculator!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            operations = {
                '1': (calc.add, '+'),
                '2': (calc.subtract, '-'),
                '3': (calc.multiply, '*'),
                '4': (calc.divide, '/'),
                '5': (calc.power, '^'),
                '6': (calc.modulo, '%')
            }
            
            operation, symbol = operations[choice]
            result = operation(num1, num2)
            
            print(f"\nResult: {num1} {symbol} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
