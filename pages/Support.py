import streamlit as st
import pandas as pd
import numpy as np

st.title("Support")

# Chargez les données spécifiques au Support
df_sup = pd.read_csv("data/Support.csv")

# Supprimez la colonne "Country"
if 'Country' in df_sup.columns:
    df_sup = df_sup.drop(columns=['Country'])

# Option pour supprimer les joueurs avec des valeurs NaN
remove_nan = st.sidebar.checkbox("Supprimer les joueurs avec des valeurs manquantes")
if remove_nan:
    df_sup = df_sup.dropna()

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
for column in df_sup.columns:
    if pd.api.types.is_numeric_dtype(df_sup[column]):
        filters[column] = create_numeric_filter(df_sup, column)
    else:
        filters[column] = create_categorical_filter(df_sup, column)

# Appliquez les filtres
for column, filter_value in filters.items():
    if isinstance(filter_value, tuple):  # Pour les filtres numériques
        df_sup = df_sup[(df_sup[column] >= filter_value[0]) & (df_sup[column] <= filter_value[1])]
    elif isinstance(filter_value, list) and 'Tous' not in filter_value:  # Pour les filtres catégoriels
        df_sup = df_sup[df_sup[column].isin(filter_value)]

# Affichez les données filtrées
st.dataframe(df_sup)

# Ajoutez d'autres éléments spécifiques au Support
# Par exemple :
# st.line_chart(df_sup["some_column"])