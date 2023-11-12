import random

def function_A(minimum, maximum):
    """
    Returns a Random integer between minimum and maximum.
    """
    return random.randint(int(minimum), int(maximum))

def function_B():
    """
    Returns a Random operator of the 3 given below.
    """
    return random.choice(['+', '-', '*'])

def function_C(number1, number2, operator):
    problem = f"{number1} {operator} {number2}" # problem
    """
    This function does the operation based on the operator used
    """
    if operator == '+':
        solution = number1 + number2
    elif operator == '-':
        solution = number1 - number2
    else:
        solution = number1 * number2
    return problem, solution

def math_quiz():
    score = 0 #your score
    total_questions = 3 # total number of questions
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    for _ in range(total_questions):
        num1 = function_A(1, 10); # we get a random number between 1 and 10
        num2 = function_A(1, 5.5); # we get a random number between 1 and 5.5
        oper = function_B() # perform a random operation
        PROBLEM, ANSWER = function_C(num1, num2, oper)
        print(f"\nQuestion: {PROBLEM}") # This is the problem
        useranswer = input("Your answer: ") # we give our solution here
        useranswer = int(useranswer)
        if useranswer == ANSWER: # we check if our solution is actually correct or not
            print("Correct! You earned a point.")
            score += -(-1) # if yes we get a point and our score increases by 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.") # if not we will get correct answer displayed
    print(f"\nGame over! Your score is: {score}/{total_questions}") # we print here the score out of number of questions i.e, 3

if __name__ == "__main__":
    math_quiz()
