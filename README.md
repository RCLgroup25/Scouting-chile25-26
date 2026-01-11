⚽ Scouting Chile 2025 — Player Similarity Engine
📌 Descripción general
Este proyecto es un motor de búsqueda de jugadores similares aplicado al fútbol chileno (Primera División y Primera B), construido bajo un enfoque Moneyball, es decir:
comparar jugadores por impacto estadístico real, sin depender de la posición nominal ni de etiquetas subjetivas.

La herramienta permite, a partir de un jugador de referencia, encontrar perfiles estadísticamente similares, facilitando procesos de:
scouting
reemplazo de jugadores
identificación de talento subvalorado
análisis comparativo entre ligas y equipos

🎯 Objetivo del proyecto
Desarrollar una herramienta práctica de scouting basada en datos, que transforme estadísticas individuales en un producto usable, replicable y adaptable a cualquier liga.
El foco no está en la predicción, sino en:
comparabilidad
interpretabilidad
toma de decisiones deportivas

🧠 Enfoque metodológico
El modelo utiliza:
Feature engineering propio, combinando métricas ofensivas, defensivas y de participación.
Normalización estadística (StandardScaler) para evitar sesgos por escala.
Cosine Similarity como métrica principal para medir similitud entre jugadores.
Filtro por minutos jugados para asegurar muestras representativas.
Búsqueda robusta de nombres, tolerante a mayúsculas/minúsculas y errores de escritura.

👉 No se utilizan roles fijos ni posiciones tradicionales:
los jugadores se comparan por lo que hacen en cancha, no por cómo están etiquetados.

📊 Features utilizadas
Las variables base del modelo incluyen:
stat_goals
conversion_remate
calidad_de_remate
stat_onTargetScoringAttempt
generador_ocasiones
participacion_ofensiva
solidez_defensiva
rating_avg

Estas métricas representan:

producción ofensiva
eficiencia
volumen de acciones
aporte defensivo
rendimiento global

🔎 Funcionamiento del buscador

El usuario ingresa el nombre de un jugador.

El sistema:
valida el nombre (búsqueda flexible)
filtra jugadores con minutos suficientes
normaliza las métricas
Se calcula la similitud coseno entre jugadores.

Se devuelve un ranking de jugadores similares con:
nombre
equipo
liga
porcentaje de similitud

🖥️ Interfaz

El proyecto cuenta con:

desarrollo completo en Jupyter Notebook
versión funcional en Streamlit (demo local)
visualizaciones de apoyo en Tableau Public

🛠️ Stack tecnológico

Python
pandas / numpy
scikit-learn
Streamlit
Jupyter Notebook
Tableau Public
Web scraping (Sofascore)

📈 Casos de uso

🔍 Scouting de reemplazos ante salidas de jugadores
💰 Identificación de perfiles de bajo costo y alto impacto
📊 Comparación entre ligas (Primera vs Primera B)
🧠 Apoyo a decisiones deportivas en clubes y agencias
🧪 Base para futuros modelos predictivos o de valoración económica
🚀 Proyección del proyecto

El modelo está diseñado para ser:

escalable a otras ligas
integrable con datos económicos (valor de mercado, edad)
adaptable a distintos criterios de similitud
evolucionable hacia una plataforma de scouting completa

👤 Autor

Diego Gutiérrez
Analista de Datos | Scouting & Football Analytics RCLgroup.

Proyecto desarrollado como iniciativa personal y en colaboración con comunidades de scouting, con foco en análisis aplicado y toma de decisiones deportivas.
