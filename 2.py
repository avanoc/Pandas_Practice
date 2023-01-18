'''
Ejercicio 2
Escribir una función que reciba un diccionario con las notas de los alumno de un curso y 
devuelva una serie con la nota mínima, la máxima, media y la desviación típica.
'''
import pandas as pd
import numpy as np


def analisis_notas(notas):
    serie_notas = pd.Series(data=notas)
    dic_notas = {
        'minima':np.min(serie_notas),
        'maxima':np.max(serie_notas),
        'media':np.mean(serie_notas),
        'desviacion tipica':np.std(serie_notas)
    }
    return pd.Series(data=dic_notas)

misnotas = {
    'mat': 10,
    'lengua': 9,
    'historia': 7,
    'quimica': 10,
}
print(analisis_notas(misnotas))