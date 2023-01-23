'''
Ejercicio 7
El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:
'''
import pandas as pd


# Generar un DataFrame con los datos del fichero.
titanic = 'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv'
df = pd.read_csv(titanic)

# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, 
# los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print(f'Dimensiones del DataFrame: \n{df.shape}\n')
print(f'Número de datos que contiene, nombres de sus columnas y filas y tipos de datos de las columnas\n{df.info()}\n')
print(f'10 primeras filas:\n{df.head()}\n')
print(f'10 últimas filas\n{df.tail()}\n')

# Mostrar por pantalla los datos del pasajero con identificador 148.
print(f'Datos del pasajero con identificador 148:\n{df.loc[df["PassengerId"] == 148]}\n')

# Mostrar por pantalla las filas pares del DataFrame.
print(f'Filas pares:\n{df.loc[df.index % 2 == 0]}\n')

# Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
primera_clase = df.loc[df["Pclass"] == 1]
segunda_clase = df.loc[df["Pclass"] == 2]
tercera_clase = df.loc[df["Pclass"] == 3]
print(f'Nombres de las personas que iban en primera clase ordenadas alfabéticamente\n{primera_clase["Name"].sort_values().to_string(index=False)}\n')

# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
survived = df['Survived'].loc[df["Survived"] == 1].sum()
survived_1 = primera_clase['Survived'].loc[primera_clase['Survived'] == 1].sum()
survived_2 = segunda_clase['Survived'].loc[segunda_clase['Survived'] == 1].sum()
survived_3 = tercera_clase['Survived'].loc[tercera_clase['Survived'] == 1].sum()
total = df['PassengerId'].iloc[-1]
print(f'Porcentaje de personas que sobrevivieron: {survived / total * 100 : .2f}% y que murieron: {(total - survived) / total * 100 : .2f}%')

# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
print(f'Porcentaje de personas que sobrevivieron en cada clase:\nPrimera clase: {survived_1 / total * 100 : .2f}%\nSegunda clase: {survived_2 / total * 100 : .2f}%\nTercera clase: {survived_3 / total * 100 : .2f}%')

#Eliminar del DataFrame los pasajeros con edad desconocida.
df.dropna(subset="Age", inplace=True)

# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print(f"Edad media de las mujeres en 1ra clase: {primera_clase['Age'].mean() : .2f} %")
print(f"Edad media de las mujeres en 2da clase: {segunda_clase['Age'].mean() : .2f} %")
print(f"Edad media de las mujeres en 3ra clase: {tercera_clase['Age'].mean() : .2f} %")

# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df.loc[df['Age'] < 18, 'Underage'] = True
df.loc[df['Age'] >= 18, 'Underage'] = False

# Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
menores_sup_primera = df.loc[(df['Underage'] == True) & (df['Pclass'] == 1)].Survived.sum()
menores_sup_segunda = df.loc[(df['Underage'] == True) & (df['Pclass'] == 2)].Survived.sum()
menores_sup_tercera = df.loc[(df['Underage'] == True) & (df['Pclass'] == 3)].Survived.sum()

print(f"% de menores que sobrevivieron en 1ra clase: {menores_sup_primera / primera_clase.Name.count() * 100 : .2f} %")
print(f"% de menores que sobrevivieron en 2da clase: {menores_sup_segunda / segunda_clase.Name.count() * 100 : .2f} %")
print(f"% de menores que sobrevivieron en 3ra clase: {menores_sup_tercera / tercera_clase.Name.count() * 100 : .2f} %")
print(f"% de mayores que sobrevivieron en 1ra clase: {(survived_1 - menores_sup_primera) / primera_clase.Name.count() * 100 : .2f} %")
print(f"% de mayores que sobrevivieron en 2da clase: {(survived_2 - menores_sup_segunda) / segunda_clase.Name.count() * 100 : .2f} %")
print(f"% de mayores que sobrevivieron en 3ra clase: {(survived_3 - menores_sup_tercera) / tercera_clase.Name.count() * 100 : .2f} %")
