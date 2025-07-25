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
    
question_count = 5
score = 0
time_limit = 20
for i in range(question_count):
    try:
        start_time = time.time()
        answer = generate_question()
        user_answer = float(input("Your answer: "))
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < time_limit:
            if user_answer == answer:
                score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {answer}.")
        else:
            print("Time's up! You took too long to answer.")
        print(f"Your current score is: {score}")
    
    except:
        print("Invalid input. Please enter a number.")
        continue

  
