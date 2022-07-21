print("ECC forma general:\t y^2 mod n=(x^3  + a*x + b)mod n\n#IMPORTANTE# Por cuestiones de dificultad los valores 'n', 'a' y 'b' son fijos\n\nValor de 'n': 193") 
import numpy as geek

def polynomial(LHS, RHS, n):
    for i in range(0, n):
        LHS[0].append(i)
        RHS[0].append(i)
        LHS[1].append((i * i * i + a * i + b) % n)
        RHS[1].append((i * i) % n)


def points_generate(arr_x, arr_y, n):
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            if (LHS[1][i] == RHS[1][j]):
                count += 1
                arr_x.append(LHS[0][i])
                arr_y.append(RHS[0][j])
    return count


# main
n = 193 #primos
LHS = [[]]
RHS = [[]]
LHS.append([])
RHS.append([])
a = 3
print("Introduce el valor de 'a':", a)
b = 1
print("Introduce valor de 'b':", b)
# Polynomial
polynomial(LHS, RHS, n)

arr_x = []
arr_y = []
# Generating base points
count = points_generate(arr_x, arr_y, n)

# Print Generated Points
print("Los puntos generados son")
for i in range(0, count):
    print(i + 1, " (", arr_x[i], ",", arr_y[i], ")\n")

# Calculando punto base
bx = arr_x[5]
by = arr_y[0]
print("Punto de la curva inicial:\t(", bx, ",", by, ")\n")

print("Introduce numero random 'd' para la llave privada del remitente (d<n):")
d = int(input())
print("Clave primaria para el destinatario : ", d )
if (d >= n):
    print("'d' debe ser mas pequeno que 'n'.")
else:
    # Q i.e. Generacion de clave publica del remitente
    Qx = d * bx
    Qy = d * by
    print("Public key :\t(", Qx, ",", Qy, ")\n")

    # Encrytion
    k = d
    if (k >= n):
        print("La k debe ser menor que 'n'")
    else:

        # Cipher text 1 generation
        C1x = k * Qx
        C1y = k * Qy
        print("Punto KKP (cifrado punto) :\t(", C1x, ",", C1y, ")\n")

        # Cipher text 2 generation
        C2x = k * bx
        C2y = k * by
        print("Punto KP (decifrado de punto) :\t(", C2x, ",", C2y, ")\n")

        ### Cifrado de puntos KP ###
        Et1 = chr(C2x)
        Et2 = chr(C2y)
        print("Cifrado de puntos KP =\t(", Et1, ",", Et2, ")\n")

        ### Cifrado de puntos KKP ####
        Ek = C1x
        print("Puntos KKP = ", Ek)
        Eb = [bin(Ek)[2:].zfill(8)]
        Ebb= ','.join(Eb)
        print("Cifrado de puntos en binario = ",Eb)

        ### INtroduce texto sin formato ###
        print("Enter the message to be sent:\n")
        B = str(input())

        ## Conversion a binario ##
        In = [ord(c) for c in B]
        print(In)

        ## Merubah Ke Biner ##
        Bi = [bin(x) [2:].zfill(8) for x in In]
        Bii= ','.join(Bi)
        print(Bii)

        ## Relizando XOR en el punto absisa XOR ##
        data = Bii
        key = Ebb


        #### Haciendo XOR ####

        in_arr1 = In
        in_arr2 = [Ek]

        print("Input array1 : ", in_arr1)
        print("Input array2 : ", in_arr2)

        out_arr = geek.bitwise_xor(in_arr1, in_arr2)
        print("La matriz de salida ", out_arr)

        Ekb = [bin(x)[2:].zfill(8) for x in out_arr]
        print("Resultados de XOR =",Ekb)

        ###### Texto cifrado #######
        Dekripsi_xor = ''.join([chr(int(x, 2)) for x in Ekb])
        print("Resultado XOR =" ,Dekripsi_xor)


        ##### Cifrado de texto sin formato  + encabezado #####
        q= Et1
        w= Et2
        e= Dekripsi_xor
        t= '#'
        z= q+t+w+t+e
        print("Resultado de encriptacion =",z)

########################################################################################################################
        print("========================== Descripcion de mensaje cifrado ==========================================")
        ##### Descifrado de separacion de encabezados#####
        Dz=z[4:]
        print("Cifrado con encabezado eliminado", Dz)

        ###### Descripcion de encriptacion #######
        bz = [ord(c) for c in Dz]
        print(bz)
        ###### Integrar a binario #######
        bzi = [bin(x)[2:].zfill(8) for x in bz]
        print(bzi)

        ###### Punto kp ######
        Kt1= k*C2x
        Kt2= k*C2y
        print("Puntos KKP (Descifrado de punto) :\t(", Kt1, ",", Kt2, ")\n")

        ### Cifrado de puntos KKP ####
        Edt = Kt1
        print("Punto absisa = ", Edt)
        Edtb = [bin(Edt)[2:].zfill(8)]
        Edtbb = ','.join(Edtb)
        print("Punto absisa de KKP en binario = ", Edtbb)

        #### Hacer XOR ####4

        Dek_arr1 = bz
        Dek_arr2 = [Edt]

        print("Input array1 : ", Dek_arr1)
        print("Input array2 : ", Dek_arr2)

        Fin_arr = geek.bitwise_xor(Dek_arr1, Dek_arr2)
        print("Salida de la matriz: ", Fin_arr)

        Pl = [bin(x)[2:].zfill(8) for x in Fin_arr]
        print("Resultado de XOR =",Pl)

        ###### Crear texto plano #######
        Plaintex_ecc = ''.join([chr(int(x, 2)) for x in Pl])
        print("El texto original es =",Plaintex_ecc)