'''
Ejercicio 5
Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, 
y devuelva el balance (ventas - gastos) total en los meses indicados.
'''
import pandas as pd
import numpy as np


def balancear(df):
    df['Balance'] = df['Ventas'] - df['Gastos']
    return df

datos = {
    'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas':[30500, 35600, 28300, 33900],
    'Gastos':[22000, 23400, 18100, 20700]
}

mi_df = pd.DataFrame(data=datos)
mi_df.set_index('Mes', inplace=True)

print(f'El balance total en los meses indicados es {np.sum(balancear(mi_df))["Balance"]}')