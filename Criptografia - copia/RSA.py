import random

def rabinMiller(n, d):
    a = random.randrange(2, (n - 2) - 2)
    x = pow(a, int(d), n)
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    # No es primo
    return False


def isPrime(n):
    ##Return True si n es primo
    ##Regrea a RabinMiller si no

    if n < 2:
        return False

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if n in lowPrimes:
        return True
    
    for prime in lowPrimes:
        if n % prime == 0:
            return False
        
    c = n - 1
    while c % 2 == 0:
        c /= 2

    # aplicando RobinMiller no es primo
    for i in range(128):
        if not rabinMiller(n, c):
            return False


    return True


def generateKeys(keySize=1024):
    e = d = N = 0

    ##Obtener numeros primos p y q
    p = generateLargePrime(keySize)
    q = generateLargePrime(keySize)


    N = p * q

    phiN = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** keySize - 1)
        if (isCoPrime(e, phiN)):
            break

    #Escoger d 
    #d es mod inv de e con respecto a phiN, e * d (mod phiN) - 1
    d = modularInv(e, phiN)

    return e, d, N, p, q, phiN

def generateLargePrime(keySize):
    ## Devuelve un numero primo largo de tamano keysize bits 

    while True:
        num = random.randrange(2 ** (keySize - 1), 2 ** keySize - 1)
        if (isPrime(num)):
            return num

def isCoPrime(p, q):
    
## Devuelve True si gcd(p, q) es 1
## primo relativo

    return gcd(p, q) == 1

def gcd(p,q):
    ## Alritmo para encontrar mcd de p y q

    while q:
        p, q = q, p % q

    return p  

def egcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r // r 
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # Return gcd, x, y
    return old_r, old_s, old_t

def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x

def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher

def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg


def main():
    print("Hola, Bienvenido a RSA!")

    keySize = 32 
    e, d, N, p, q, phiN = generateKeys(keySize)

    # p = 11
    # q = 13
    # N = p * q
    # phiN = (p - 1) * (q - 1)

    # e = 13
    # d = modularInv(e, phiN)

    msg = input("Ingresa el mensaje que deseas decifrar: \n")


    enc = encrypt(e, N, msg)
    dec = decrypt(d, N, enc)

    print(f"La variable prima de p es: {p}")
    print(f"La variable prima de q es: {q}")
    print (f"Se genera N = p * q\n{p} * {q} = {N}\n")
    print(f"Se genera PhiN = (p - 1) * (q - 1)\n({p} - 1) * ({q} - 1) = {phiN}\n")
    print(f"Generamos e en cuanto al tamano de la llave: {e}\n")
    print(f"Calculamos d, que d es mod inv de e con respecto a phiN, \n{e} * d (mod {phiN}) - 1: {d}")

    # print (f"Mensaje: {msg}")
    # print(f"e: {e}")
    # print(f"d: {d}")
    # print(f"N: {N}")
    print(f"\nEncriptado: {enc}")
    print(f"Desencriptado: {dec}")


    print("\nRegresando al menu")

main()
