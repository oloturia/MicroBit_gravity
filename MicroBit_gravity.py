from microbit import *

accel = 50
dot_x = 3
dot_y = 3

while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    gesture = accelerometer.current_gesture()
    if (reading_x > accel):
        dot_x +=1
        if (dot_x > 4):
            dot_x = 4
    if (reading_x < accel*-1):
        dot_x -=1
        if (dot_x < 0):
            dot_x = 0
    if (reading_y > accel):
        dot_y +=1
        if (dot_y > 4):
            dot_y = 4
    if (reading_y < accel*-1):
        dot_y -=1
        if (dot_y < 0):
            dot_y = 0
    i=0
    string = ""
    while (i<=5):
        
        if (i != dot_y):
            string = string+"00000:"
        else:
            i2 = 0
            while (i2 <= 5):
                if (i2 != dot_x):
                    string = string+"0"
                else:
                    string = string+"9"
                i2 +=1
            string = string+":"    
        i +=1
    display.show(Image(string),delay=400)
