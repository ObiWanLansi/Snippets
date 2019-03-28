import os
import datetime as dt
import sqlite3

from xml.sax import make_parser, handler

#######################################################################################################################

osm_input_file = r"x:\OpenStreetMap\Europe\germany-latest.osm"
sqlite_output_file = r"x:\OpenStreetMap\Europe\germany-latest.py.sqlite"

#osm_input_file = "X:\OpenStreetMap\europe-latest.osm"
#sqlite_output_file = "X:\OpenStreetMap\europe-latest.sqlite"

tags = [ "place" , "aeroway" , "power" , "man_made" , "leisure" , "amenity" , "shop" , "vending" , "craft" , "emergency" , "military" ]

sql = "INSERT INTO NODE (ID, LAT, LON, NAME, TAG, VALUE) VALUES (?,?,?,?,?,?)"

#######################################################################################################################


class NodeHandler(handler.ContentHandler):

    def __init__(self):
        self.id = None
        self.lat = None
        self.lon = None
        self.name = None
        self.tag = None
        self.value = None
        self.wanted = False


    def storeNode(self):
        cursor = db.cursor()
        values = (self.id,self.lat,self.lon,self.name,self.tag,self.value)
        cursor.execute(sql,values)


    def startElement(self, name, attrs):

        if name == "node":
            self.name = None
            self.tag = None
            self.value = None
            self.wanted = False

            self.id = attrs["id"]
            self.lat = attrs["lat"]
            self.lon = attrs["lon"]

        if name == "tag":
            if self.wanted == False:
                self.tag = attrs["k"]
                if self.tag == "name":
                    self.name = attrs["v"]
                else:
                    if self.tag in tags:
                        self.value = attrs["v"]
                        self.wanted = True
                        global nodecounter
                        nodecounter += 1

        if name == "way":
            # Soblad die Wege kommen sind die Nodes durch und wir können (auch wenn unschön) beenden ...
            raise BaseException('We need no ways ...')


    def endElement(self,name):
        if name == "node":
            if self.wanted == True :
                #pass
                self.storeNode()


#######################################################################################################################


if os.access(sqlite_output_file,os.F_OK):
    os.remove(sqlite_output_file)

db = sqlite3.connect(sqlite_output_file)

cursor = db.cursor()

cursor.execute("""CREATE TABLE NODE (ID INTEGER NOT NULL PRIMARY KEY,LAT DOUBLE NOT NULL,LON DOUBLE NOT NULL, NAME TEXT, TAG TEXT NOT NULL,VALUE TEXT NOT NULL)""")

start = dt.datetime.now()

nodecounter = 0

nh = NodeHandler()
parser = make_parser()
parser.setContentHandler(nh)

#--------------------------------------

cursor.execute("""begin transaction""");

try:
    parser.parse(osm_input_file)
except (BaseException) as e:
    print ("Exception: {0}".format(e.args[0]))

cursor.execute("""commit""");

#--------------------------------------

print ("Nodes: {0}".format(nodecounter))

stop = dt.datetime.now()

timespan = stop - start

print ("Time :",timespan)

db.close()
