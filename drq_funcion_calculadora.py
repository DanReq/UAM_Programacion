#Daniel Reséndiz Quiroz - 2183034962

#Funcion calculadora
def calculadora(opcion):
    match opcion:
        case 1:
            entrada1 = int(input("Ingresa el primer numero: "))
            entrada2 = int(input("Ingresa el segundo numero: "))
            suma = entrada1 + entrada2
            print(suma)
        case 2:
            entrada1 = int(input("Ingresa el primer numero: "))
            entrada2 = int(input("Ingresa el segundo numero: "))
            resta = entrada1 - entrada2
            print(resta)
        case 3:
            entrada1 = int(input("Ingresa el primer numero: "))
            entrada2 = int(input("Ingresa el segundo numero: "))
            multiplica = entrada1 * entrada2
            print(multiplica)
        case 4:
            entrada1 = int(input("Ingresa el primer numero: "))
            entrada2 = int(input("Ingresa el segundo numero: "))
            division = entrada1 / entrada2
            print(division)
        case _:
            print("Selecciona una opcion valida")