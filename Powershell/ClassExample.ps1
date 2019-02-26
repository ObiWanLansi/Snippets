class Person
{
    [string] $Surename;

    [string] $Firstname;

    [DateTime] $DateOfBirth
}


$p = [Person]::new()
$p.Firstname = "Hans"
$p.Surename = "Glück"
$p.DateOfBirth = [DateTime]::Now

Out-GridView -InputObject $p