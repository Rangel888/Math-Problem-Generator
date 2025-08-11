from machine import Pin
import utime

led1 = Pin(28, Pin.OUT)
led2 = Pin(22, Pin.OUT)
led1.low()
led2.low()

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