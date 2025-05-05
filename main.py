import streamlit as st
import re
import string
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the model and vectorizer
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
analyzer = SentimentIntensityAnalyzer()

# Set the page configuration
st.title("📰 Clasificador de Noticias - Real o Falsa")
st.write("Ingrese un titular para predecir si es real o falso, confianza y sentimiento. Mejor si el idioma es Inglés.")
st.write("El modelo fue entrenado con un dataset de 20,000 noticias de diferentes fuentes.")

headline = st.text_input("Titular de la noticia:")

if headline:
    clean_headline = headline.lower()
    clean_headline = re.sub(r'[%s]' % re.escape(string.punctuation), '', clean_headline)
    X_input = vectorizer.transform([clean_headline])
    pred = model.predict(X_input)[0]
    prob = model.predict_proba(X_input)[0].max()
    sentiment = analyzer.polarity_scores(headline)['compound']
    
    st.subheader("Resultados")
    st.write("**Clasificación:**", "✅ Real" if pred == 1 else "❌ Falsa")
    st.write("**Confianza:**", round(prob, 2))
    st.write("**Sentimiento:**", sentiment)