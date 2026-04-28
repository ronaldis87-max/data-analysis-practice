import pandas as pd

# Charger le fichier
df = pd.read_csv('vend-total_revenue-for-product-by-month (2025-05-01 to 2026-04-24).csv')

print("Shape original:", df.shape)

# Étape 1 : Garder seulement les colonnes utiles
colonnes_utiles = ['SKU Name', 'Tag', 'Revenue', 'Cost of Goods Sold',
                   'Gross Profit', 'Margin (%)',
                   'May 2025', 'Jun 2025', 'Jul 2025', 'Aug 2025',
                   'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025',
                   'Jan 2026', 'Feb 2026', 'Mar 2026', 'Apr 2026']

df = df[colonnes_utiles]

# Étape 2 : Supprimer les lignes où Revenue est 0 ou négatif
df = df[df['Revenue'] > 0]

# Étape 3 : Renommer 'Tag' en 'Category' pour plus de clarté
df.rename(columns={'Tag': 'Category'}, inplace=True)
# Keep only the first tag for multi-category products
df['Category'] = df['Category'].str.split(',').str[0].str.strip()

print("Shape after cleaning:", df.shape)
print("\nAperçu:")
print(df.head(3))
# Quick business overview
print("\n--- REVENUE BY CATEGORY ---")
print(df.groupby('Category')['Revenue'].sum().sort_values(ascending=False))