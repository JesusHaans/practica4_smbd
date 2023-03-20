
# Arreglo con la lista de nombres
a = ["Ricardo", "Rodrigo", "Ailyn", "Gerardo", "Tania", "Valeria", "Carlos", "Lisardo", "Rinaldo", "Rodolfo", "Rodney", "Ailen", "Ailine", "Geraldo", "German", "Tanja", "Valerie", "Marcos"]



# funcion para obtener el valor de una cadena dada
""""
    Entrada: cadena a
    Salida: valor entero de la cadena a
"""
def getValue(a):
    sum = 0
    for char in a:
        sum = sum + ord(char)
    return sum

# funcion para hacer un hash de un elemento dado
"""
    Entrada: elemento a
    Salida: valor hash del elemento a
"""

def hashing(a):
    h = getValue(a) % 9
    return h


# funcion para hacer un hash de un vector dado
"""
    Entrada: vector a
    Salida: vector con los valores hash de cada elemento del vector a asi 
    como los fue encontrando en los valores de entrada
"""

def hashingArray(a):
    res = []
    for x in a:
        res.append(hashing(x))
    return res

# funcion para hacer un hash de un vector dado
"""
    Entrada: vector a
    Salida: vector con los valores hash de cada elemento del vector a asi 
    como los fue encontrando en los valores de entrada e imprime el bucket 
"""
def hashingArrayWithPrint(a):
    res = []
    buckets = [[],[],[],[],[],[],[],[],[]]
    for x in a:
        h = hashing(x)
        buckets[h].append(x)
        res.append(h)
    print("Las asignaciones del arreglo son")
    print(res)
    print("\n")
    print("Los DataBuckets quedarían de la siguiente manera \n")
    print(buckets)
    return

# funcion para testear las funciones

def test():
    hashingArrayWithPrint(a)
    return

#Ejecucion del programa de testeo

test()