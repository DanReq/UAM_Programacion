#Daniel Reséndiz Quiroz - 2183034962

#Función impresión de vector invertido
def vectorInvertido(n):
    vector = []
    for i in range(n):
        serie = int(input())
        vector.append(serie)
        i += 1
    print("Forma invertida")
    for i in range(0, n):
        print(int(vector[n-i-1]))