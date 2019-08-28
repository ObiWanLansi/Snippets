
function Get-MarkdownForServices($status)
{
   $markdown = "`n# $status`n`n"
   $markdown += "|Name|DisplayName|`n"
   $markdown += "|----|-----------|`n"

   foreach($service in Get-Service| Where-Object {$_.status -eq “$status”})
   {
        $markdown += "|" + $service.Name + "|" + $service.DisplayName + "|`n"
   }

    return $markdown
}

$markdown = ""

$markdown += Get-MarkdownForServices("Running");
$markdown += Get-MarkdownForServices("Stopped");


$markdown
Set-Clipboard $markdown
