from app.commands import Command
from decimal import Decimal, InvalidOperation

class MultiplyCommand(Command):
    def execute(self,args):
        if len(args) != 2:
            print("Usage: <operation> <number1> <number2>")
            return
        a, b = args
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            print(a_decimal * b_decimal)
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e: # Catch-all for unexpected errors
            print(f"An error occurred: {e}")