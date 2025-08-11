import random as r
import ujson
from hardware import toggle_red_light, toggle_green_light

problem_list = []
problem_answers = []

# Load configs from JSON
with open('application.json', 'r') as f:
    config = ujson.load(f)


def select_operation():
    print("\nWhat would you like to work on?\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    user_input = input("Enter an option (1-4) from above: ").strip()
    print()

    if user_input == "1":
        return "addition"
    elif user_input == "2":
        return "subtraction"
    elif user_input == "3":
        return "multiplication"
    elif user_input == "4":
        return "division"
    else:
        print("Invalid choice. Defaulting to 'addition'.")
        return "addition"

def load_problems(problem_list, problem_answers, operation, number_of_problems):
    for _ in range(number_of_problems):
        temp1 = r.randint(1,20)
        temp2 = r.randint(1,20)
        num1 = max(temp1, temp2)
        num2 = min(temp1, temp2)

        if operation == "addition":
            problem = f"{num1} + {num2} = "
            answer = num1 + num2
        elif operation == "subtraction":
            problem = f"{num1} - {num2} = "
            answer = num1 - num2
        elif operation == "multiplication":
            problem = f"{num1} * {num2} = "
            answer = num1 * num2
        else:
            while num1 % num2 != 0:
                num2 = r.randint(1, 10)
            problem = f"{num1} / {num2} = "
            answer = num1 / num2
        
        problem_list.append(problem)
        problem_answers.append(answer)
        
def main():

    print("------------Welcome to the Math Problem Generator----------")


main()
