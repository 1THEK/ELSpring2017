import RPi.GPIO as GPIO
import os
import time
import datetime
import glob
import MySQLdb
import Adafruit_DHT
import random
import json
from collections import defaultdict
from time import strftime
#EL Spring 2017 Project
#Group Members: Jason Goodman, Karen Ho, Kevyn Martinez
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor = '/sys/bus/w1/devices/w1_bus_master1/XX-XXXXXX/w1_slave' #Look into /sys/bus/w1/devices for your temperature probe
GPIO.setmode(GPIO.BCM)

moisture = 2
pin = 17
times = defaultdict(int)
shouldBreak = True
GPIO.setup(pin, GPIO.IN)
GPIO.setup(24,GPIO.OUT)
 
#Connects to the database
#IMPORTANT: Change the host, user, password, and db values to reflect your setup
db = MySQLdb.connect(host="localhost", user="root",passwd="password", db="some_database")
cur = db.cursor()

#This method reads in the current temperature from the temperature probe
#This method only utilizes the temperature probe, not the DHT_22 sensor
def tempRead():
    t = open(temp_sensor, 'r')
    lines = t.readlines()
    t.close()
 
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string)/1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
    return round(temp_f,1)

#Runs the motor
def run(t):
        GPIO.output(24,True)
        time.sleep(times[t])
        GPIO.output(24,False)

#Initializes the values for the motor
def init_Dict():
        for x in range(10):
                times[x] = x
                

#'1' indicates that there is no moisture
#'0' indicates that there is moisture.
#This method simply returns what the moisture sensor is currently detecting                
def getMoisture(pin):
    global moisture
    moisture = GPIO.input(pin)
    
def updateJSONFile(): #Reads and writes a count variable to a JSON file
    with open('count.json', "r") as data_file:    
        data = json.load(data_file)
        if moisture == 1:
            data["count"] = data["count"] + 1 #If moisture returns 1, add to count
            
        if data["count"] >= 3: #If count is greater than or equal to 3, turn on the motor
            init_Dict()
            run(3)

    with open("count.json", "w") as data_file:
        json.dump(data, data_file)

#This is responsible for inserting the values into the table of your local MySQL database
#Please rename 'some_Log' to whatever your named your table as 
def insertSQL(datetimeWrite,temp,humidity,moisture):
    sql = ("""INSERT INTO some_Log (datetime, temperature, humidity, moisture) VALUES (%s,%s,%s,%s)""",(datetimeWrite,temp,humidity,moisture))
    try:
        print "Writing to database..."
        cur.execute(*sql)
        db.commit()
        print "Write Complete"
        
    except:
        db.rollback()
        print "Failed writing to database"
 
    cur.close()
    db.close()


def Main():
    temp = tempRead()
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S")) #Reads time and date
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, '22') #Reads from DHT22 Sensor
    GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300) # Tells us when the pin goes HIGH or LOW
    GPIO.add_event_callback(pin, getMoisture) #when there is a change on the pin, run this function
    getMoisture(pin) #Returns moisture status
    print temp
    print datetimeWrite
    print humidity
    print moisture
    insertSQL(datetimeWrite,temp,humidity,moisture) #Inserts into MySQL
    updateJSONFile() #Updates the status of "count"
 
while True:

    Main()
    GPIO.cleanup() #Cleans up the GPIO pins
    if shouldBreak: #If true, the program will break. False the program will continue running (not recommended)
        break
    

