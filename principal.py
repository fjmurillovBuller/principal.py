edades = [32, 15, 8, 19, 33, 12, 40, 15, 11, 8, 33, 33, 28, 33, 32]
print(edades)

nombres = ("Francisco", "Javier", "Jovanela", "Josue", "Murillo", "Estefany")
print(nombres)  

calificaciones =["A", 100, 10.5, 6.5, "B", "A", 7.5, 43, "C"]
print(calificaciones)

colores =["Azul", "Rojo", "Verde", "Rosado", "Blanco", "Gris","Magenta", "Negro"]
print(colores)

#cual es el cuarto Elemento de las edades?
cuarto_elemento_edades = edades[3]
print(f"El cuarto elemento de las edades es:{cuarto_elemento_edades}")

#cual es el segundo elemento de los nombres
segundo_elemento_nombres = nombres [1]
print(f"el segundo nombre es: {segundo_elemento_nombres}")

#exite la edad 12
existe_edad_12 = 12 in edades #devuelve true o False
print(f"hay alquien de 12 años: {existe_edad_12}")

#En que posicion esta el nombre Josue
print(f"El nombre Josue en que posicion esta: {nombres.index('Josue')}")

#cuales son los primeros 3 elementos calificacines?
# slice
tres_primeras_calicacione = calificaciones[:3]
print(f"los primeros 3 elementos de las calificaciones es:{tres_primeras_calicacione}")

#cuales son los ultimos 5 elementos de los colores?
cinco_ultimos_colores = colores[-5:]
print(f"cuales son los ultimos colores {cinco_ultimos_colores }")

#cuales son las calificaciones omitiendo el primero y  el ultimo elemento
calificaciones_omitiendo_limites = calificaciones[1:-1]
print(f"cuales son las calificaciones omitiendo la primera y la ultima {calificaciones_omitiendo_limites}")

#las listas son modificables y las duplas son Inmutables

colores.append("Naranja")
print(f"La lista de los colores acutalizada(agregando el color naranja) es: {colores}")

#extends: agrega al final de la lista los elementos de otras listas
municipios_Managua = ["Ciudad Sandino", "El Crucero", "Mateare", "San Francisco libre","Tipitapa"]
municipios_Masaya = ["Catarina", "La Concepcion", "Masatepe", "Masaya", "Nandasmo", "Nindiri"]
municipios=[]
municipios.extend(municipios_Managua)
municipios.extend(municipios_Masaya)
print(f"Los municipios de Managua es:{municipios_Managua}")
print(f"Los municipios de Masaya es: {municipios_Masaya}")
print(f"La lista de municipios(extendida)es:{municipios}")

# Insert: Para agregar elemento en otro lugar que no sea al final de la lista

#Agregar el municipio de Managua, entre el crucero y Mateare
municipios.insert(2, "Managua")
print(f"La lista de Municipios(Incluyendo la cuidad de Managua)es:{municipios}")

# pop: Elimina un elemento de una lista por indice
# Eliminar el cuarto elemento de la lista de minicipios(Mateare)
municipios.pop(3)
print(f"La lista de municipios(eliminando el cuarto elemento)es:{municipios}")

# Eliminar el penultimo elemento de los municipios
municipios.pop(-2)
print(f"Eliminame el penultimo elemento de la lista {municipios}")

# elimiar con una palabra reservada llamada DEL
# Eliminar el Cuarto elemento de la lista de municipios
del municipios[3]
print(f"la lista de municipios(eliminando el cuarto elemento)es:{municipios}")

# Eliminame de la lista de municipios desde el segundo hasta el cuarto elemento
del municipios[1:4]
print(f"La lista de municipios(eliminame del segundo al cuato elemento) es:{municipios}")

# Remove : Para eliminar una lista por medio del valor
# Eliminar Nindiri de la lista de municipios
municipios.remove("Nindiri")
print(f"La lista de municipios(eliminar Nindiri)es:{municipios}")

# Nueva Lista con Lenguajes
# Se le pregunta a algunas personas que lenguaje habla
Lenguajes = {"Español", "English", "Español", "Frances","Español", "Portuques", "Ruso","Chino_Mandarin","Español", "Italiano"}

# hay alquien que habla English
alquien_habla_English = "English" in Lenguajes
print(f"hay alquien que habla English? Repuesta: {alquien_habla_English}")











