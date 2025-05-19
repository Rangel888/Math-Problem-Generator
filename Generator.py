from machine import Pin
import utime
import random as r
import ujson

problem_list = []

problem_answers = []

with open('application.json', 'r') as f:
    config = ujson.load(f)
