import streamlit as st
from model import compute_similarity, FEATURES, df_model

st.set_page_config(
    page_title="Scouting Chile 2025",
    layout="wide"
)

st.title("🔍 Buscador de Jugadores Similares — Chile 2025")

st.markdown(
    """
    **Modelo de similitud tipo Moneyball basado en métricas ofensivas y defensivas.**  
    Comparación estadística sin roles predefinidos.  
    Solo jugadores con ≥500 minutos jugados.
    """
    
)
st.caption(
    f"Universo de comparación: {df_model.shape[0]} jugadores"
)

player = st.text_input(
    "Escribe el nombre del jugador",
    placeholder="Ej: Lucas Cepeda"
)

if st.button("Buscar similares"):
    try:
        result = compute_similarity(df_model, player, FEATURES)
        # 👉 ORDENAR POR SIMILARIDAD
        result = result.sort_values("similarity_%", ascending=False)
        st.dataframe(result, use_container_width=True)
    except ValueError as e:
        st.warning(str(e))