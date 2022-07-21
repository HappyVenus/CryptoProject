##Pregunto los primos
print("Bienvenido al algoritmo Diffie-Hellman\n")
p = int(input("Ingresa un numero primo para p: "))
q = int(input("Ingresa un numero primo para q: "))
##Private Keys
print("\nGenerando las llaves privadas, introduce un numero: ")
Alice_Key = int(input("Alice llave privada: "))
Bob_Key = int(input("Bob llave privada: "))

##Valores publicos
print("Creando las llaves publicas...\n")
alice = p**Alice_Key % q
print(f"llave publica Alicia: {p}**{Alice_Key} % {q} = {alice}")
bob = p**Bob_Key % q
print(f"llave publica Bob: {p}**{Bob_Key} % {q} = {bob}")
#Alice y Bob, generan la misma llave

print("\nGenerando la misma llave...")
Alice = bob**Alice_Key % q
print(f"Generando la llave de Alice {bob}**{Alice_Key} % {q} = {Alice}")
Bob = alice**Bob_Key % q
print(f"Generando llave de Bob {alice}**{Bob_Key} % {q} = {Bob}")
print(f"\nLlave de Alice es {Alice} y la de Bob es {Bob}")
print("\nAmbos tuvieron la misma llave, eso significa que funciono!")
print("\nRegresando al menu...")