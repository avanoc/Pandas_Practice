'''
Ejercicio 6
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 

nombre (nombre de la empresa), 
Final (precio de la acción al cierre de bolsa), 
Máximo (precio máximo de la acción durante la jornada), 
Mínimo (precio mínimo de la acción durante la jornada), 
volumen (Volumen al cierre de bolsa), 
Efectivo (capitalización al cierre en miles de euros). 

Construir una función que construya un DataFrame a partir del un fichero con el formato anterior 
y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.
'''
import pandas as pd

def crear_df(csv):
    mi_df = pd.read_csv(csv, sep=';', decimal=',')
    mi_df.drop(columns=['Nombre', 'Final', 'Volumen', 'Efectivo'], inplace=True)
    mi_df['Media'] = mi_df.mean(axis=1)
    return mi_df

cotizacion = 'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv'
nuevo_df = crear_df(cotizacion)
print(nuevo_df.head())