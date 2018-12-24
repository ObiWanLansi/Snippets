#!/usr/bin/python

import requests
import time
import sqlite3
import os.path

from bs4 import BeautifulSoup

#----------------------------------------------------------------------------------------------------------------------

current_time = time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time()))
divider = "".center(80,'-')
#print ("CurrentTime: {0}".format(current_time ))

#----------------------------------------------------------------------------------------------------------------------

# The Shell Immenstaad
#SHELL_IMMENSTAAD = "http://www.clever-tanken.de/tankstelle_details/45625"

# The Shell Espasingen
#SHELL_ESPASINGEN = "http://www.clever-tanken.de/tankstelle_details/45654"

# The Aral Singen
#ARAL_SINGEN = "http://www.clever-tanken.de/tankstelle_details/48757"

# The Agip Meersburg
#AGIP_MEERSBURG = "http://www.clever-tanken.de/tankstelle_details/2423"

# The Agip Stockach
#AGIP_STOCKACH = "http://www.clever-tanken.de/tankstelle_details/2413"

#----------------------------------------------------------------------------------------------------------------------


#DATABASEFILE = "/var/www/html/FuelPrice.db"
DATABASEFILE = r"S:\Work\FuelPrice.db"


GASSTATIONS = {
        "SHELL Immenstaad" : 45625,
        "SHELL Espasingen" : 45654,
        "ARAL Singen" : 48757,
        "AGIP Meersburg" : 2423,
        "AGIP Stockach" : 2413
}

#----------------------------------------------------------------------------------------------------------------------


def createEmptyDatabase():
    db = sqlite3.connect(DATABASEFILE)
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE FUELPRICE (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, INSERTTIME TIMESTAMP NOT NULL, GASTSTATIONID INTEGER NOT NULL, GASTSTATIONNAME TEXT NOT NULL, FUELTYPE TEXT NOT NULL,PRICE FLOAT NOT NULL)""")
    db.close()

#----------------------------------------------------------------------------------------------------------------------


def readGasStation(station_name,station_id):

    url = "http://www.clever-tanken.de/tankstelle_details/{}".format(station_id)

    result = requests.get(url)

    if result.status_code != 200:
        return

    #station_id =url[url.rindex('/')+1:]
    #print ("{}: >{}<".format(url,station_id))

    html_content = result.content
    soup = BeautifulSoup(html_content,'html.parser')

    #print()
    #print(divider)
    #title = soup.title.string
    #index = title.rindex(" -")
    #print (">{0}<".format( title[:index]).title())

    #address = soup.select_one('div[id="gas_station_address"]')

    #------------------------------------------------------

    db = sqlite3.connect(DATABASEFILE)

    divs = soup.select('div[class="fuel-price-entry"]')

    for entry in divs:
        #print()

        price = entry['ng-init'][6:11].replace(',','.')
        #print ("\tPrice    : >{}<".format(price))

        fueltype = entry.div.span.string
        #print ("\tFuelType : >{}<".format(fueltype))

        cursor = db.cursor()

        sql = """INSERT INTO FUELPRICE (INSERTTIME,GASTSTATIONID,GASTSTATIONNAME,FUELTYPE,PRICE) VALUES ('{0}',{1},'{2}','{3}',{4})""".format(current_time,station_id,station_name,fueltype,price)

        try:
            #print (sql)
            cursor.execute(sql)
            db.commit()
        except Exception as ex:
            print ("Exception  : {0}".format(ex))
    db.close()

#----------------------------------------------------------------------------------------------------------------------

if os.path.exists(DATABASEFILE) == False:
    #print ("Database {} not exists, i'll create them!".format(DATABASEFILE))
    createEmptyDatabase()
#else:
    #print ("Database {} already exists!".format(DATABASEFILE))

#----------------------------------------------------------------------------------------------------------------------

for station in GASSTATIONS.keys():
    readGasStation(station,GASSTATIONS[station])

#readGasStation(SHELL_IMMENSTAAD)
#readGasStation(SHELL_ESPASINGEN)
#readGasStation(ARAL_SINGEN)
#readGasStation(AGIP_STOCKACH)

