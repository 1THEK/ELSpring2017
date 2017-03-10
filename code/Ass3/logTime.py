#!/usr/bin/python
import datetime
import time
import sys
import sqlite3 as mydb

def logTime(cur):
"""Function that gets the current date and time. The function will then log
   it into a table in the format (Date, Time)."""
 	t = time.localtime() #Get Local Time
	#The next step is broken down as follows:
	# 1) loop thru t list. the first 3 are the year, month and day.
	# 2) iterate and convert each element into a string. join the list with '-'
	# 3) repeat for elements [3,4,5] (hour, min, seconds
	xdate,xtime = ['-'.join([str(x) for x in t][0:3]),'-'.join([str(x) for x in t][3:6])]
	#Insert into table
	cur.execute("INSERT INTO tb VALUES(?,?)", [xdate,xtime])

#Connect to database
con = mydb.connect('testTime.db')

with con:
    cur = con.cursor()
    #Create table if does not exist otherwise continue
    cur.execute("CREATE TABLE IF NOT EXISTS tb(Date TEXT, Time TEXT)")
    # Loop for 10 minutes writing every 30 seconds
    for x in range(20):
        time.sleep(30)
        logTime(cur)
