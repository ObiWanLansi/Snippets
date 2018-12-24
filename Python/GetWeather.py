#!/usr/bin/python

import requests
import time;
import sqlite3
import xml.etree.ElementTree as ElementTree
import codecs

# Documentation:
# https://openweathermap.org/current
# https://openweathermap.org/price

url = "http://api.openweathermap.org/data/2.5/weather?q=Trier&units=metric&mode=xml&lang=de&APPID=<UUID>"
databasefile = "/var/www/html/openweather.db"
outputfile = "/var/www/html/openweather.xml"
content = ""

#------------------------------------------------------------------------------


def writeToFile():
    f = open(outputfile, "w")
    f.write(content)
    f.close()

#------------------------------------------------------------------------------


def createEmptyDatabase():
    db = sqlite3.connect(databasefile)   
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE OPENWEATHER (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, INSERTTIME TIMESTAMP NOT NULL, WEATHERTIME TIMESTAMP NOT NULL, CONTENT TEXT NOT NULL, MIN FLOAT NOT NULL, MAX FLOAT NOT NULL, TEMPERATURE FLOAT NOT NULL) """)
    db.close()


def appendToDatabase():
    
    xml = ElementTree.fromstring(content)
    
    #------------------------------------------------------

    current_time = time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time()))
    print ("CurrentTime: {0}".format(current_time ))

    last_update = xml.find("./lastupdate").attrib["value"]
    print ("LastUpdate : {0}".format(last_update))
    
    #------------------------------------------------------

    temperature = xml.find("./temperature").attrib["value"]
    print ("Temperature: {0}".format(temperature))

    min = xml.find("./temperature").attrib["min"]
    print ("Min        : {0}".format(min))

    max = xml.find("./temperature").attrib["max"]
    print ("Max        : {0}".format(max))
    
    #------------------------------------------------------
    
    db = sqlite3.connect(databasefile)   

    cursor = db.cursor()
    #                                     0          1           2    3   4      5  
    sql = """INSERT INTO OPENWEATHER (INSERTTIME,WEATHERTIME,CONTENT,MIN,MAX,TEMPERATURE) VALUES ('{0}','{1}','{2}',{3},{4},{5})""".format(current_time,last_update,content,min,max,temperature)
    
    try:
        print (sql)
        cursor.execute(sql)
        db.commit()
    except Exception as ex:
        print ("Exception  : {0}".format(ex))
 #       db.rollback()
    
    db.close()

#------------------------------------------------------------------------------

#createEmptyDatabase();

result = requests.get(url)

if result.status_code == 200:
    content = result.content
    writeToFile()
    appendToDatabase()
    
