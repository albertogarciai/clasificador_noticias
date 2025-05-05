# 📰 Clasificador de Titulares de Noticias

Este proyecto utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) para construir un modelo capaz de clasificar titulares de noticias como reales o falsas. Además, incluye análisis de sentimiento y una aplicación interactiva desarrollada en Streamlit.

## 🚀 Características principales

- **Preprocesamiento de texto:** limpieza, normalización, tokenización y lematización.
- **Vectorización:** implementación de TF-IDF para convertir texto en vectores numéricos.
- **Modelado:** entrenamiento de modelos de clasificación (Logistic Regression y Random Forest).
- **Análisis de sentimientos:** integración de VADER para determinar el tono emocional de los titulares.
- **Aplicación web:** app en Streamlit para clasificación en tiempo real y visualización de resultados.

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/albertogarciai/clasificador_noticias.git
cd clasificador_noticias
```

2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## 🧠 Uso

### Entrenamiento

Ejecuta el notebook para:

- Preprocesar los datos.
- Entrenar y evaluar los modelos.
- Guardar el modelo y el vectorizador entrenados.

```bash
jupyter notebook clasificacion_noticias_nlp.ipynb
```

### Aplicación Streamlit

Lanza la aplicación web para realizar predicciones en tiempo real:

```bash
streamlit run app.py
```

La aplicación permite:

- Ingresar un titular y predecir si es real o falso.
- Mostrar la confianza del modelo.
- Visualizar el análisis de sentimiento del titular.

## 📁 Estructura del proyecto

```
├── dataset/
│   ├── training_data.csv
│   └── testing_data.csv
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
├── app.py
├── clasificacion_noticias_nlp.ipynb
├── requirements.txt
└── README.md
```

## 📌 Notas adicionales

- Los modelos y vectorizadores entrenados se almacenan en la carpeta `models`.
- El análisis de sentimiento es orientativo y puede ser complementado con técnicas adicionales.
- Preparado para despliegue en Streamlit Cloud con ajustes mínimos.

---

**Autor:** [@albertogarciai]