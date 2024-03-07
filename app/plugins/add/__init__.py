import logging
from app.commands import Command
from decimal import Decimal, InvalidOperation

class AddCommand(Command):
    def operation(self,a,b):
        return a + b
    def reiterateList(self,arr):
        result = arr[0]
        while len(arr) != 1:
            try:
                result = self.operation(result,arr[1])
                arr = arr[1:]
            except:
                return Exception
        return result
    def execute(self,args):
        try:
            argList = list(map(Decimal, args))
            res = self.reiterateList(argList)
            print(res)
            logging.info("Command 'add' executed with arguments: " + str(args) + " and returned value \"" + str(res) + "\"")
        except InvalidOperation:
            string = "["
            for i in range(len(args)):
                string += "\"" + args[i] + "\""
                if (i < len(args)-1):
                    string += ", "
            string += "]"
            print(f"Invalid number input: {string} does not include valid numbers.")
            logging.info("Command 'add' error: " + f"Invalid number input: {string} does not include valid numbers.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
            logging.info("Command 'add' error: " + "Error: Division by zero.")
        except Exception as e: # Catch-all for unexpected errors
            print(f"An error occurred: {e}")
            logging.info("Command 'add' error: " + f"An error occurred: {e}")
