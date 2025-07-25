import random
import time

def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*', '/'])
    print(f"Question: What is {number1} {operation} {number2}?")
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        return number1 / number2
    else:
        raise ValueError("Unknown operation")
    