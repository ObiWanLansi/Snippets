# DESC File Or Directory Change Name
# AUTH Jörg Lanser
# VERS 1.0

########################################################################################################################

require 'getoptlong'

opts = GetoptLong.new(
  [ "--help"        , "-h", GetoptLong::NO_ARGUMENT ],
  [ "--verbose"     , "-v", GetoptLong::NO_ARGUMENT ],
  [ "--files"       , "-f", GetoptLong::NO_ARGUMENT ],
  [ "--directories" , "-d", GetoptLong::NO_ARGUMENT ],
  [ "--recurse"     , "-r", GetoptLong::NO_ARGUMENT ],
  [ "--upper"       , "-u", GetoptLong::NO_ARGUMENT ],
  [ "--lower"       , "-l", GetoptLong::NO_ARGUMENT ],
  [ "--capitalize"  , "-c", GetoptLong::NO_ARGUMENT ],
  [ "--test"        , "-t", GetoptLong::NO_ARGUMENT ]
)

########################################################################################################################

def usage
    puts ""
    puts "Usage : fidich.rb [-v] [-d] [-f] [-r] -u -l -c [-t]"
    puts
    puts "    -v Verbose output"
    puts "    -d Rename directories"
    puts "    -f Rename files"
    puts "    -r Recursiv"
    puts "    -u Uppercase"
    puts "    -l Lowercase"
    puts "    -c Capitalize"
    puts "    -t Testingmode"
end

########################################################################################################################

def output(strMessage, bVerbose)
    if bVerbose == true then
        puts strMessage
    end
end

########################################################################################################################

def isAlpha(iASCII)
    if ( iASCII < 65 or iASCII > 90 ) and ( iASCII < 97 or iASCII > 122 ) then
        return false
    end
    
    return true
end

########################################################################################################################

def capitalize(strText)

    strOutput = ""
    
    #puts strText

    for iCounter in 0 .. strText.length - 1
    
        c = strText[iCounter,1]
    
        if isAlpha(strText[iCounter]) == true then
        
            if iCounter > 0 then
            
                if isAlpha(strText[iCounter-1]) == false then
                    c.upcase!
                else
                    c.downcase!
                end
            else
                c.upcase!
            end
            
        end
        
        strOutput = strOutput + c
    end

    #puts strOutput

    return strOutput
end

########################################################################################################################

def checkAndRename(strDirectoryname, strFilename, iType, bVerbose, bTest)

    case iType

        when 0
            strNewName = strFilename.downcase

        when 1
            strNewName = strFilename.upcase

        when 2
            strNewName = capitalize(strFilename)
    end

    if strNewName != strFilename then

        output("    Rename " + strFilename + "\n    to     " + strNewName + "\n\n", bVerbose)
        
        strFullnameOld = strDirectoryname + "\\" + strFilename
        strFullnameNew = strDirectoryname + "\\" + strNewName

        if bTest == false then
            begin
                File.rename(strFullnameOld,strFullnameNew)
            rescue
                output("    Error : #{$!}", bVerbose)
            end
        end
    end
end

########################################################################################################################

def scanDirectory(strDirectoryname, bRecursiv, bDirectories, bFiles, iType, bVerbose, bTest)

    output("Scanning directory " + strDirectoryname, bVerbose)

    Dir.foreach(strDirectoryname) {

        |dCurrent|

        if dCurrent != "." and dCurrent != ".." then

            strFullname = strDirectoryname + "\\" + dCurrent

            if FileTest.directory?(strFullname) then

                if bDirectories == true then
                
                    checkAndRename(strDirectoryname, dCurrent, iType, bVerbose, bTest)
                end

                if bRecursiv == true then

                    scanDirectory(strFullname, bRecursiv, bDirectories, bFiles, iType, bVerbose, bTest)
                end
            else
            
                if bFiles then
                
                    if FileTest.file?(strFullname) then

                        checkAndRename(strDirectoryname, dCurrent, iType, bVerbose, bTest)
                    end
                end
            end
        end
    }
end

####################################################################################################

bVerbose     = false
bDirectories = false
bFiles       = false
bRecursiv    = false
iType        = 0 # 0->Lowercase, 1->Uppercase, 2->Capitalize
bTest        = false


opts.each do |opt, arg|
    case opt
    
        when "--help"
            usage
            exit
            
        when "--verbose"
            bVerbose = true

        when "--files"
            bFiles = true

        when "--directories"
            bDirectories = true

        when "--recurse"
            bRecursiv = true

        when "--lower"
            iType = 0 # 0->Lowercase, 1->Uppercase, 2->Capitalize

        when "--upper"
            iType = 1 # 0->Lowercase, 1->Uppercase, 2->Capitalize

        when "--capitalize"
            iType = 2 # 0->Lowercase, 1->Uppercase, 2->Capitalize

        when "--test"
            bTest = true
    end
end


if bFiles == true or bDirectories == true then

    scanDirectory(Dir.getwd, bRecursiv, bDirectories, bFiles, iType, bVerbose, bTest)
else

    puts "Es muss mindestens angeben werden ob Dateiname oder Verzeichnisname gewandelt werden sollen !"
end