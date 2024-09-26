import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analyse des rôles", layout="wide")

# CSS personnalisé pour centrer le contenu
st.markdown("""
<style>
.centered {
    display: flex;
    justify-content: center;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Utilisation de colonnes pour centrer le contenu
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    st.title("Mercato 2025 - Simon 'Baguette'")

    # Ajout de l'image
    #st.image("chemin/vers/votre/gif.gif", caption="Légende du GIF", use_column_width=True)

    st.write("Data provided by gol GG - https://gol.gg/esports/home/")

    # Vous pouvez ajouter ici du contenu général pour la page d'accueil

    # Fonction pour charger les données (à adapter selon vos besoins)
    @st.cache_data
    def load_data():
        # Chargez vos données ici
        # Par exemple :
        df = pd.read_csv("data\Toplane.csv")
        return df

    # Vous pouvez afficher des statistiques générales ou un aperçu ici si vous le souhaitez

    # Ajout du lien Twitter
    st.markdown("Follow me on Twitter : [@BaguetteCoach](https://x.com/BaguetteCoach)")

    # Vous pouvez également ajouter un widget Twitter si vous le souhaitez
    st.components.v1.html("""
<a class="twitter-timeline" data-width="400" data-height="500" href="https://twitter.com/BaguetteCoach?ref_src=twsrc%5Etfw">Tweets by BaguetteCoach</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
""", height=500)

    st.markdown('</div>', unsafe_allow_html=True)