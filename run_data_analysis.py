import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import warnings
warnings.filterwarnings('ignore')

print("=== Generando datos simulados basados en el paper ===")
# Mismas estadísticas descritas en el paper: 
# MULTICOM Mean TM-score top-1 = 0.902, best-of-top-5 = 0.922
# AF3-server Mean TM-score top-1 = 0.891, best-of-top-5 = 0.904
# N = 84 dominios

np.random.seed(42) # Para reproducibilidad

data = {
    'Domain': [f'Domain_{i}' for i in range(1, 85)],
    'MULTICOM_Top1': np.random.normal(0.902, 0.05, 84).clip(0, 1),
    'MULTICOM_Best5': np.random.normal(0.922, 0.04, 84).clip(0, 1),
    'AF3Server_Top1': np.random.normal(0.891, 0.06, 84).clip(0, 1),
    'AF3Server_Best5': np.random.normal(0.904, 0.05, 84).clip(0, 1)
}
df = pd.DataFrame(data)

# Para objetivos específicos mencionados en la tesis (sobrescribimos)
df.loc[0, ['Domain', 'MULTICOM_Top1', 'AF3Server_Top1']] = ['T1257-D1', 0.95, 0.80] 
df.loc[1, ['Domain', 'MULTICOM_Top1', 'AF3Server_Top1']] = ['T1267s1-D1', 0.98, 0.85]
df.loc[2, ['Domain', 'MULTICOM_Top1', 'AF3Server_Top1']] = ['T1218-D2', 0.70, 0.85] # AF3 fue mejor aquí

print(df.head())

# Pruebas estadísticas (Test de rangos de Wilcoxon)
print("\n=== Test de Wilcoxon para TM-Score (Top-1) ===")
stat_top1, p_top1 = stats.wilcoxon(df['MULTICOM_Top1'], df['AF3Server_Top1'], alternative='greater')
print(f"p-value = {p_top1:.4f} (El paper reportó p=0.08, no significativo)")

print("\n=== Test de Wilcoxon para TM-Score (Mejor de Top-5) ===")
stat_best5, p_best5 = stats.wilcoxon(df['MULTICOM_Best5'], df['AF3Server_Best5'], alternative='greater')
print(f"p-value = {p_best5:.6f} (El paper reportó p=1.491e-05, estadísticamente significativo)")

# Graficando Head-to-Head (Replicando Fig. 4)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(df['AF3Server_Top1'], df['MULTICOM_Top1'], alpha=0.7, color='blue')
plt.plot([0, 1], [0, 1], 'k--', lw=1) # Línea diagonal
plt.xlabel('AF3-server TM-score (Top-1)')
plt.ylabel('MULTICOM TM-score (Top-1)')
plt.title('Comparación de Modelos Top-1')
plt.xlim(0.6, 1)
plt.ylim(0.6, 1)

plt.subplot(1, 2, 2)
plt.scatter(df['AF3Server_Best5'], df['MULTICOM_Best5'], alpha=0.7, color='red')
plt.plot([0, 1], [0, 1], 'k--', lw=1) # Línea diagonal
plt.xlabel('AF3-server TM-score (Mejor de Top-5)')
plt.ylabel('MULTICOM TM-score (Mejor de Top-5)')
plt.title('Comparación de Modelos Mejores de Top-5')
plt.xlim(0.6, 1)
plt.ylim(0.6, 1)

plt.tight_layout()
plt.savefig('d:/Nueva carpeta (2)/Data_Analysis_Plot.png')
print("\n=== Gráfico guardado como 'Data_Analysis_Plot.png' ===")
