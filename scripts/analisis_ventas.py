
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Definición de rutas relativas para mantener la reproducibilidad del proyecto
RUTA_DATOS = Path("datos/ventas.csv")
RUTA_RESULTADOS = Path("resultados")
RUTA_GRAFICO = RUTA_RESULTADOS / "grafico_ventas.png"
RUTA_RESUMEN = RUTA_RESULTADOS / "resumen_ventas.txt"

# Validación de existencia del archivo de datos
if not RUTA_DATOS.exists():
    raise FileNotFoundError("No se encontró el archivo datos/ventas.csv")

# Leer datos
ventas = pd.read_csv(RUTA_DATOS)

# Validación de columnas necesarias para el análisis
columnas_requeridas = {"fecha_venta", "producto", "cantidad_vendida", "precio"}

if not columnas_requeridas.issubset(ventas.columns):
    raise ValueError("El dataset no contiene todas las columnas requeridas")

# Crear columna total
ventas["total_venta"] = ventas["cantidad_vendida"] * ventas["precio"]

# Ventas totales
ventas_totales = ventas["total_venta"].sum()

# Producto más vendido
producto_mas_vendido = ventas.groupby("producto")["cantidad_vendida"].sum().idxmax()

# Ventas por mes
ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"])
ventas["mes"] = ventas["fecha_venta"].dt.to_period("M")

ventas_por_mes = ventas.groupby("mes")["total_venta"].sum()

# Mostrar resultados
print("Ventas Totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Crear carpeta de resultados si no existe
RUTA_RESULTADOS.mkdir(exist_ok=True)

# Guardar resumen en archivo de texto
with open(RUTA_RESUMEN, "w", encoding="utf-8") as archivo:
    archivo.write("Resumen del análisis de ventas\n")
    archivo.write("--------------------------------\n")
    archivo.write(f"Ventas totales: {ventas_totales}\n")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}\n")

# Gráfico
ventas_por_mes.plot(kind="bar")
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto de Ventas")
plt.tight_layout()

# Guardar gráfico
plt.savefig(RUTA_GRAFICO)

print("Gráfico guardado en resultados/")
print("Resumen guardado en resultados/resumen_ventas.txt")
