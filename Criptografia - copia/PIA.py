
print("Hola, este es el PIA de Criptologia")
print("En base el siguiente menu, digita el numero correspondiente a la encriptacion que deseas ver")
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Diffie-Hellman")
    print ("2. RSA")
    print ("3. ECC")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Diffie-Hellman\n")
        import DiffieHellman

    elif opcion == 2:
        print ("RSA\n")
        import RSA

    elif opcion == 3:
        print("ECC\n")
        import ECC2
        
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")