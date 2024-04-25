#https://github.com/BerkeGulmen/RoboticProjects/TemperatureLimiter.py
from microbit import *

a = 1
b = 27
c = ''
while True :
    if button_a . was_pressed () :
        b = b + 1
        
    if button_b . was_pressed () :
        b = b - 1
    
    if a == 1 :
        a = 0
        if temperature () > b :
            pin0 . write_digital (1)
            pin1 . write_analog (1023)
            c = temperature ()
            #display . scroll (c)
            #sleep (100)
            c = '+'
            c += str (temperature () - b)
            display . scroll (c)
        print ('Limit: ' , b, '    Now: ', temperature ())
        sleep (300)
        
    else :
        a = 1
        pin0 . write_digital (0)
        pin1 . write_analog (0)
        c = temperature ()
        #display . scroll (c)
        #sleep (100)
        c = str (temperature () - b)
        display . scroll (c)
        print ('Limit: ' , b, '    Now: ', temperature ())
        sleep (300)
