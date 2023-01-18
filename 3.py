'''
Ejercicio 3
Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y 
devuelva una serie con las notas de los alumnos aprobados (> 5) ordenadas de mayor a menor.
'''
import pandas as pd


def aprobados(notas):
    serie_notas = pd.Series(data=notas)
    serie_notas = serie_notas[serie_notas >= 5]
    serie_notas.sort_values(ascending=False, inplace=True)
    return serie_notas

alumnos = {
    'Juan':9, 
    'María':6.5, 
    'Pedro':4, 
    'Carmen': 8.5, 
    'Luis': 5
}
print(aprobados(alumnos))