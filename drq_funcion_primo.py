#Daniel Reséndiz Quiroz - 2183034962

#Funcion Esprimo
def esPrimo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True