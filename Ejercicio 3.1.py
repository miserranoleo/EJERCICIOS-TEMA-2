texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Dividir el texto en partes usando el carácter "#" como separador
partes = texto_original.split("#")

# Capitalizar la primera letra de la primera parte para que empiece con mayúscula
partes[0] = partes[0].capitalize()

# Agregar un punto al final de la primera parte
partes[0] += "..."

# Agregar un punto y un espacio al final de las otras partes
for i in range(1, len(partes)):
    partes[i] = "- " + partes[i].capitalize() + "."

# Unir las partes para formar el texto transformado
texto_transformado = "\n".join(partes)

print(texto_transformado)
