import random as r
from hardware import toggle_red_light, toggle_green_light
from input_utils import normalize_remainder_input
from configs import Config

problem_list = []
problem_answers = []

config = Config('user_settings.json')

def select_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter 1, 2, or 3: ").strip()
    print()

    if choice == "1":
        return "easy"
    elif choice == "2":
        return "medium"
    elif choice == "3":
        return "hard"
    else:
        print("Invalid choice. Defaulting to 'easy'.")
        return "easy"
    
def select_mode():
    print("\nSelect a mode:\n")
    print("1. Free Play (focus on one subject)")
    print("2. Random Mode (mix of all subjects +, -, *, /)")

    choice = input("Enter 1 or 2: ").strip()
    print()
    
    if choice == "1":
        return "free"
    elif choice == "2":
        return "random"
    else:
        print("Invalid choice. Defaulting to Free Play.")
        return "free"
    
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

def load_problems(problem_list, problem_answers, operation, mode, difficulty):

    operations = ['addition', 'subtraction', 'multiplication', 'division']
    for _ in range(config.number_of_problems):

        operation = operation if mode == "free" else operations[r.randint(0, len(operations) - 1)]

        # Determine number range
        if (config.custom_ranges_enabled and mode == "free" and config.custom_range_operation == operation):
            range_min = config.custom_range_min
            range_max = config.custom_range_max
        else:
            range_min = config.difficulty_levels[difficulty][operation]["min"]
            range_max = config.difficulty_levels[difficulty][operation]["max"]

        temp1 = r.randint(range_min, range_max)
        temp2 = r.randint(range_min, range_max)
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
            if config.use_division_remainders:
                # Find all divisors of num1
                divisors = [i for i in range(1, num1 + 1)]
            else: 
                # Find all divisors of num1 with no remainder
                divisors = [i for i in range(1, num1 + 1) if num1 % i == 0]

            # Choose random divisor from list
            num2 = divisors[r.randint(0, len(divisors) - 1)]
            problem = f"{num1} / {num2} = "
            
            if num1 % num2 != 0:
                answer = f"{num1 // num2} r{num1 % num2}"
            else: 
                answer = num1 // num2
        
        problem_list.append(problem)
        problem_answers.append(answer)

def play_game():
    print("------------Welcome to the Math Problem Generator----------")

    problem_list.clear()
    problem_answers.clear()
    mode = select_mode()

    operation = None
    if mode == "free":
        operation = select_operation()
    difficulty = select_difficulty()

    load_problems(problem_list, problem_answers, operation, mode, difficulty)

    for i, problem in enumerate(problem_list):     

        user_answer = None
            
        # keep trying on same problem until right answer given
        while (user_answer != problem_answers[i]):
            raw_input = input(problem)

            if " / " in problem and "r" in raw_input.lower():
                user_answer = normalize_remainder_input(raw_input)
            else:
                try:
                    user_answer = int(raw_input)
                except ValueError:
                    print("Invalid input! Please enter a number")
                    continue

            if user_answer != problem_answers[i]:
                toggle_red_light()
                print("Wrong, Try again!")

        # Answer was correct 
        toggle_green_light()
        print("Correct!!!!!\n")

        
def main():

    while True:
        play_game()
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        
    print("Exiting game")


main()
