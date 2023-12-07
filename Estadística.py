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


# In[5]:


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
    iqr = Q3 - Q1
    return float(iqr)

