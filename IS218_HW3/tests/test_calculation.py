from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations():
    """
    Test calculation operations with specific scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operations
    for addition, subtraction, multiplication, and division.
    """

    # Test case 1: Subtraction
    calc = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calc.perform() == Decimal('5'), "Failed subtraction operation with 10 and 5"
    
    # Test case 2: Subtraction with decimals
    calc = Calculation(Decimal('10.5'), Decimal('0.5'), subtract)
    assert calc.perform() == Decimal('10.0'), "Failed subtraction operation with 10.5 and 0.5"

    # Test case 3: Multiplication with decimals
    calc = Calculation(Decimal('10.5'), Decimal('2'), multiply)
    assert calc.perform() == Decimal('21.0'), "Failed multiplication operation with 10.5 and 2"

    # Test case 4: Division with decimals
    calc = Calculation(Decimal('10'), Decimal('0.5'), divide)
    assert calc.perform() == Decimal('20'), "Failed division operation with 10 and 0.5"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    This test verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.