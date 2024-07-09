import anndata as ad
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Lecture des données
adata_Deng = ad.read_h5ad('Processing/standardv2/Objects/object_1_Deng_filtered_1.h5ad')
genes_Deng = adata_Deng.obs['n_genes_by_counts'].to_list()

adata_Chen = ad.read_h5ad('Processing/standardv2/Objects/object_2_Chen_filtered_1.h5ad')
genes_Chen = adata_Chen.obs['n_genes_by_counts'].to_list()

adata_Mo = ad.read_h5ad('Processing/standardv2/Objects/object_3_Mohammed_filtered_1.h5ad')
genes_Mo = adata_Mo.obs['n_genes_by_counts'].to_list()

adata_Nowo = ad.read_h5ad('Processing/standardv2/Objects/object_4_Nowo_filtered_1.h5ad')
genes_Nowoa = adata_Nowo.obs['n_genes_by_counts'].to_list()

adata_Nowob = ad.read_h5ad('Processing/standardv2/Objects/object_4bis_Nowo_filtered_1.h5ad')
genes_Nowob = adata_Nowob.obs['n_genes_by_counts'].to_list()

genes_Nowo = genes_Nowoa + genes_Nowob

adata_Posfai = ad.read_h5ad('Processing/standardv2/Objects/object_5_Posfai_filtered_1.h5ad')
genes_Posfai = adata_Posfai.obs['n_genes_by_counts'].to_list()

adata_Arge = ad.read_h5ad('Processing/standardv2/Objects/object_6_Arg_filtered_1.h5ad')
genes_Arge = adata_Arge.obs['n_genes_by_counts'].to_list()

adata_Vrij = ad.read_h5ad('Processing/Vrij/Objects/object_7_Vrij_filtered_1.h5ad')
genes_Vrij = adata_Vrij.obs['n_genes_by_counts'].to_list()

adata_Schu = ad.read_h5ad('Processing/Schu_ssVrij/Objects/object_8_Schu_filtered_1.h5ad')
genes_Schu = adata_Schu.obs['n_genes_by_counts'].to_list()

data = {
    "Deng": genes_Deng,
    "Chen": genes_Chen,
    "Mo": genes_Mo,
    "Nowo": genes_Nowo,
    "Posfai": genes_Posfai,
    "Arg": genes_Arge,
    "Vrij": genes_Vrij,
    "Schu": genes_Schu
}

# Ajouter des valeurs manquantes pour uniformiser la longueur
l = []
for dataset, val in data.items():
    l.append(len(val))

max_length = max(l)

for dataset in data:
    while len(data[dataset]) < max_length:
        data[dataset].append(np.nan)

# Convertir les données en un DataFrame long
df = pd.DataFrame(data)
df_long = df.melt(var_name='Dataset', value_name='genes')

# Supprimer les valeurs manquantes
df_clean = df_long.dropna(subset=['genes'])

# Créer le boxplot et le stripplot
sns.boxplot(data=df_clean, x='Dataset', y='genes', whis=[0, 100], width=.5, palette="Set2")
sns.stripplot(data=df_clean, x='Dataset', y='genes', size=2, color=".3")

# Ajouter des titres et labels si nécessaire
plt.title('Number of genes per cell per dataset')
plt.xlabel('Dataset')
plt.ylabel('Number of genes')

# Afficher le plot
plt.show()
