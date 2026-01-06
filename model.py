import pandas as pd
import unicodedata
import re

from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

# =====================
# Configuración
# =====================

FEATURES = [
    "stat_goals",
    "conversion_remate",
    "calidad_de_remate",
    "stat_onTargetScoringAttempt",
    "generador_ocasiones",
    "participacion_ofensiva",
    "solidez_defensiva",
    "rating_avg"
]

# =====================
# Utilidades
# =====================

def clean_name(text):
    text = str(text).lower().strip()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"\s+", " ", text)
    return text


def scale_features(df, features):
    scaler = StandardScaler()
    return scaler.fit_transform(df[features])

# =====================
# Cargar y preparar data
# =====================

df = pd.read_csv("chile_players_2025_agg.csv")

df_model = df.copy()
df_model = df_model[df_model["minutes_played_total"] >= 500].copy()
df_model["player_name_clean"] = df_model["player_name"].apply(clean_name)
df_model = df_model.dropna(subset=FEATURES)
df_model.reset_index(drop=True, inplace=True)

# =====================
# Motor de similitud
# =====================

def compute_similarity(df_model, player_name, features, top_n=15):

    player_clean = clean_name(player_name)

    if player_clean not in df_model["player_name_clean"].values:
        suggestions = get_close_matches(
            player_clean,
            df_model["player_name_clean"].unique(),
            n=3,
            cutoff=0.6
        )
        raise ValueError(
            f"Jugador no encontrado. ¿Quisiste decir?: {suggestions}"
        )

    X = scale_features(df_model, features)
    sim_matrix = cosine_similarity(X)

    idx = df_model.index[
        df_model["player_name_clean"] == player_clean
    ][0]

    scores = list(enumerate(sim_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:top_n+1]

    result = df_model.iloc[[i[0] for i in scores]][
        ["player_name", "team_name", "minutes_played_total"]
    ].copy()

    result["similarity_%"] = [round(i[1]*100, 1) for i in scores]

    return result