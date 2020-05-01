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

#Setup PWM
GPIO.output(BUZZ, True)

# GPIO 18 for PWM with 20Hz
pwm = GPIO.PWM(BUZZ, 20)

#Initialisation
pwm.start(1)

def change_freq(dist):
    int(dist)
    if (dist <= 5):
        pwm.ChangeFrequency(3)
    elif (dist <= 10):
        pwm.ChangeFrequency(2.5)
    elif (dist <= 15):
        pwm.ChangeFrequency(2)
    elif (dist <= 20):
        pwm.ChangeFrequency(1.5)
    else:
        pwm.ChangeFrequency(1)


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
        
        #change the frequency by the distance
        change_freq(distance)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
