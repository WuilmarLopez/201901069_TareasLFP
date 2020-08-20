
import json
with open("Registro1.json") as misDatos:
    datos=json.loads(misDatos.read())
    #print(datos)
    print('***************Registro Json***************')
    for i in range(0,4):
        print('nombre: '+datos['nombres'][i])
        #print(type(datos['nombres'][i]))
        print('profesion:'+datos['profesion'][i])
        print('Estado civil: '+datos['estadoCivil'][i])
        print('pais: '+datos['pais'][i])
        print('-------------------------------------')

    print('tipos de datos de los registros Json')
    print(type(datos['nombres']))


