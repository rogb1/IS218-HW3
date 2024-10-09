'''My Calculator Test'''
from faker import Faker
from calculator import Calculator
import pytest
fake = Faker()

def test_addition():
    '''Test that addition function works '''    
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    ex_result = a + b
    assert Calculator.add(a,b)== ex_result

def test_subtraction():
    '''Test that addition function works '''
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=a)# Ensure b <= a to avoid negative numbers
    ex_result = a - b
    assert Calculator.subtract(a, b) == ex_result

def test_multiply():
    '''Test that Multiply function works'''
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    ex_result = a * b
    assert Calculator.multiply(a, b) == ex_result

def test_divide():
    '''Test that division function works'''
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    ex_result = a / b
    assert Calculator.divide(a, b) == ex_result

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(fake.random_int(min=1, max=100), 0)