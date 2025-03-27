import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error


st.title("Analyse des Données Beans & Pods")



def load_data():
    data = pd.read_csv('BeansDataSet.csv')  
    return data

data = load_data()


columns_for_total_sales = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']


missing_columns = [col for col in columns_for_total_sales if col not in data.columns]
if missing_columns:
    st.warning(f"Les colonnes suivantes sont manquantes : {missing_columns}. Elles seront ignorées dans le calcul des ventes totales.")
    columns_for_total_sales = [col for col in columns_for_total_sales if col in data.columns]


data['TotalSales'] = data[columns_for_total_sales].sum(axis=1)


st.sidebar.title("Navigation")
menu = st.sidebar.selectbox("Choisissez une section", ["Accueil", "Exploration des Données", "Tendances Clés", "Recommandations", "Données Supplémentaires"])


if menu == "Accueil":
    st.header("Bienvenue dans l'analyse des données Beans & Pods")
    st.write("""
            Beans & Pods, un fournisseur familial en plein essor, se spécialise dans les grains de café de qualité et les gousses.
            Cette application innovante offre un accès approfondi aux données de ventes 
             et propose des recommandations personnalisées pour des campagnes de marketing ciblées et percutantes
    """)
    st.write("**Jeu de données :**")
    st.write(data.head())


elif menu == "Exploration des Données":
    st.header("Exploration des Données")
    
    
    if st.checkbox("Afficher les données brutes"):
        st.write(data)
    
    
    st.subheader("Statistiques Descriptives")
    st.write(data.describe())


elif menu == "Tendances Clés":
    st.header("Tendances Clés dans les Données")
    
    
    st.subheader("Ventes par Canal")
    sales_by_channel = data.groupby('Channel')['TotalSales'].sum()
    st.bar_chart(sales_by_channel)
    st.write("""
    **Observation :** Les ventes en magasin sont plus élevées que les ventes en ligne.
    """)
    
    
    ventes_par_canal = data.groupby('Channel').sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ventes_par_canal[columns_for_total_sales].plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Ventes Totales par Canal')
    ax.set_ylabel('Ventes')
    ax.set_xlabel('Canal')
    ax.legend(loc='upper right')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)
    st.write("""
    **Observation :** 
            le Robusta est le produit le plus vendu en magasin tandis que l'Espresso  est le plus vendu en ligne
            le Lungo est moins vendu en ligne et plus vendu en ligne
            le Latte est plus vendu en ligne que en magasin
            le Cappuccino est plus vendu en magasin que en ligne
            l'Arabica est plus vendu en ligne que en magasin
            le Robusta est plus vendu en magasin que en ligne
            l'Espresso est plus vendu en ligne que en magasin .
    """)
    
    
    st.subheader("Ventes par Région")
    sales_by_region = data.groupby('Region')['TotalSales'].sum()
    st.bar_chart(sales_by_region)
    st.write("""
    **Observation :** La région Sud génère le plus de ventes, suivie par le Nord et le Centre.
    """)
    
    
    ventes_par_region = data.groupby('Region').sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ventes_par_region[columns_for_total_sales].plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Ventes Totales par Région')
    ax.set_ylabel('Ventes')
    ax.set_xlabel('Région')
    ax.legend(loc='upper right')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)
    st.write("""
    **Observation :** La région Sud génère le plus de ventes de tous les different types de café, le café le plus vendu dans tout les region sont:
             1-le Robusta
             2-L'Arabica
             3-L'Espresso .
    """)
    
    
    st.subheader("Ventes par Produit")
    product_sales = data[columns_for_total_sales].sum()
    st.bar_chart(product_sales)
    st.write("""
    **Observation :** Les produits les plus vendus sont le Robusta et l'Espresso.
    """)
    
    


elif menu == "Recommandations":
    st.header("Recommandations pour la Campagne Marketing")
    st.write("""
    **Sur la base des tendances identifiées, voici nos recommandations** :
    
    1. **Cibler les régions avec les ventes les faibles** :
        - Renforcer les campagnes marketing dans les régions Nord et Centre.
        - Maintenir et améliorer les campagnes dans la région Sud.
        - Promouvoir les produits populaires et offrir des promotions spéciales pour les produits moins populaires.
        - Collecter des données supplémentaires: dates de transaction, informations démographiques sur les clients, et feedback client.
        
    
    2. **Promouvoir les produits les plus vendus** :
       - Mettre en avant le Lungo et le Cappuccino dans les campagnes publicitaires.
       - Offrir des promotions sur ces produits pour stimuler davantage les ventes.
    
    3. **Renforcer la présence en ligne** :
       - Étant donné que les ventes en magasin sont plus élevées, investir dans des campagnes digitales (réseaux sociaux, publicités en ligne).
       - Améliorer l'expérience utilisateur sur la plateforme en ligne.
    """)


elif menu == "Données Supplémentaires":
    st.header("Données Supplémentaires à Collecter")
    st.write("""
             
    Pour améliorer l'analyse et les décisions marketing, nous recommandons de collecter les données suivantes :
    
    1. **Données démographiques des clients** :
       - Âge, sexe, revenu, etc.
       - Ces données aideront à mieux comprendre le profil des clients et à personnaliser les campagnes.
    
    2. **Données sur les habitudes d'achat** :
       - Fréquence d'achat, montant moyen dépensé, etc.
       - Ces données permettront d'identifier les clients fidèles et de cibler les promotions.
    
    3. **Données sur les préférences des clients** :
       - Préférences en matière de goût, d'emballage, etc.
       - Ces données aideront à développer de nouveaux produits et à améliorer les produits existants.
       -Données de satisfaction client: Retours sur les produits et services.
    """)


st.sidebar.header("Conclusion")
st.sidebar.write("""
    ****Beans & Pods** est une entreprise en pleine croissance avec un fort potentiel de développement.
    En analysant les données de ventes et en identifiant les tendances clés, nous avons pu formuler des recommandations
    pour des campagnes marketing ciblées et efficaces.
    Pour aller plus loin, nous recommandons de collecter des données supplémentaires sur les clients et leurs préférences.
                 Nous avons constaté les ventes en magasin sont plus élevées que les ventes en ligne.
                 La région Sud génère le plus de ventes, suivie par le Nord et le Centre.
                 Les produits les plus vendus sont le Robusta et l'Espresso.
                 Pour améliorer l'analyse et les décisions marketing, nous recommandons de collecter les données suivantes :
                 Données démographiques des clients : age, sexe, revenu car ces données aideront à mieux comprendre le profil des clients et à personnaliser les campagnes.
                 par exemple l'age et le sexe des clients peuvent permettre de cibler les promotions et savoir la tranche d'age qui consomme le plus de café et l'achete en ligne ou en magasin.
    Nous espérons que nos analyses et nos recommandations vous aideront à améliorer votre business et à réduire les coûts d'entrée.
    merci pour votre attention.**
""")
