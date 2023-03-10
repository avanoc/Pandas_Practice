'''
Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, 
contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 
2016, 2017, 2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:
'''

import pandas as pd
import numpy as np

# Generar un DataFrame con los datos de los cuatro ficheros:
emisiones_2016 = pd.read_csv('https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2016.csv', sep=';', decimal=',')
emisiones_2017 = pd.read_csv('https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2017.csv', sep=';', decimal=',')
emisiones_2018 = pd.read_csv('https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2018.csv', sep=';', decimal=',')
emisiones_2019 = pd.read_csv('https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2019.csv', sep=';', decimal=',')
emisiones = pd.concat([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])

# Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES 
# y las correspondientes a los días D01, D02, etc.
droplist = [dropcol for dropcol in emisiones if 'V' in dropcol] + ['MUNICIPIO'] + ['PUNTO_MUESTREO']
emisiones.drop(columns=droplist, inplace=True)

# Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
emisiones = emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
emisiones['VALOR'] = emisiones.VALOR.astype(float)

# Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
emisiones['FECHA'] = emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.DIA.str.strip('D').apply(str)
emisiones['FECHA'] = pd.to_datetime(emisiones.FECHA, format='%Y/%m/%d', errors='coerce')

# Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones,
# contaminantes (MAGNITUD) y fecha.
emisiones = emisiones.drop(emisiones[np.isnat(emisiones['FECHA']) == True].index)
emisiones.sort_values(by=['ESTACION', 'MAGNITUD', 'FECHA'], inplace=True)

# Mostrar por pantalla las estaciones y los contaminantes (MAGNITUD) disponibles en el DataFrame.
estaciones = emisiones['ESTACION'].unique().tolist()
magnitud = emisiones['MAGNITUD'].unique().tolist()
print(f'Estaciones: {estaciones}\nMagnitud: {magnitud}')

# Crear una función que reciba una estación, un contaminante y un rango de fechas 
# y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
def serie_emisiones(estacion, contaminante, fechas):
    return emisiones.loc[(emisiones['ESTACION'] == estacion) & (emisiones['MAGNITUD'] == contaminante) & (emisiones['FECHA'] == fechas)]

serie_emi = serie_emisiones(4, 1, '2016-01-01')
print(serie_emi)

# Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
for m in magnitud:
    print(f'Resumen descriptivo del contaminante: {m}:')
    print(emisiones.loc[emisiones['MAGNITUD'] == m].VALOR.describe())

# Mostrar un resumen descriptivo para cada contaminante por distritos (ESTACIONES).
for m in magnitud:
    for e in estaciones:
        if not emisiones.loc[(emisiones['MAGNITUD'] == m) & (emisiones['ESTACION'] == e)].empty:
            print(f'Resumen descriptivo del contaminante {m} en la estación {e}:')
            print(emisiones.loc[(emisiones['MAGNITUD'] == m) & (emisiones['ESTACION'] == e)].VALOR.describe())

# Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo 
# de las emisiones del contaminante indicado en la estación indicada.
def resumen(e, m):
    return emisiones.loc[(emisiones['MAGNITUD'] == m) & (emisiones['ESTACION'] == e)].VALOR.describe()

print(resumen(55, 44))

# Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
def media_mensual(m, a):
    filtrado = emisiones[(emisiones['MAGNITUD'] == m) & (emisiones['ANO'] == a)]
    mensual = {}
    for m in range(1, 13):
        mensual[m] = filtrado[filtrado['MES'] == m].VALOR.mean()
    return mensual

print(media_mensual(1, 2016))

# Crear un función que reciba una estación de medición y devuelva un DataFrame 
# con las medias mensuales de los distintos tipos de contaminantes.
def media_mensual_estacion(e):
    filtrado = emisiones[emisiones['ESTACION'] == e]
    contaminante = {}
    for m in magnitud:
        mensual = {}
        for mes in range(1, 13):
            mensual[mes] = filtrado[filtrado['MES'] == mes].VALOR.mean()
        contaminante[m] = mensual
    return pd.DataFrame(contaminante)

print(media_mensual_estacion(4))