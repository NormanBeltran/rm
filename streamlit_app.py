import streamlit as st
import google.generativeai as genai

st.title("Recetas del mundo")

# Diccionario de banderas
banderas = {
    "Argentina": "https://flagcdn.com/w320/ar.png",
    "Bolivia": "https://flagcdn.com/w320/bo.png",
    "Brasil": "https://flagcdn.com/w320/br.png",
    "Chile": "https://flagcdn.com/w320/cl.png",
    "Colombia": "https://flagcdn.com/w320/co.png",
    "Ecuador": "https://flagcdn.com/w320/ec.png",
    "Guyana": "https://flagcdn.com/w320/gy.png",
    "Paraguay": "https://flagcdn.com/w320/py.png",
    "Perú": "https://flagcdn.com/w320/pe.png",
    "Surinam": "https://flagcdn.com/w320/sr.png",
    "Uruguay": "https://flagcdn.com/w320/uy.png",
    "Venezuela": "https://flagcdn.com/w320/ve.png",
    "Estados Unidos": "https://flagcdn.com/w320/us.png",
    "Canadá": "https://flagcdn.com/w320/ca.png",
    "México": "https://flagcdn.com/w320/mx.png",
    "Guatemala": "https://flagcdn.com/w320/gt.png",
    "Honduras": "https://flagcdn.com/w320/hn.png",
    "El Salvador": "https://flagcdn.com/w320/sv.png",
    "Nicaragua": "https://flagcdn.com/w320/ni.png",
    "Costa Rica": "https://flagcdn.com/w320/cr.png",
    "Panamá": "https://flagcdn.com/w320/pa.png",
    "Cuba": "https://flagcdn.com/w320/cu.png",
    "República Dominicana": "https://flagcdn.com/w320/do.png",
    "Haití": "https://flagcdn.com/w320/ht.png",
    "Puerto Rico": "https://flagcdn.com/w320/pr.png",
    "Jamaica": "https://flagcdn.com/w320/jm.png",
    "Trinidad y Tobago": "https://flagcdn.com/w320/tt.png",
    "España": "https://flagcdn.com/w320/es.png",
    "Portugal": "https://flagcdn.com/w320/pt.png",
    "Francia": "https://flagcdn.com/w320/fr.png",
    "Italia": "https://flagcdn.com/w320/it.png",
    "Alemania": "https://flagcdn.com/w320/de.png",
    "Reino Unido": "https://flagcdn.com/w320/gb.png",
    "Irlanda": "https://flagcdn.com/w320/ie.png",
    "Grecia": "https://flagcdn.com/w320/gr.png",
    "Rusia": "https://flagcdn.com/w320/ru.png",
    "China": "https://flagcdn.com/w320/cn.png",
    "Japón": "https://flagcdn.com/w320/jp.png",
    "India": "https://flagcdn.com/w320/in.png",
    "Australia": "https://flagcdn.com/w320/au.png",
    "Nueva Zelanda": "https://flagcdn.com/w320/nz.png",
    "Sudáfrica": "https://flagcdn.com/w320/za.png",
    "Egipto": "https://flagcdn.com/w320/eg.png",
    "Nigeria": "https://flagcdn.com/w320/ng.png"
}

# Lista de países
paises = list(banderas.keys())

# Selección del país
pais_seleccionado = st.selectbox("Selecciona un país:", paises)

# Mostrar la bandera del país seleccionado
if pais_seleccionado:
    st.image(banderas[pais_seleccionado], width=100)

# Clave de la API de Gemini
gemini_api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)

# Modelo de Gemini
model = genai.GenerativeModel('gemini-2.0-flash')

# Contexto del modelo
contexto = "Eres un experto cocinero mundial, y conoces de recetas típicas de cada país."

# Botón para generar la receta
if st.button("A cocinar"):
    # Generar respuesta
    if pais_seleccionado:
        prompt = f"{contexto} Dame una receta de cocina típica de {pais_seleccionado}."
        response = model.generate_content(prompt)
        st.write("Receta:", response.text)

# Estilo de fondo
st.markdown(
    """
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1495195134817-aeb325a55b65?q=80&w=2076&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
