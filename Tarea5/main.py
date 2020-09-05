#entrada="__servidor1"          #Correcta
#entrada="_____servidor18"       #correcta
entrada="servidor3"            #incorrecta
#entrada="_servidor*"           #incorrecta
if entrada[0]=="_":
    estado=0
else:
    estado=3


for i in range(1,len(entrada)):
    if estado==0:
        if entrada[i].isalpha():
            estado=1
        elif entrada[i]=="_":
            estado=0
        else:
            print("no pertenece")
            break
    elif estado==1:
        if entrada[i].isnumeric():
            print("Si pertenece")
            estado=2
            break
        elif entrada[i].isalpha():
            estado=1
            if i==len(entrada)-1:
                print("error")
                break
        else:
            print("no pertenece")
            break
    else:
        print("no pertenece")
        break

