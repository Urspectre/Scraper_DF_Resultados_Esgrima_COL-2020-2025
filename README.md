# Análisis de Deserción en la Federación Colombiana de Esgrima (2020–2024)

Este repositorio contiene el proyecto completo de Business Analytics enfocado en analizar y predecir la deserción de deportistas de la categoría de mayores dentro de la Federación Colombiana de Esgrima.  
El análisis combina **web scraping, ETL, EDA, modelos predictivos y visualización**, integrando Python, BigQuery y Power BI.

## 📂 Estructura del repositorio

```
📁 Datasets
📁 EDA y Analisis Diagnostico
📁 Modelos
📁 Scrapper
📄 Proyecto_Final_Nikolai_Torres_Julian_Almario.pdf
```

## Objetivo general

Analizar los factores que influyen en la deserción de deportistas en la categoría de mayores e identificar patrones y predicciones que permitan a la Federación tomar decisiones basadas en datos.

##  Resumen del enfoque

###  1. Web Scraping  
Obtención automática de resultados desde:

https://sistemainfo.fedesgrimacolombia.com/resultados

###  2. ETL en BigQuery  
- Limpieza de datos  
- Cálculo de edad  
- Integración de costos  
- Consolidación de participación por deportista  

###  3. EDA & Diagnóstico  
- Tasa de deserción por arma, liga y género  
- Impacto económico  
- Patrones por edad, arma y frecuencia competitiva  

###  4. Modelos Predictivos  
Se implementaron 3 modelos:

| Modelo | Tipo | Métrica | Resultado |
|--------|------|----------|-----------|
| Decision Tree Regressor | Regresión | R² | 0.99 |
| Decision Tree Classifier | Clasificación | ROC AUC | 0.9987 |
| Random Forest Classifier | Clasificación | ROC AUC | 1.0 |

El Random Forest fue el mejor modelo predictivo.

##  Dashboard Power BI

Incluye:
- Tasa de deserción  
- Impacto económico  
- Comparación por armas  
- Evolución temporal  
- Variables explicativas  

##  Hallazgos clave

- El predictor más fuerte de deserción es la frecuencia de participación.  
- La edad crítica está entre 21 y 24 años.  
- El impacto económico acumulado supera los 340 millones COP.  
- Las armas con mayor deserción: florete y sable.  
- Las ligas con más deserción: Cesar, Santander, Panamá.

## 🛠 Tecnologías utilizadas

- Python  
- Pandas / NumPy  
- Scikit-Learn  
- BeautifulSoup  
- Google BigQuery  
- Matplotlib  
- Power BI  

##  Documento Final  
El informe completo se encuentra en:

Proyecto_Final_Nikolai_Torres_Julian_Almario.pdf
