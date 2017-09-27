import RPi.GPIO as GPIO
import time 

IN1 = 11    # pin11  
IN2 = 12  
IN3 = 13  
IN4 = 15 

def setStep(w1, w2, w3, w4):  
    GPIO.output(IN1, w1)  
    GPIO.output(IN2, w2)  
    GPIO.output(IN3, w3)  
    GPIO.output(IN4, w4) 

def stop():  
    setStep(0, 0, 0, 0)  
  
def forward(delay, steps):    
    for i in range(0, steps):  
        setStep(1, 0, 0, 0)  
        time.sleep(delay)  
        setStep(0, 1, 0, 0)  
        time.sleep(delay)  
        setStep(0, 0, 1, 0)  
        time.sleep(delay)  
        setStep(0, 0, 0, 1)  
        time.sleep(delay)  
  
def backward(delay, steps):    
    for i in range(0, steps):  
        setStep(0, 0, 0, 1)  
        time.sleep(delay)  
        setStep(0, 0, 1, 0)  
        time.sleep(delay)  
        setStep(0, 1, 0, 0)  
        time.sleep(delay)  
        setStep(1, 0, 0, 0)  
        time.sleep(delay)  
		
def gc1loopmain():  
    while True:  
        print ("backward...")  
        backward(0.003, 512)  # 512 steps --- 360 angle  
          
        print ("stop...")  
        stop()                 # stop  
        time.sleep(3)          # sleep 3s  
          
        print ("forward...")  
        forward(0.005, 100)  
          
        print ("stop...")  
        stop()  
        time.sleep(3)

	print ("backing...")
	forward(0.005, 412)
	print ("over")
	time.sleep(0.1)
	
	break
	
def gc2loopmain():
    while True:
	print ("backword...")
	backward(0.003, 1024)
		
	print ("stop...")
	stop()
	time.sleep(3)
		
	print ("forward...")
	forward(0.005, 100)
		
	print ("stop...")
	stop()
	time.sleep(3)
		
	print ("backing...")
	forward(0.005, 924)
	print ("over")
	time.sleep(1)
		
        break
		
		