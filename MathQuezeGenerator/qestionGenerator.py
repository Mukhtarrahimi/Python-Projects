import random
import time

def select_difficulty():
    print("Select your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                return (1, 10)
            elif choice == 2:
                return (1, 100)
            elif choice == 3:
                return (1, 1000)
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        except:
            print("Invalid input. Please enter a number.")

def generate_question(min_val, max_val):
    number1 = random.randint(min_val, max_val)
    number2 = random.randint(min_val, max_val)
    operation = random.choice(['+', '-', '*', '/'])
    
    if operation == '/':
        while number2 == 0:
            number2 = random.randint(min_val, max_val)
    
    print(f"Question: What is {number1} {operation} {number2}?")
    
    if operation == '+':
        return round(number1 + number2, 2)
    elif operation == '-':
        return round(number1 - number2, 2)
    elif operation == '*':
        return round(number1 * number2, 2)
    elif operation == '/':
        return round(number1 / number2, 2)

min_val, max_val = select_difficulty()


question_count = 5
score = 0
time_limit = 20

for i in range(question_count):
    try:
        start_time = time.time()
        answer = generate_question(min_val, max_val)
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
