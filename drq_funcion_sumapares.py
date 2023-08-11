#Daniel Reséndiz Quiroz - 2183034962

#Función Suma de pares
def sumaPares(n, m):
    suma = 0
    while n <= m:
        if n % 2 == 0:
            suma = suma + n
            print(n)
        elif n != m:
            print("+")
        n = n + 1
    return print("=", suma)