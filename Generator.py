from machine import Pin
import utime
import random as r
import ujson

problem_list = []
problem_answers = []

# Initialize lights
led1 = Pin(28, Pin.OUT)
led2 = Pin(22, Pin.OUT)
led1.low()
led2.low()

# Load configs from JSON
with open('application.json', 'r') as f:
    config = ujson.load(f)

# Toggle incorrect light
def toggle_red_light():
    led1.toggle()
    utime.sleep(2)
    led1.toggle()  

# Toggle correct light
def toggle_green_light():
    led2.toggle()
    utime.sleep(2)
    led2.toggle()
    
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

def main():

    print("------------Welcome to the Math Problem Generator----------")


main()
