#!/usr/bin/env python
# coding: utf-8

# In[1]:


def promedio (vals):
    """
    Calcula el promedio de una lista de numeros.

    Parámetros
    ----------
    vals: lista
    » Lista con números.

    Retorna
    ---------
    promedio: float
    » El promedio aritmetico de los números.
    
    Explicación
    ---------
    Suma todos los datos de la lista y divide esta sumatoria por la cantidad de datos de la lista.
    """
    return sum(vals) / len(vals)


# In[3]:


def mediana (vals):
    """
    Calcula la mediana de los datos de una lista de números.
    
    Parámetros
    ----------
    vals: lista
    » Lista con números.
    lista = lista
    » Lista de datos ordenados.
    largo = float
    » Cantidad de datos en la lista.
    
    Retorna
    ---------
    mediana: float
    » Calcula la mediana de los datos.
    
    Explicación
    ---------
    Se crea la variable lista donde contiene los valores ordenados de menor a mayor, luego se
    crea otra variable llamada largo donde contiene la cantidad de los datos.
    Se crea un ciclo for donde se comprueba que si es que la longitud de la lista es impar, 
    entonces se divide la lista en dos y se obtiene el número central.
    Sin embargo, si no se cumple esto, significando que la lista es par, entonces se divide esta
    lista en dos partes y se obtiene los datos del medio, obteniendo su promedio.
    """
    
    lista = sorted(vals)
    largo = len(vals)
    
    if largo % 2 == 1:
        mediana = lista[largo // 2]
    else:
        centro1 = lista[largo // 2 - 1]
        centro2 = lista[largo // 2]
        mediana = (centro1 + centro2) / 2
    
    return mediana


# In[5]:


def moda(vals):
    """
    Calcula la moda de los datos de una lista de números.

    Parámetros
    ----------
    vals: lista
    » Lista con números de la cual se calculará la moda.

    Retorna
    ---------
    moda: lista
    » Una lista que contiene los valores que son considerados modas en los datos.

    Variables
    ----------
    categorias: lista
    » Una lista que almacena las categorías únicas presentes en la lista de valores.
    
    cuentas: lista
    » Una lista que almacena la frecuencia de cada categoría en la lista de valores.
    
    i_max: integer
    » Índice del valor máximo en la lista de frecuencias.
    
    val_max: integer
    » Valor máximo de frecuencia encontrado en la lista de frecuencias.
    
    Explicación
    ---------
    La función recorre la lista de valores y crea una lista de categorías únicas. 
    Luego, cuenta la frecuencia de cada categoría en la lista de valores y almacena 
    las cuentas en una lista separada. A continuación, encuentra la cuenta máxima y devuelve 
    el valor correspondiente a esa cuenta en la lista de categorías.
    """
    categorias = []
    for v in vals:
        if v not in categorias:
            categorias.append(v)
    cuentas = []
    for c in categorias:
        n = 0  # Cero elementos en esa categoría
        for val in vals:
            if val == c:
                n = n + 1
        cuentas.append(n)

    i_max = 0
    val_max = cuentas[0]
    for i in range(1, len(cuentas)):  # El rango debe comenzar en 1
        if cuentas[i] > val_max:
            i_max = i 
            val_max = cuentas[i]
    comun = categorias[i_max]
    return comun


# In[7]:


def varianza (vals):
    """
    Calcula la varianza.

    Parámetros
    ----------
    vals: lista
    » Lista con números de la cual se calculará la varianza.

    Retorna
    ---------
    Var: float
    » Valor de punto flotante donde se muestra la varianza.

    Variables
    ----------
    suma: variable
    » sumatoria de la resta entre un valor y la suma de todos los datos, dividido
    en la cantidad de datos y todo esto elevado al cuadrado.
    
    Explicación
    ---------
    La función calcula la media aritmética de los valores en la lista y luego calcula 
    la suma de los cuadrados de las diferencias entre cada valor y la media. 
    A continuación, divide esta suma por la cantidad de valores en la lista para obtener 
    la varianza.
    """
    suma = sum((x - (sum(vals) / len(vals)))**2 for x in vals)
    var = suma/len(vals)
    return var


# In[9]:


def desviacion (vals):
    from math import sqrt
    """
    Calcula la desviación estándar de los datos.
    
    Parámetros
    ----------
    vals: lista
    » Lista con números.
    
    Retorna
    ---------
    desv: float
    » La raíz de la varianza.
    
    Explicación
    ---------
    Importamos la raíz de la librería math y la aplicamos a la varianza que obtuvimos 
    anteriormente.
    """
    desv = sqrt(varianza(vals))
    return desv


# In[ ]:


def rango (vals):
    """
    Esta función retorna el rango de una lista de datos.

    Parámetros
    ----------
    vals: lista
    » Lista con números de la cual se calculará el rango.

    Retorna
    ---------
    rango: float
    » Valor de punto flotante donde se muestra el rango de los datos.

    Explicación
    ---------
    La función toma el valor máximo de la lista, el valor mínimo y los resta.
    """
    rango = max(vals) - min(vals)
    return rango


# In[11]:


def MAD (vals):
    """
    Calcula la Desviación Absoluta Media (MAD) de una lista de valores.

    Parámetros
    ----------
    vals: lista de números
    » Lista de números de la cual se calculará la MAD.

    Retorna
    ---------
    mad: float
    » La Desviación Absoluta Media de los valores en la lista.

    Variables
    ----------
    mediana_valor: float
    » La mediana de los valores en la lista, que se utilizará como punto de referencia.
    datos: lista de números
    » Una lista que contendrá las diferencias absolutas entre cada valor y la mediana.
    lista: lista de números
    » Una lista ordenada que contiene las diferencias absolutas.
    longitud: int
    » La cantidad de elementos en la lista 'datos'.
    mad: float
    » La Desviación Absoluta Media calculada.
    
    Explicación
    ---------
    La función utiliza la función `mediana` (que calcula la mediana) para obtener el valor 
    de la mediana de los valores en la lista. Luego, crea una nueva lista llamada 
    'datos', que contiene las diferencias absolutas entre cada valor y la mediana. 
    A continuación, ordena la lista 'datos' y determina la longitud de esta lista.
    Si la longitud de la lista es impar, el MAD es el valor central de la lista ordenada.
    Sin embargo, si la longitud de la lista es par, el MAD es el promedio de los dos valores 
    centrales de la lista ordenada.
    """
    mediana_valor = mediana(vals)
    datos = []
    for num in vals:
        datos_mad = abs(num - mediana_valor)
        datos.append(datos_mad)
        
    lista = sorted(datos)
    longitud = len(datos)
    
    if longitud % 2 == 1:
        mad = lista[longitud // 2]
    else:
        centro1 = lista[longitud // 2 - 1]
        centro2 = lista[longitud // 2]
        mad = (centro1 + centro2) / 2
    
    return mad


# In[7]:


def cuartiles (vals):
    """
    Calcula el percentil 25 y 75 de una lista de valores.

    Parámetros
    ----------
    vals: lista de números
    » Lista de números de la cual se calculará el IQR.

    Retorna
    ---------
    iqr: float
    » El Rango Intercuartil (IQR) de los valores en la lista.

    Variables
    ----------
    datos_ordenados: lista de números
    » Una lista de valores ordenados en orden ascendente.
    longitud: int
    » La cantidad de elementos en la lista 'datos_ordenados'.
    Q1: int
    » El primer cuartil.
    Q3: int
    » El tercer cuartil.
    iqr: lista
    » El primer y tercer cuartil de los datos.
    
    Explicación
    ---------
    La función ordena los valores de menor a menor y luego determina la longitud de la 
    lista ordenada. Luego, verifica si la longitud de la lista es divisible por 4.
    Si la longitud es divisible por 4, significa que esta es par. 
    Se calcula los cuartiles Q1 y Q3 utilizando los valores  en las posiciones correspondientes.
    Si la longitud no es divisible por 4, calcula los cuartiles Q1 y Q3 utilizando los valores 
    en las posiciones ajustadas.
    La función retorna una tupla que contiene los cuartiles Q1 y Q3.
    """
    datos_ordenados = sorted(vals)
    longitud = len(datos_ordenados)
    
    if longitud % 4 == 0:
        Q1 = (datos_ordenados[longitud // 4 - 1] + datos_ordenados[longitud // 4]) / 2
        Q3 = (datos_ordenados[3 * longitud // 4 - 1] + datos_ordenados[3 * longitud // 4]) / 2
    else:
        Q1 = datos_ordenados[(longitud + 1) // 4 - 1]
        Q3 = datos_ordenados[3 * (longitud + 1) // 4 - 1]
    iqr = (Q1, Q3)
    return iqr


# In[8]:


def rango_intercuartil (vals):
    """
    Calcula el Rango Intercuartil (IQR) de una lista de valores.

    Parámetros
    ----------
    vals: lista de números
    » Lista de números de la cual se calculará el IQR.

    Retorna
    ---------
    iqr: float
    » El Rango Intercuartil (IQR) de los valores en la lista.

    Variables
    ----------
    datos_ordenados: lista de números
    » Una lista de valores ordenados en orden ascendente.
    longitud: int
    » La cantidad de elementos en la lista 'datos_ordenados'.
    Q1: int
    » El primer cuartil.
    Q3: int
    » El tercer cuartil.
    iqr: float
    » El Rango Intercuartil calculado al restarle el primer cuartil al tercer cuartil.
    
    Explicación
    ---------
    La función ordena los valores de menor a menor y luego determina la longitud de la 
    lista ordenada. Luego, verifica si la longitud de la lista es divisible por 4.
    Si la longitud es divisible por 4, significa que esta es par. 
    Se calcula los cuartiles Q1 y Q3 utilizando los valores  en las posiciones correspondientes.
    Si la longitud no es divisible por 4, calcula los cuartiles Q1 y Q3 utilizando los valores 
    en las posiciones ajustadas.
    El rango intercuartil (IQR) se calcula como la diferencia entre el tercer cuartil (Q3) 
    y el primer cuartil (Q1).
    """
    datos_ordenados = sorted(vals)
    longitud = len(datos_ordenados)
    
    if longitud % 4 == 0:
        Q1 = (datos_ordenados[longitud // 4 - 1] + datos_ordenados[longitud // 4]) / 2.0
        Q3 = (datos_ordenados[3 * longitud // 4 - 1] + datos_ordenados[3 * longitud // 4]) / 2.0
    else:
        Q1 = datos_ordenados[(longitud + 1) // 4 - 1]
        Q3 = datos_ordenados[3 * (longitud + 1) // 4 - 1]
    iqr = (Q3 - Q1)
    return iqr


# In[9]:


def repeticiones(vals): #Función para buscar repeticiónes.
    """
    Calcula y devuelve los valores de una lista que se repiten 10 o más veces.

    Parámetros
    ----------
    vals: lista
    » Lista con números.

    Retorna
    ---------
    lista_tamaño: lista
    » Lista que contiene los valores de Size que se repiten 10 o más veces.
    
    Explicación
    ---------
    El formato de ejecución del código es similar a buscar una moda, haciendo un ciclo for inicial
    para ir acumulando los valores en una lista vacia. Luego, se crea otra lista donde se ven las cuentas
    y se hace otro ciclo for donde se lee la lista con datos que creamos inicialmente.
    El contador se establece inicialmente como cero y se crea otro ciclo for donde
    se comprueba que los numeros de la lista inicial (Size) si estaban en la cuenta se agrega a esta
    cuenta. El ultimo ciclo for permite que solo sean relevantes los valores que se repiten
    diez o más veces.
    """
    lista_tamaño = []
    for i in vals:
        if i not in lista_tamaño:
            lista_tamaño.append(i)
    cuentas_t = []
    for c in lista_tamaño:
        n = 0
        for nums in vals:
            if nums == c:
                n = n + 1
        if n >= 10:
            cuentas_t.append(n)
    return lista_tamaño


# In[3]:


def agrupaciones(lista_tamaños):
    """
    Permite agrupar por tipos de galaxia los tamaños que obtuvimos previamente.
    
    Parámetros
    ----------
    lista_tamaños : list
    » Lista de tamaños de galaxias representados como números enteros.

    Retorna
    ---------
    Resultado
    » Un diccionario que contiene los promedios de tamaños para diferentes tipos de galaxias.

    Explicación
    ---------
    Esta función toma una lista de tamaños de galaxias y los agrupa en categorías (SBa, SBb, SBc, Irr)
    basadas en intervalos encontrados en internet y el archivo proveido. 
    Comienza con el diccionario vacio llamado resultado donde se iran acumulando los tamaños
    agrupados. Luego, cada tamaño en la lista se verifica con el ciclo for tipo, (inicio, fin)
    donde este lee el diccionario intervalos proveido y verifica donde entra cada dato que lee.
    La función retorna el diccionario nuevo y tambien calcula el promedio de tamaños en 
    cada categoría.
    """
    intervalos = {
        "SBa": (16, 32),
        "SBb": (32, 64),
        "SBc": (64, 128),
        "Irr": (128, float("inf")) #Tuve que investigar para este tipo de galaxias irregulares.
    }

    resultado = {tipo: [] for tipo in intervalos}

    for tamaño in lista_tamaños:
        try:
            tamaño_int = int(tamaño)
        except ValueError:
            # Si no se puede convertir a entero, ignora ese dato. (espero)
            continue

        for tipo, (inicio, fin) in intervalos.items(): #Leemos de inicio a fin el diccionario
            if inicio <= tamaño_int < fin: #Comprobamos si el dato que se lee cabe en los intervalos prefijos.
                resultado[tipo].append(tamaño_int) #Se agrega el resultado a la lista vacia tipo.
                break #Salimos del bucle.
    #Calculamos promedio y mediana.
    promedios = {} #Diccionario vacio para acumular los promedios de cada etiqueta.
    medianas = {} #Diccionario vacío para acumular las medianas de cada etiqueta
    for tipo, tamaños in resultado.items():#.items sirve para leer lo que esta al interior de cada etiqueta en los diccionarios.
        promedio = sum(tamaños) / len(tamaños) #Calculo del promedio.
        promedios[tipo] = promedio #Indexamos los promedios.
        
        tamaños.sort() #Ordenamos de menor a mayor los tamaños.
        longitud = len(tamaños) #Longitud de cada etiqueta.
        if longitud % 2 == 0: #Se verifica si la longitud es par para calcular el promedio de los dos datos a la mitad.
            mediana = (tamaños[longitud // 2 - 1] + tamaños[longitud // 2]) / 2
        else: #Si no es par, simplemente se toma el dato que divide en dos la longitud.
            mediana = tamaños[longitud // 2]
        medianas[tipo] = mediana

    print("Los promedios respectivos a cada categoría: ", promedios, "\n")
    print("Las medianas respectivas a cada categoría: ", medianas, "\n")
    return resultado


# In[ ]:


def limites(vals):
    """
    Permite agrupar por tipos de galaxia los tamaños que obtuvimos previamente.

    Parámetros
    ----------
    vals : list
    » Lista de tamaños de galaxias representados como números enteros.

    Retorna
    ---------
    resultado : dict
    » Un diccionario que contiene los promedios de tamaños para diferentes tipos de galaxias.

    Explicación
    ---------
    Esta función toma una lista de tamaños de galaxias y los agrupa en categorías (SBa, SBb, SBc, Irr)
    basadas en intervalos encontrados en internet y el archivo proveído. Comienza con el diccionario vacío
    llamado resultado donde se irán acumulando los tamaños agrupados. Luego, cada tamaño en la lista se
    verifica con el ciclo for tipo, (inicio, fin), donde este lee el diccionario intervalos proveído y
    verifica en qué categoría entra cada dato que lee. La función retorna el diccionario nuevo y también
    calcula el promedio de tamaños en cada categoría.
    """
    multiplicador = 1.5
    intervalos = {'SBa': (100, 200), 'SBb': (201, 400), 'SBc': (401, 600), 'Irr': (601, 800)}
    resultado = {categoria: [] for categoria in intervalos}

    for valor in vals:
        for categoria, (inicio, fin) in intervalos.items():
            if inicio <= valor <= fin:
                resultado[categoria].append(valor)
                break

    promedios = {categoria: sum(tamanos) / len(tamanos) if tamanos else 0 for categoria, tamanos in resultado.items()}

    Cuartil_1 = promedios['SBa']
    Cuartil_3 = promedios['SBc']

    rango_cuartil = Cuartil_3 - Cuartil_1

    limite_inferior = Cuartil_1 - multiplicador * rango_cuartil
    limite_superior = Cuartil_3 + multiplicador * rango_cuartil

    return {
        'limite_superior': limite_superior,
        'limite_inferior': limite_inferior,
        'promedios': promedios
    }


