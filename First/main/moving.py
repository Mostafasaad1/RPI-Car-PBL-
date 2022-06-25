from gpiozero import Servo
from time import sleep 

servo1 = Servo(3)
servo2 = Servo(2)


def Forward():
    #Forward Action 
    servo1.value = 0.5
    servo2.value = -0.7
    return

def Backward():
    #Backward Action 
    servo1.value = -0.5
    servo2.value = 0.1
    return

def Right():
    #Right Action   
    servo1.value = -0.5
    servo2.value = -0.7
    return

def Left():
    #left Action 
    servo1.value = 0.5
    servo2.value = 0.7
    return

def Stop():
    servo1.value = -0.2
    servo2.value = -0.2
    return

    