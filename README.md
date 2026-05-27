# TP Gestión Colaborativa - Análisis de Ventas

## Integrantes
- Ana Laura Mansilla
- Gonzalo Gomez

## Materia
Organización Empresarial - UTN TUP a Distancia

## Escenario elegido
Escenario B – Análisis de Ventas de una Pequeña Empresa

## Descripción del proyecto
Este proyecto tiene como objetivo analizar un conjunto de datos simulados de ventas comerciales mediante Python.

El análisis realizado incluye:
- cálculo de ventas totales;
- identificación del producto más vendido;
- análisis de ventas por mes;
- generación de un gráfico de ventas mensuales;
- generación de un archivo resumen con los principales resultados.

## Estructura del proyecto

tp-gestion-colaborativa-ventas/

├── datos/
│   └── ventas.csv

├── scripts/
│   └── analisis_ventas.py

├── resultados/
│   ├── grafico_ventas.png
│   └── resumen_ventas.txt

├── README.md

└── .gitignore

## Dataset utilizado
Se utilizó un dataset de ventas simulado en formato CSV para representar registros comerciales simples.

El archivo contiene:
- fecha de venta;
- producto;
- cantidad vendida;
- precio unitario.

## Tecnologías utilizadas
- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Jira
- Google Colab

## Flujo de trabajo colaborativo
El trabajo se organizó mediante un tablero Kanban en Jira, donde se crearon tareas asociadas a la estructura del proyecto, el desarrollo del análisis, la documentación y la revisión QA.

Para mantener la trazabilidad, los commits se vincularon con los identificadores de las tareas de Jira. Durante la revisión final se normalizó el uso del prefijo KAN correspondiente al tablero del proyecto.

También se utilizó una rama específica para las tareas de revisión y documentación:

feature/qa-documentacion

Esta rama permitió incorporar mejoras sin modificar directamente la rama principal.

## Mejoras QA incorporadas
Durante la etapa de revisión QA se realizaron las siguientes mejoras:
- validación de existencia del archivo datos/ventas.csv;
- validación de columnas requeridas;
- uso de rutas relativas mediante pathlib;
- generación automática de la carpeta resultados;
- generación de archivo resumen_ventas.txt;
- revisión de reproducibilidad del script en Google Colab.

## Instrucciones de ejecución

1. Clonar el repositorio:

git clone https://github.com/laurana1991/tp-gestion-colaborativa-ventas.git

2. Ingresar a la carpeta del proyecto:

cd tp-gestion-colaborativa-ventas

3. Ejecutar el script:

python scripts/analisis_ventas.py

4. Consultar resultados:

Los resultados se guardan en la carpeta resultados:
- grafico_ventas.png
- resumen_ventas.txt

## Resultados obtenidos
El script calcula las ventas totales, identifica el producto más vendido y genera un gráfico que representa la evolución mensual de las ventas.

Además, se genera un archivo de texto con un resumen de los principales resultados del análisis.
