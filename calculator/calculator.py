#Todo: Implement trigonometric operations in higher_level_op.py
#Todo: Implement errors
#Todo: Implement a better UI
#Todo: Implement unit tests (where needed)
#Todo: Implement zecimals for better precision in division, logarithm and others


from basic_op import Calculator
from higher_level_op import AdvancedCalculator, TrigonometricOperations


def main():
    # Template for UI
    print("=" * 50)
    print("Simple Calculator".center(50))
    print("=" * 50)
    print('\n')

    calc = Calculator()
    adv_calc = AdvancedCalculator()

    while True:
        print("Do you want to perform basic or advanced operations?")
        print("A. Advanced Operations")
        print("B. Basic Operations")
        print("x. Exit")

        choice = input("Select an option (A/B/x): ").strip().lower()
        if choice == 'x':
            print("Thank you for using the calculator!")
            break

        if choice not in ['a', 'b']:
            print("Invalid choice! Please try again.")
            continue

        if choice == 'b':
            while True:
                print("\nOperations:")
                print("1. Addition (+)")
                print("2. Subtraction (-)")
                print("3. Multiplication (*)")
                print("4. Division (/)")
                print("5. Power (^)")
                print("6. Modulo (%)")
                print("0. Exit")

                op_choice = input("\nSelect operation (0-6): ").strip()

                if op_choice == '0':
                    break

                if op_choice not in ['0', '1', '2', '3', '4', '5', '6']:
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

                    operation, symbol = operations[op_choice]
                    result = operation(num1, num2)

                    print(f"\nResult: {num1} {symbol} {num2} = {result}")

                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

        elif choice == 'a':
            while True:
                print("\nAdvanced Operations:")
                print("1. Square Root")
                print("2. Logarithm")
                print("3. Factorial")
                print("4. Do you want to perform trigonometric operations?")
                print("0. Exit")

                adv_choice = input("\nSelect operation (0-4): ").strip()

                if adv_choice == '0':
                    break

                try:
                    if adv_choice == '1':
                        value = float(input("Enter a number: "))
                        result = adv_calc.square_root(value)
                    elif adv_choice == '2':
                        value = float(input("Enter a number: "))
                        base_input = input("Enter the base (default 10): ").strip()
                        base = float(base_input) if base_input else 10
                        result = adv_calc.logarithm(value, base)
                    elif adv_choice == '3':
                        n = int(input("Enter a non-negative integer: "))
                        result = adv_calc.factorial(n)
                    elif adv_choice == '4':
                        trig_calc = TrigonometricOperations()
                        print("\nTrigonometric Operations:")
                        print("a. Sine")
                        print("b. Cosine")
                        print("c. Tangent")
                        print("d. Cotangent")
                        print("e. Arcsine")
                        print("f. Arccosine")
                        print("g. Arctangent")

                        trig_choice = input("\nSelect operation (a-g): ").strip().lower()

                        angle = float(input("Enter angle in radians: "))

                        if trig_choice == 'a':
                            result = trig_calc.sine(angle)
                        elif trig_choice == 'b':
                            result = trig_calc.cosine(angle)
                        elif trig_choice == 'c':
                            result = trig_calc.tangent(angle)
                        elif trig_choice == 'd':
                            result = trig_calc.cotangent(angle)
                        elif trig_choice == 'e':
                            result = trig_calc.asin(angle)
                        elif trig_choice == 'f':
                            result = trig_calc.acos(angle)
                        elif trig_choice == 'g':
                            result = trig_calc.atan(angle)
                        else:
                            print("Invalid choice! Please try again.")
                            continue

                    else:
                        print("Invalid choice! Please try again.")
                        continue

                    print(f"\nResult: {result}")

                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
