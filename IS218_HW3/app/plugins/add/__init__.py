#add plugins in a different branch and then merge them into the main
from app.commands import Command
from calculator.operations import add
from calculator.calculation import Calculation
from decimal import Decimal, InvalidOperation

class AddCommand(Command):
    def __init__(self):
        pass
    def execute(self, *args):
        try: 
            if len(args) != 2:
                raise ValueError("You must provide 2 arguments.")
            a = Decimal(args[0])
            b = Decimal(args[1])

            calculation = Calculation.create(a, b, add)
            result = calculation.perform()
            print(f"Result: {result}")

        except(ValueError, IndexError, InvalidOperation):
            print("Invalid input, provide two valid numbers")