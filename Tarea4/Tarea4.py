import os

import webbrowser


nombre=["wuilmar","Carlos","Juan","Pedro","wuilmar","Carlos","Juan","Pedro","wuilmar","Carlos"]
edad=["22","21","15","54","10","45","18","54","32","23"]
activo=["True","False","False","True","True","False","False","True","True","False"]
saldo=["100","35","48","22","58","22","69","61.5","22.6","89.3"]
texto=""
for i in range(0,len(nombre)):
    texto=texto+f"<tr><td>{nombre[i]}</td><td>{edad[i]}</td><td>{activo[i]}</td><td>{saldo[i]}</td></tr>"

f = open("Reporte.html", "w")
m = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reporte</title>



</head>
<body>
    <h1 align="center" >Reporte</h1>
<br>
<br>
   <table align="center">
    <tr>
    <td>NOMBRE</td>
    <td>EDAD</td>
    <td>ACTIVO</td>
    <td>SALDO</td>
    </tr>
    <tr>{texto}</tr>


    </table>

</body>
</html>
"""

f.write(m)
f.close()
webbrowser.open_new_tab("Reporte.html")





