import random
import math
import numpy as np


# ---------------------------
# Function 1: Generate Question
# ---------------------------
def generate_question():
    operations = ["add", "subtract", "multiply", "sqrt", "power", "factorial"]
    operation = random.choice(operations)

    if operation == "add":
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        question = f"What is {a} + {b}? "
        answer = a + b

    elif operation == "subtract":
        a = random.randint(10, 30)
        b = random.randint(1, 10)
        question = f"What is {a} - {b}? "
        answer = a - b

    elif operation == "multiply":
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        question = f"What is {a} × {b}? "
        answer = a * b

    elif operation == "sqrt":
        a = random.randint(1, 15)
        question = f"What is the square root of {a*a}? "
        answer = math.sqrt(a*a)

    elif operation == "power":
        a = random.randint(1, 5)
        b = random.randint(2, 3)
        question = f"What is {a} to the power of {b}? "
        answer = math.pow(a, b)

    elif operation == "factorial":
        a = random.randint(1, 6)
        question = f"What is {a}! ? "
        answer = math.factorial(a)

    return question, answer


# ---------------------------
# Function 2: Check Answer
# ---------------------------
def check_answer(user_answer, correct_answer):
    try:
        if float(user_answer) == float(correct_answer):
            return True
        else:
            return False
    except:
        return False


# ---------------------------
# Function 3: Display Results
# ---------------------------
def display_results(scores_array):
    print("\n--- Quiz Results ---")

    total_questions = len(scores_array)
    total_correct = np.sum(scores_array)
    percentage = (total_correct / total_questions) * 100

    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {total_correct}")
    print(f"Average Score: {np.mean(scores_array)}")
    print(f"Highest Score: {np.max(scores_array)}")
    print(f"Lowest Score: {np.min(scores_array)}")
    print(f"Percentage: {percentage:.2f}%")


# ---------------------------
# Main Program
# ---------------------------
def main():
    print("Welcome to the Maths Challenge Quiz!")
    num_questions = int(input("How many questions would you like? "))

    scores = []

    for i in range(num_questions):
        question, correct_answer = generate_question()
        user_answer = input(f"\nQuestion {i+1}: {question}")

        if check_answer(user_answer, correct_answer):
            print("Correct!")
            scores.append(1)
        else:
            print(f"Wrong! The correct answer was {correct_answer}")
            scores.append(0)

    scores_array = np.array(scores)
    display_results(scores_array)


main()
