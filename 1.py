'''
Ejercicio 1
Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie 
con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.
'''
import pandas as pd


año_inicio = int(input('Año de incio: '))
año_final = int(input('Año final: '))
ventas = {}
for año in range(año_inicio, año_final + 1):
    venta = float(input(f'¿Cuál fue la venta del año {año}?: '))
    ventas[año] = venta
serie_ventas = pd.Series(data=ventas)
print(f'VENTAS: \n {serie_ventas}')
print(f'VENTAS CON DESCUENTO: \n {serie_ventas * 0.9}')