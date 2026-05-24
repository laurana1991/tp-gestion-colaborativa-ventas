
import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
ventas = pd.read_csv('datos/ventas.csv')

# Crear columna total
ventas['total_venta'] = ventas['cantidad_vendida'] * ventas['precio']

# Ventas totales
ventas_totales = ventas['total_venta'].sum()

# Producto más vendido
producto_mas_vendido = ventas.groupby('producto')['cantidad_vendida'].sum().idxmax()

# Ventas por mes
ventas['fecha_venta'] = pd.to_datetime(ventas['fecha_venta'])
ventas['mes'] = ventas['fecha_venta'].dt.to_period('M')

ventas_por_mes = ventas.groupby('mes')['total_venta'].sum()

# Mostrar resultados
print("Ventas Totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Gráfico
ventas_por_mes.plot(kind='bar')
plt.title('Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Monto de Ventas')
plt.tight_layout()

# Guardar gráfico
plt.savefig('resultados/grafico_ventas.png')

print("Gráfico guardado en resultados/")
