from app.commands import Command
from calculator.operations import divide
from calculator.calculation import Calculation
from decimal import Decimal, InvalidOperation

class DivCommand(Command):
    def __init__(self):
        pass

    def execute(self, *args):
        try: 
            if len(args) != 2:
                raise ValueError("You must provide 2 arguments.")
            a = Decimal(args[0])
            b = Decimal(args[1])

            calculation = Calculation.create(a, b, divide)
            result = calculation.perform()
            print(f"Result: {result}")

        except(ValueError, IndexError, InvalidOperation):
            print("Invalid input, provide two valid numbers")