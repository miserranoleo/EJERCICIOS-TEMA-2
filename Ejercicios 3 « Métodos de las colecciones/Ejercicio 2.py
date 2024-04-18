def modificar(lista):
    # Copiar la lista original para no modificarla
    lista_modificada = lista.copy()

    # Borrar los elementos duplicados
    lista_modificada = list(set(lista_modificada))

    # Ordenar la lista de mayor a menor
    lista_modificada.sort(reverse=True)

    # Eliminar todos los números impares
    lista_modificada = [num for num in lista_modificada if num % 2 == 0]

    # Realizar la suma de todos los números que quedan
    suma = sum(lista_modificada)

    # Añadir la suma como primer elemento de la lista
    lista_modificada.insert(0, suma)

    return lista_modificada

# Ejemplo de uso y comprobación
lista = [3, 7, 2, 8, 2, 5, 9, 8, 7, 4]
nueva_lista = modificar(lista)
print(nueva_lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))
