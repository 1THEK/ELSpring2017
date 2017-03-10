#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys
""" Log Current Time, Temperature in Celsius and Fahrenheit
 To an Sqlite3 database """
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-051692206bff/w1_slave")
	tempfile_text = tempfile.read()
	currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	print [currentTime, tempC, tempF]
	return [currentTime, tempC, tempF]
def logTemp():
	con = mydb.connect('temperature.db')
	with con:
		try:
			[t,C,F]=readTemp()
			print "Current temperature is: %s F" %F
			cur = con.cursor()
			cur.execute('CREATE TABLE IF NOT EXISTS TempData(Time TEXT, Cel REAL, Far REAL)')
			#sql = "insert into TempData values(?,?,?)"
			print "Still works"
			cur.execute('insert into TempData values(?,?,?)', (t,C,F))
			print "Temperature logged"
		except:
			print "Error!!"


con = mydb.connect('temperature.db')
with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS TempData")

#loop for 10 min
for x in range(20):
	logTemp() #log temp
	time.sleep(30) #wait 30 seconds

#create csv file
f = open("data.csv","w")

con = mydb.connect('temperature.db')
with con:
	cur = con.cursor()
	cur.execute('SELECT * FROM TempData')
	rows = cur.fetchall()
	for row in rows:
		f.write(','.join([str(x) for x in row]))
		f.write('\n')
	#[f.write(','.join(row)) for row in rows]
f.close()
