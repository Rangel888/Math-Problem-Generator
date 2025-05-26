from machine import Pin
import utime
import random as r
import ujson

problem_list = []
problem_answers = []

# Load configs
with open('application.json', 'r') as f:
    config = ujson.load(f)


def toggle_red_light():
    led1.toggle()
    utime.sleep(2)
    led1.toggle()  


def toggle_green_light():
    led2.toggle()
    utime.sleep(2)
    led2.toggle()

# Initialize lights
led1 = Pin(28, Pin.OUT)
led2 = Pin(22, Pin.OUT)
led1.low()
led2.low()

print("------------Welcome to the math problem generator------------")