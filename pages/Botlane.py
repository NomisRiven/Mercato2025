import streamlit as st
import pandas as pd
import numpy as np

st.title("Botlane")

# Chargez les données spécifiques à la Botlane
df_bot = pd.read_csv("data/Botlane.csv")

# Supprimez la colonne "Country"
if 'Country' in df_bot.columns:
    df_bot = df_bot.drop(columns=['Country'])

# Option pour supprimer les joueurs avec des valeurs NaN
remove_nan = st.sidebar.checkbox("Supprimer les joueurs avec des valeurs manquantes")
if remove_nan:
    df_bot = df_bot.dropna()

# Créez des sélecteurs pour chaque colonne numérique
st.sidebar.header("Filtres")

# Fonction pour créer un sélecteur pour une colonne numérique
def create_numeric_filter(df, column):
    values = df[column].dropna()
    if len(values) > 0:
        min_value = float(values.min())
        max_value = float(values.max())
        step = (max_value - min_value) / 100 if max_value > min_value else 0.01
        return st.sidebar.slider(f"Filtre {column}", min_value, max_value, (min_value, max_value), step=step)
    else:
        st.sidebar.text(f"Pas de données numériques pour {column}")
        return None

# Fonction pour créer un sélecteur pour une colonne catégorielle
def create_categorical_filter(df, column):
    options = ['Tous'] + list(df[column].dropna().unique())
    return st.sidebar.multiselect(f"Filtre {column}", options, default='Tous')

# Créez des filtres pour chaque colonne
filters = {}
for column in df_bot.columns:
    if pd.api.types.is_numeric_dtype(df_bot[column]):
        filters[column] = create_numeric_filter(df_bot, column)
    else:
        filters[column] = create_categorical_filter(df_bot, column)

# Appliquez les filtres
for column, filter_value in filters.items():
    if isinstance(filter_value, tuple):  # Pour les filtres numériques
        df_bot = df_bot[(df_bot[column] >= filter_value[0]) & (df_bot[column] <= filter_value[1])]
    elif isinstance(filter_value, list) and 'Tous' not in filter_value:  # Pour les filtres catégoriels
        df_bot = df_bot[df_bot[column].isin(filter_value)]

# Affichez les données filtrées
st.dataframe(df_bot)

# Ajoutez d'autres éléments spécifiques à la Botlane
# Par exemple :
# st.line_chart(df_bot["some_column"])