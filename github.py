#leer un numero entero comprendido entre 1 y 7 e imprimir en pantalla los dias de semana
#entrada
print("Ingresa el numero")
numero = int(input())
#proceso
if numero==1:
    print("Tu dia es Lunes")
elif numero==2:
    print("Tu dia es Martes")
elif numero==3:
    print("Tu dia es Miercoles")
elif numero==4:
    print("Tu dia es Jueves")
elif numero==5:
    print("Tu dia es Viernes")
elif numero==6:
    print("Tu dia es Sabado")
elif numero==7:
    print("Tu dia es Domingo")
else:
    print("Numero no encontrado entre las semanas")
#salida