import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

total_genes = 244

data=pd.read_csv('DEG/Go_up_down/GO_PrE_up_biological_process.txt', sep= '\t')

# Calculer le gene ratio
data['gene_ratio'] = data['genes'] / total_genes

# Trier les données par valeur de p
data = data.sort_values(by='gene_ratio', ascending=False)

# Configurer la taille de la figure
plt.figure(figsize=(12, 8))

# Créer le graphique en points
scatter = sns.scatterplot(
    x='gene_ratio', 
    y='GO_term', 
    size='genes', 
    sizes=(20, 1500),
    data=data, 
    hue='p_value',
    palette='viridis',
    legend=False
)

# Ajouter des labels et un titre pour le graphique principal
plt.xlabel('Gene Ratio')
plt.ylabel('GO Terms')
plt.title('Top Enriched GO Terms')

# Ajouter la barre de couleur pour les p-values à droite
norm = plt.Normalize(data['p_value'].min(), data['p_value'].max())
sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
sm.set_array([])  # Ajoute un mappable vide pour générer une colorbar

# Obtenir l'axe actuel
ax = plt.gca()

# Ajouter la colorbar verticale à droite du graphique principal
cbar = plt.colorbar(sm, ax=ax, orientation='vertical', pad=0.01, fraction=0.05, anchor=(0, 0.3), shrink=0.5)
cbar.set_label('p-value')

# Ajouter les points pour le nombre de gènes à droite du graphique
plt.scatter([], [], s=5, label='5', color='black')
plt.scatter([], [], s=50, label='50', color='black')
plt.scatter([], [], s=100, label='100', color='black')
plt.scatter([], [], s=500, label='500', color='black')
plt.scatter([], [], s=1000, label='1000', color='black')

# Ajouter une légende pour le nombre de gènes au-dessus de la colorbar
plt.legend(loc='upper left', title='Number of Genes', bbox_to_anchor=(1, 1), ncol=3)

# Ajuster la disposition pour empêcher le chevauchement
plt.tight_layout()

# Afficher le graphique
plt.show()
