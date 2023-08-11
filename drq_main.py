#Daniel Reséndiz Quiroz - 2183034962

#Computacion lo mejor en la UAM

#main
print("Ingresa dos numeros para la suma de sus pares")
num1 = int(input())
num2 = int(input())
sumaPares(num1, num2)

print("Ingresa el tamaño del arreglo e ingresa sus valores")
tamanho = int(input())
vectorInvertido(tamanho)

print("Ingresa un numero p para determinar si es primo")
p = int(input())
prim = esPrimo(p)
if prim:
    print("p es primo")
else:
    print("p no es primo")

#Calculadora
print("Calculadora basica")
print("1) Suma")
print("2) Resta")
print("3) Multiplicacion")
print("4) Division")
print("Elige una opcion")
operacion = int(input())
calculadora(operacion)