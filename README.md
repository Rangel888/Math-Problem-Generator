# Math-Problem-Generator

## Purpose
This project is a math problem generator for the Rasberry PI Pico W that uses LEDs and sounds to create an interactive learning experience. 

The game focuses on practicing addition, subtraction, multiplication, and division through repitition. Using LEDs and sounds provides immdiate feedback, allowing kids to learn and practice without the need for constant supervision. 

## Set Up
### Required Hardware

- Rasberry PI Pico W
- Breadboard
- Micro USB
- 2 LED lights (Green, Red)
- Resistors 

### Required Software
## Configuration

This project uses a JSON file `user_settings.json` to store custom settings like LED pins

```json
{   
    "numberOfProblems" : 5,
    "useDivisionRemainders" : true

}
```