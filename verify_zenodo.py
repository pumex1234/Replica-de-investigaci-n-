import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os
import glob
import warnings
warnings.filterwarnings('ignore')

# Ruta de la carpeta donde están los verdaderos datos de la tesis
data_dir = r"d:\Nueva carpeta (2)\zenodo\Labels\TM-score"

# Cargar todos los archivos CSV y consolidarlos
all_files = glob.glob(os.path.join(data_dir, "*.csv"))

results = []

for file in all_files:
    domain_name = os.path.basename(file).replace('.csv', '')
    df = pd.read_csv(file)
    
    # Múltiples predicciones de MULTICOM (en general todas menos AF3 están en esta categoría para la tesis, o los "colabfold / deepmsa / default" etc)
    # y predicciones explícitas de AF3 (que comienzan con af3_)
    
    # Filtrar modelos AlphaFold3
    af3_models = df[df['model'].str.startswith('af3_')]
    
    # Filtrar los demás que se consideraron (Alphafold2, Colabfold, MSA variados, etc.)
    non_af3_models = df[~df['model'].str.startswith('af3_')]
    
    
    if not af3_models.empty and not non_af3_models.empty:
        # Calcular los máximos (Top 1 teórico y mejor de Top 5)
        # Nota: aquí simplemente buscamos el mejor posible de la lista para ilustrar
        multicom_top1 = non_af3_models['tmscore'].max()
        af3_top1 = af3_models['tmscore'].max()
        
        results.append({
            'Domain': domain_name,
            'MULTICOM_Max_TMScore': multicom_top1,
            'AF3_Max_TMScore': af3_top1
        })

df_results = pd.DataFrame(results)
print("=== Resumen de datos reales de la Tesis extraídos de Zenodo ===")
print(df_results)
print("\nMedia de TM-score Máximo No-AF3 (MULTICOM approach):", df_results['MULTICOM_Max_TMScore'].mean())
print("Media de TM-score Máximo AF3:", df_results['AF3_Max_TMScore'].mean())

print("\n=== Test de Wilcoxon ===")
stat, p = stats.wilcoxon(df_results['MULTICOM_Max_TMScore'], df_results['AF3_Max_TMScore'], alternative='greater')
print(f"p-value (MULTICOM > AF3) = {p:.4f}")
