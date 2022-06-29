import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from datetime import date
from django.db import models
import os
from gpiozero import Servo
import  time
import asyncio 
servo1 = Servo(14)
servo2 = Servo(15)
Delay = 0.1

#os.system('cd  ../mjpg-streamer/mjpg-streamer-experimental/  && ./start.sh ')
#await Stream();
#os.system('pwd && ./start.sh')
def index(request):
    print("hi");
#    Stream();
    servo1.value = -0.2
    servo2.value = -0.2
    return render(request,"index.html")

def send(request):
    tasks = request.GET.getlist('tasks[]')
    Key_pressed = int(tasks[0])
    print(Key_pressed)
    if (Key_pressed == 87):
        servo1.value = 0.5
        servo2.value = 0.7
        time.sleep(Delay)
        servo1.value = -0.2
        servo2.value = -0.2
        Key_pressed =0;
	#Key_pressed =0;

    elif (Key_pressed == 68):
        servo1.value = 0.5
        servo2.value = -0.7
        time.sleep(Delay)
        servo1.value = -0.2
        servo2.value = -0.2
        Key_pressed =0;
	#Key_pressed =0;
        
    elif (Key_pressed == 65):
        servo1.value = -0.5
        servo2.value = 0.7
        time.sleep(Delay)
        servo1.value = -0.2
        servo2.value = -0.2
        Key_pressed =0;
	#Key_pressed =0;
        
    elif (Key_pressed == 83):
        servo1.value = -0.5
        servo2.value = -0.5
        time.sleep(Delay)
        servo1.value = -0.2
        servo2.value = -0.2
        Key_pressed =0;
	#Key_pressed =0;
        
    else :
        servo1.value = -0.2
        servo2.value = -0.2
        time.sleep(Delay)
        servo1.value = -0.2
        servo2.value = -0.2
        Key_pressed =0;
    	#Key_pressed =0; 
    
    return HttpResponse('Success')


'''
    print("Start \n")
    # print(dir(request.GET.get))
    # print(request.GET.get)
    keyPressed = request.GET.get('Key') # voting id number is brought in as var
    #v = Entry.objects.get(pk=voting_id) # get by voting id var
    print("End \n \n ")

    print("Request Happend")
    return HttpResponse("Done") # Only on console
'''
    
