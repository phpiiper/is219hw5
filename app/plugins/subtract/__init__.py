import logging
from app.commands import Command
from decimal import Decimal, InvalidOperation

class SubtractCommand(Command):
    def operation(self,a,b):
        return a - b
    def reiterateList(self,list):
        result = list[0]
        while len(list) != 1:
            try:
                result = self.operation(result,list[1])
                list = list[1:]
            except:
                return Exception
        return result
    def execute(self,args):
        try:
            argList = list(map(Decimal, args))
            res = self.reiterateList(argList)
            print(res)
            logging.info("Command 'subtract' executed with arguments: " + str(args) + " and returned value \"" + str(res) + "\"")
        except InvalidOperation:
            string = "["
            for i in range(len(args)):
                string += "\"" + args[i] + "\""
                if (i < len(args)-1):
                    string += ", "
            string += "]"
            print(f"Invalid number input: {string} does not include valid numbers.")
            logging.info("Command 'subtract' error: " + f"Invalid number input: {string} does not include valid numbers.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
            logging.info("Command 'subtract' error: " + "Error: Division by zero.")
        except Exception as e: # Catch-all for unexpected errors
            print(f"An error occurred: {e}")
            logging.info("Command 'subtract' error: " + f"An error occurred: {e}")