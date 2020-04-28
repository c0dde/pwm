import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

BUZZ = 18
TRIG = 23
ECHO = 24

#HC-SR04
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Buzzer
GPIO.setup(BUZZ,GPIO.OUT)


#This function takes distance as a prarmeter, and perform
#corresponding speed of sound

def beep(dist):
    int(dist)
    
    t_end = time.time() + 2.1
    while time.time() < t_end:

        
        if (dist <= 5):
            GPIO.output(BUZZ,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(BUZZ,GPIO.LOW)
            time.sleep(0.1)

        elif (dist <= 10):
            GPIO.output(BUZZ,GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(BUZZ,GPIO.LOW)
            time.sleep(0.2)
            
        elif (dist <= 15):
            GPIO.output(BUZZ,GPIO.HIGH)
            time.sleep(0.4)
            GPIO.output(BUZZ,GPIO.LOW)
            time.sleep(0.4)
            
        elif (dist <= 20):
            GPIO.output(BUZZ,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(BUZZ,GPIO.LOW)
            time.sleep(0.5)
            
        else:
            GPIO.output(BUZZ,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(BUZZ,GPIO.LOW)
            time.sleep(1)


try:
    while True:
        print ("Distance Measurement In Progress")
        GPIO.output(TRIG, False)
        time.sleep(0.01)
        GPIO.output(TRIG, True)
        time.sleep(0.01)
        GPIO.output(TRIG, False)

        #Get the output and input time
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()    

        #Calculate the duration that the ultrasonic come back to the device   
        pulse_duration = pulse_end - pulse_start
        #Distance = 17150 * time
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print ("Distance:",distance,"cm")

        #Call the beep function by passing the distance to it.
        beep(distance)

except KeyboardInterrupt:
    GPIO.cleanup()



