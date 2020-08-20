import csv
m1=open("Registro3.csv","r")
m1_csv=csv.reader(m1)
print('***************Registro CSV***************')
for nombre,profesion,pais,estado in m1_csv:
    print('-------------------------------------')
    print("nombre: ", nombre)
    print("profesion: ",profesion)
    print("pais: ",pais)
    print("Estado: ",estado)
    print("Tipo de datos",type(nombre))
