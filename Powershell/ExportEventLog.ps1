Get-EventLog System | Export-Csv C:\Work\EventLog.csv -NoTypeInformation -Delimiter ";" -Encoding UTF8

Get-EventLog System | Export-Clixml C:\Work\EventLog.xml -Encoding UTF8