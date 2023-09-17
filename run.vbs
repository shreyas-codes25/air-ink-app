set oShell = CreateObject ("Wscript.shell")
Dim strArgs
strArgs = "cmd /c Air.bat"
oShell.Run strArgs, 0, false