#!/home/lansi/anaconda3/bin/python3

# Test Argument 1: /home/lansi/freemind/freemind.sh
# Test Argument 2: /home/lansi/knime_3.6.0/knime

import sys
import os

if len(sys.argv) < 2:
    print("Es muss mindestens eine Executable als Argument übergeben werden!")
    exit

#----------------------------------------------------------------------------------------------------------------------

template_file = "/home/lansi/Starter/Template.txt"
starter_dir = "/home/lansi/Starter/Generated"

#----------------------------------------------------------------------------------------------------------------------

fTemplate = open(template_file)
strTemplate = fTemplate.read()
fTemplate.close()
    
#----------------------------------------------------------------------------------------------------------------------


def CreateEntry(executable):
    
    print("Create Deskop Entry For {0}".format(executable))
    basename = os.path.basename(executable).capitalize()
    
    if basename.endswith(".sh"):
        basename = basename[:-3]
    
    strDesktopEntry = strTemplate.replace("%NAME%", basename)
    strDesktopEntry = strDesktopEntry.replace("%EXEC%", executable)
    strDesktopEntry = strDesktopEntry.replace("%COMMENT%", executable)
    print (strDesktopEntry)
    strDesktopEntryFilename = "{0}/{1}.desktop".format(starter_dir,basename)
    #print (strDesktopEntryFilename)
    fDesktopEntry = open(strDesktopEntryFilename,"w")
    fDesktopEntry.write(strDesktopEntry)
    fDesktopEntry.close()
    os.chmod( strDesktopEntryFilename,0o700)

#----------------------------------------------------------------------------------------------------------------------

for i in range(1,len(sys.argv)):
    CreateEntry(sys.argv[i])
    