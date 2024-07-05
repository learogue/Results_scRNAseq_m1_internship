"""import anndata as ad
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


adata_Deng = ad.read_h5ad('Processing/standardv2/Objects/object_1_Deng_filtered_1.h5ad')
reads_Deng = adata_Deng.obs['total_counts'].to_list()

adata_Chen = ad.read_h5ad('Processing/standardv2/Objects/object_2_Chen_filtered_1.h5ad')
reads_Chen = adata_Chen.obs['total_counts'].to_list()

adata_Mo = ad.read_h5ad('Processing/standardv2/Objects/object_3_Mohammed_filtered_1.h5ad')
reads_Mo = adata_Mo.obs['total_counts'].to_list()

adata_Nowo = ad.read_h5ad('Processing/standardv2/Objects/object_4_Nowo_filtered_1.h5ad')
reads_Nowoa = adata_Nowo.obs['total_counts'].to_list()

adata_Nowob = ad.read_h5ad('Processing/standardv2/Objects/object_4bis_Nowo_filtered_1.h5ad')
reads_Nowob = adata_Nowob.obs['total_counts'].to_list()

reads_Nowo = reads_Nowoa + reads_Nowob

adata_Posfai = ad.read_h5ad('Processing/standardv2/Objects/object_5_Posfai_filtered_1.h5ad')
reads_Posfai = adata_Posfai.obs['total_counts'].to_list()

adata_Arge = ad.read_h5ad('Processing/standardv2/Objects/object_6_Arg_filtered_1.h5ad')
reads_Arge = adata_Arge.obs['total_counts'].to_list()

adata_Vrij = ad.read_h5ad('Processing/Vrij/Objects/object_7_Vrij_filtered_1.h5ad')
reads_Vrij = adata_Vrij.obs['total_counts'].to_list()

adata_Schu = ad.read_h5ad('Processing/Schu_ssVrij/Objects/object_8_Schu_filtered_1.h5ad')
reads_Schu = adata_Schu.obs['total_counts'].to_list()

data = {
    "Deng": reads_Deng,
    "Chen": reads_Chen,
    "Mo": reads_Mo,
    "Nowo": reads_Nowo,
    "Posfai": reads_Posfai,
    "Arg": reads_Arge,
    "Vrij": reads_Vrij,
    "Schu": reads_Schu
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
df_long = df.melt(var_name='Dataset', value_name='reads')
df_clean = df_long.dropna()

sns.boxplot(df_clean, x='Dataset', y='reads', whis=[0, 100], width=.5, palette="Set2")
sns.stripplot(x='Dataset', y='reads', data=df_clean, size=2, color=".3")

# Ajouter des titres et labels si nécessaire
plt.title('Number of reads per cell per dataset')
plt.xlabel('Dataset')
plt.ylabel('Number of reads')

# Afficher le plot
plt.show()

"""


import anndata as ad
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Lecture des données
adata_Deng = ad.read_h5ad('Processing/standardv2/Objects/object_1_Deng_filtered_1.h5ad')
reads_Deng = adata_Deng.obs['total_counts'].to_list()

adata_Chen = ad.read_h5ad('Processing/standardv2/Objects/object_2_Chen_filtered_1.h5ad')
reads_Chen = adata_Chen.obs['total_counts'].to_list()

adata_Mo = ad.read_h5ad('Processing/standardv2/Objects/object_3_Mohammed_filtered_1.h5ad')
reads_Mo = adata_Mo.obs['total_counts'].to_list()

adata_Nowo = ad.read_h5ad('Processing/standardv2/Objects/object_4_Nowo_filtered_1.h5ad')
reads_Nowoa = adata_Nowo.obs['total_counts'].to_list()

adata_Nowob = ad.read_h5ad('Processing/standardv2/Objects/object_4bis_Nowo_filtered_1.h5ad')
reads_Nowob = adata_Nowob.obs['total_counts'].to_list()

reads_Nowo = reads_Nowoa + reads_Nowob

adata_Posfai = ad.read_h5ad('Processing/standardv2/Objects/object_5_Posfai_filtered_1.h5ad')
reads_Posfai = adata_Posfai.obs['total_counts'].to_list()

adata_Arge = ad.read_h5ad('Processing/standardv2/Objects/object_6_Arg_filtered_1.h5ad')
reads_Arge = adata_Arge.obs['total_counts'].to_list()

adata_Vrij = ad.read_h5ad('Processing/Vrij/Objects/object_7_Vrij_filtered_1.h5ad')
reads_Vrij = adata_Vrij.obs['total_counts'].to_list()

adata_Schu = ad.read_h5ad('Processing/Schu_ssVrij/Objects/object_8_Schu_filtered_1.h5ad')
reads_Schu = adata_Schu.obs['total_counts'].to_list()

data = {
    "Deng": reads_Deng,
    "Chen": reads_Chen,
    "Mo": reads_Mo,
    "Nowo": reads_Nowo,
    "Posfai": reads_Posfai,
    "Arg": reads_Arge,
    "Vrij": reads_Vrij,
    "Schu": reads_Schu
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
df_long = df.melt(var_name='Dataset', value_name='reads')

# Transformation logarithmique
df_long['log_reads'] = np.log10(df_long['reads'])

# Supprimer les valeurs manquantes
df_clean = df_long.dropna(subset=['log_reads'])

# Créer le boxplot et le stripplot
sns.boxplot(data=df_clean, x='Dataset', y='log_reads', whis=[0, 100], width=.5, palette="Set2")
sns.stripplot(data=df_clean, x='Dataset', y='log_reads', size=2, color=".3")

# Ajouter des titres et labels si nécessaire
plt.title('Log10 of Number of reads per cell per dataset')
plt.xlabel('Dataset')
plt.ylabel('Log10(Number of reads)')

# Afficher le plot
plt.show()
