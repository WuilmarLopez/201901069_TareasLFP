import xml.etree.ElementTree as ET
archivo_xml=ET.parse('Registro2.xml')
raiz=archivo_xml.getroot()
#print(raiz)
print('***************Registro XML***************')

for hijo in raiz:
    print('-------------------------------------')
    #print(hijo)
    print("Tipo de datos",type(hijo))
    for subhijo in hijo:
        print(subhijo.text)
