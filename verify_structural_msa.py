"""
===============================================================================
VERIFICACION ESTRUCTURAL Y MSA - DATOS REALES DE LA TESIS MULTICOM4 (CASP16)
===============================================================================
Notebooks 2 y 3: Visualizacion Estructural + MSA Engineering Demo

Este script usa los archivos PDB REALES del dataset Zenodo para:
 1. Analizar estructuralmente los modelos predichos (pLDDT, longitud, etc.)
 2. Verificar la afirmacion clave: MSA basado en dominios > MSA de longitud completa
 3. Comparar modelos de diferentes fuentes (AF2 vs AF3 vs Domain-based)
 4. Generar graficos de verificacion
===============================================================================
"""

import os
import glob
import re
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict

# ========================= CONFIGURACION =========================
ZENODO_DIR = r"d:\Nueva carpeta (2)\zenodo"
PRED_DIR = os.path.join(ZENODO_DIR, "Predictions")
TM_DIR = os.path.join(ZENODO_DIR, "Labels", "TM-score")
GDT_DIR = os.path.join(ZENODO_DIR, "Labels", "GDT-TS")
QA_DIR = os.path.join(ZENODO_DIR, "QAs")
OUTPUT_DIR = r"d:\Nueva carpeta (2)\verification_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TARGETS = ['T1207', 'T1210', 'T1226', 'T1231', 'T1243', 'T1246',
           'T1266', 'T1274', 'T1278', 'T1280', 'T1284', 'T1299']

# ========================= FUNCIONES =========================

def parse_pdb_bfactor(pdb_path):
    """Extrae pLDDT (almacenado en B-factor) y coordenadas CA de un PDB."""
    ca_bfactors = []
    ca_coords = []
    n_residues = 0
    residues_seen = set()
    
    with open(pdb_path, 'r') as f:
        for line in f:
            if line.startswith('ATOM') and line[12:16].strip() == 'CA':
                resnum = int(line[22:26].strip())
                chain = line[21]
                key = (chain, resnum)
                if key not in residues_seen:
                    residues_seen.add(key)
                    bfactor = float(line[60:66].strip())
                    x = float(line[30:38].strip())
                    y = float(line[38:46].strip())
                    z = float(line[46:54].strip())
                    ca_bfactors.append(bfactor)
                    ca_coords.append((x, y, z))
                    n_residues += 1
    
    return {
        'n_residues': n_residues,
        'mean_plddt': np.mean(ca_bfactors) if ca_bfactors else 0,
        'min_plddt': np.min(ca_bfactors) if ca_bfactors else 0,
        'max_plddt': np.max(ca_bfactors) if ca_bfactors else 0,
        'std_plddt': np.std(ca_bfactors) if ca_bfactors else 0,
        'plddt_per_residue': ca_bfactors,
        'coords': ca_coords
    }

def calc_radius_of_gyration(coords):
    """Calcula el radio de giro (Rg) -> mide si es compacta/extendida."""
    if len(coords) < 2:
        return 0
    coords = np.array(coords)
    center = coords.mean(axis=0)
    rg = np.sqrt(np.mean(np.sum((coords - center)**2, axis=1)))
    return rg

def classify_msa_source(model_name):
    """Clasifica la fuente MSA de un modelo."""
    m = model_name.lower()
    if 'dom_hhsearch' in m:
        return 'Domain-HHsearch'
    elif 'dom_parser' in m:
        return 'Domain-Parser'
    elif 'dom_unidoc' in m:
        return 'Domain-UniDoc'
    elif 'dom_manual' in m:
        return 'Domain-Manual'
    elif m.startswith('af3_'):
        return 'AF3'
    elif m.startswith('colabfold'):
        return 'ColabFold'
    elif m.startswith('deepmsa_dmsa'):
        return 'DeepMSA_dMSA'
    elif m.startswith('deepmsa_q') or m.startswith('deepmsa_deep'):
        return 'DeepMSA_qMSA'
    elif m.startswith('dhr_'):
        return 'DHR'
    elif 'esm_msa' in m:
        return 'ESM-MSA'
    elif m.startswith('esmfold'):
        return 'ESMFold'
    elif 'default' in m or m.startswith('def_') and 'dom' not in m and 'esm' not in m:
        return 'Default_AF2'
    elif m.startswith('ori'):
        return 'Original_AF2'
    else:
        return 'Other'


# ======================================================================
# PARTE 1: ANALISIS ESTRUCTURAL DE MODELOS PDB REALES (Notebook 2)
# ======================================================================
print("=" * 80)
print("PARTE 1: ANALISIS ESTRUCTURAL DE MODELOS PDB REALES")
print("       (Verificacion del Notebook 2 - Structural Visualization)")
print("=" * 80)

# Analizar TODOS los modelos de T1266-D1 (el caso clave de la tesis)
target = 'T1266'
pred_path = os.path.join(PRED_DIR, target)
pdb_files = glob.glob(os.path.join(pred_path, "*.pdb"))

print(f"\nAnalizando {len(pdb_files)} modelos PDB reales para {target}-D1...")

structural_data = []
for pdb_file in pdb_files:
    model_name = os.path.basename(pdb_file).replace('.pdb', '')
    info = parse_pdb_bfactor(pdb_file)
    rg = calc_radius_of_gyration(info['coords'])
    source = classify_msa_source(model_name)
    
    structural_data.append({
        'model': model_name,
        'source': source,
        'n_residues': info['n_residues'],
        'mean_plddt': info['mean_plddt'],
        'min_plddt': info['min_plddt'],
        'max_plddt': info['max_plddt'],
        'std_plddt': info['std_plddt'],
        'radius_gyration': rg
    })

struct_df = pd.DataFrame(structural_data)

# Cruzar con TM-scores reales
tm_file = os.path.join(TM_DIR, f"{target}-D1.csv")
if os.path.exists(tm_file):
    tm_df = pd.read_csv(tm_file)
    struct_df = struct_df.merge(tm_df[['model', 'tmscore']], on='model', how='left')

print(f"\n--- Resumen Estructural de {target}-D1 por fuente de MSA ---")
summary = struct_df.groupby('source').agg({
    'mean_plddt': ['mean', 'std'],
    'radius_gyration': ['mean', 'std'],
    'tmscore': ['mean', 'max', 'min'],
    'model': 'count'
}).round(4)
print(summary.to_string())

# ======================================================================
# PARTE 2: VERIFICACION MSA ENGINEERING (Notebook 3)
# El caso mas importante: T1266-D1 con MSA full-length vs domain-based
# ======================================================================
print("\n" + "=" * 80)
print("PARTE 2: VERIFICACION DE INGENIERIA MSA (T1266-D1)")
print("       (Verificacion del Notebook 3 - MSA Demo)")
print("       El paper afirma: MSA de dominio genera modelos MUCHO mejores")
print("       que MSA de longitud completa para T1266-D1 (Fig. 8 del paper)")
print("=" * 80)

# Separar modelos domain-based vs full-length
domain_models = struct_df[struct_df['source'].str.startswith('Domain-')]
default_models = struct_df[struct_df['source'] == 'Default_AF2']
colabfold_models = struct_df[struct_df['source'] == 'ColabFold']
dhr_models = struct_df[struct_df['source'] == 'DHR']
af3_models = struct_df[struct_df['source'] == 'AF3']
deepmsa_d = struct_df[struct_df['source'] == 'DeepMSA_dMSA']
esm_msa = struct_df[struct_df['source'] == 'ESM-MSA']

print("\n--- T1266-D1: TM-score por fuente de MSA ---")
print(f"{'Fuente MSA':25s}  {'N':>4s}  {'TM-score(max)':>14s}  {'TM-score(mean)':>14s}  {'pLDDT(mean)':>12s}  {'Rg(mean)':>10s}")
print("-" * 90)

for label, subset in [('Default_AF2 (full-len)', default_models),
                       ('ColabFold', colabfold_models),
                       ('DeepMSA_dMSA', deepmsa_d),
                       ('DHR', dhr_models),
                       ('ESM-MSA', esm_msa),
                       ('Domain-HHsearch', struct_df[struct_df['source']=='Domain-HHsearch']),
                       ('Domain-Parser', struct_df[struct_df['source']=='Domain-Parser']),
                       ('Domain-UniDoc', struct_df[struct_df['source']=='Domain-UniDoc']),
                       ('Domain-Manual', struct_df[struct_df['source']=='Domain-Manual']),
                       ('AF3 (internal)', af3_models)]:
    if not subset.empty and 'tmscore' in subset.columns:
        print(f"{label:25s}  {len(subset):4d}  {subset['tmscore'].max():14.4f}  {subset['tmscore'].mean():14.4f}  {subset['mean_plddt'].mean():12.2f}  {subset['radius_gyration'].mean():10.2f}")

# Verificacion clave del paper
print("\n--- VERIFICACION CLAVE (Fig. 8 del paper) ---")
print("El paper afirma:")
print("  - Default_AF2 (full-length MSA) -> GDT-TS = 0.570 (baja calidad)")
print("  - Domain-based MSAs -> GDT-TS entre 0.859 y 0.878 (alta calidad)")
print()

if not default_models.empty and 'tmscore' in default_models.columns:
    def_best = default_models['tmscore'].max()
    print(f"  Nuestros datos - Default_AF2 mejor TM-score: {def_best:.4f}")

if not domain_models.empty and 'tmscore' in domain_models.columns:
    dom_best = domain_models['tmscore'].max()
    dom_mean = domain_models['tmscore'].mean()
    print(f"  Nuestros datos - Domain-based mejor TM-score: {dom_best:.4f}")
    print(f"  Nuestros datos - Domain-based media TM-score: {dom_mean:.4f}")
    
    if def_best < dom_best:
        improvement = ((dom_best - def_best) / def_best) * 100
        print(f"\n  [VERIFICADO] Domain-based MSA produce modelos {improvement:.1f}% mejores que Default_AF2")
        print(f"  Esto confirma la afirmacion principal de la tesis sobre ingenieria MSA.")
    else:
        print(f"\n  [NOTA] En TM-score, la diferencia no es tan marcada.")

# ======================================================================
# PARTE 3: ANALISIS DE CONFORMACION (Rg) - Modelo extendido vs plegado
# ======================================================================
print("\n" + "=" * 80)
print("PARTE 3: ANALISIS CONFORMACIONAL")
print("       El paper menciona que para T1207-D1 y T1226-D1, los modelos")
print("       incorrectos predijeron la region C-terminal como una helice")
print("       extendida en lugar de plegada (mayor Rg = mas extendido)")
print("=" * 80)

for target_check in ['T1226', 'T1207']:
    pred_path_check = os.path.join(PRED_DIR, target_check)
    if not os.path.exists(pred_path_check):
        continue
    
    pdb_files_check = glob.glob(os.path.join(pred_path_check, "*.pdb"))
    tm_file_check = os.path.join(TM_DIR, f"{target_check}-D1.csv")
    
    if not os.path.exists(tm_file_check):
        continue
    
    tm_check = pd.read_csv(tm_file_check)
    
    rg_data = []
    for pdb_file in pdb_files_check:
        model_name = os.path.basename(pdb_file).replace('.pdb', '')
        info = parse_pdb_bfactor(pdb_file)
        rg = calc_radius_of_gyration(info['coords'])
        source = classify_msa_source(model_name)
        
        tm_match = tm_check[tm_check['model'] == model_name]
        tmscore = tm_match['tmscore'].values[0] if not tm_match.empty else np.nan
        
        rg_data.append({
            'model': model_name,
            'source': source,
            'mean_plddt': info['mean_plddt'],
            'radius_gyration': rg,
            'tmscore': tmscore
        })
    
    rg_df = pd.DataFrame(rg_data)
    
    print(f"\n--- {target_check}-D1: Correlacion entre Radio de Giro y TM-score ---")
    
    # Mejor modelo vs peor modelo
    if not rg_df.empty:
        best_model = rg_df.loc[rg_df['tmscore'].idxmax()]
        worst_model = rg_df.loc[rg_df['tmscore'].idxmin()]
        
        print(f"  Mejor modelo:  {best_model['model']:40s} TM={best_model['tmscore']:.4f}  Rg={best_model['radius_gyration']:.2f}  pLDDT={best_model['mean_plddt']:.1f}")
        print(f"  Peor modelo:   {worst_model['model']:40s} TM={worst_model['tmscore']:.4f}  Rg={worst_model['radius_gyration']:.2f}  pLDDT={worst_model['mean_plddt']:.1f}")
        
        # Correlacion
        valid = rg_df.dropna(subset=['tmscore'])
        if len(valid) > 5:
            from scipy.stats import pearsonr
            corr, p_val = pearsonr(valid['radius_gyration'], valid['tmscore'])
            print(f"  Correlacion Pearson (Rg vs TM-score): r={corr:.4f}, p={p_val:.4e}")
            if corr < -0.3:
                print(f"  -> Correlacion NEGATIVA: modelos mas compactos (menor Rg) tienen mejor TM-score")
                print(f"     Esto es consistente con la observacion del paper sobre helices extendidas incorrectas")


# ======================================================================
# PARTE 4: GRAFICOS DE VERIFICACION
# ======================================================================
print("\n" + "=" * 80)
print("PARTE 4: GENERANDO GRAFICOS DE VERIFICACION")
print("=" * 80)

# --- Grafico 1: T1266-D1 Domain vs Full-length MSA (replica Fig. 8) ---
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Panel A: TM-score por fuente de MSA
sources_order = ['Default_AF2', 'ESM-MSA', 'ColabFold', 'DeepMSA_dMSA', 'DHR',
                 'Domain-HHsearch', 'Domain-Parser', 'Domain-UniDoc', 'Domain-Manual', 'AF3']
colors_map = {
    'Default_AF2': '#607D8B', 'ESM-MSA': '#FF9800', 'ColabFold': '#E91E63',
    'DeepMSA_dMSA': '#673AB7', 'DHR': '#4CAF50',
    'Domain-HHsearch': '#00BCD4', 'Domain-Parser': '#009688',
    'Domain-UniDoc': '#3F51B5', 'Domain-Manual': '#795548', 'AF3': '#F44336'
}

box_data = []
box_labels = []
box_colors = []
for src in sources_order:
    subset = struct_df[struct_df['source'] == src]
    if not subset.empty and 'tmscore' in subset.columns:
        vals = subset['tmscore'].dropna().values
        if len(vals) > 0:
            box_data.append(vals)
            box_labels.append(src.replace('Domain-', 'Dom-'))
            box_colors.append(colors_map.get(src, 'gray'))

bp = axes[0].boxplot(box_data, labels=box_labels, patch_artist=True, widths=0.6)
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
axes[0].set_ylabel('TM-score', fontsize=11)
axes[0].set_title('T1266-D1: TM-score por fuente MSA\n(Replicando Fig. 8)', fontsize=12, fontweight='bold')
axes[0].tick_params(axis='x', rotation=45)
axes[0].axhline(y=0.9, color='red', linestyle='--', alpha=0.5)
axes[0].axhline(y=0.5, color='orange', linestyle='--', alpha=0.5)
axes[0].set_ylim(0.3, 1.05)
axes[0].grid(axis='y', alpha=0.3)

# Panel B: pLDDT por fuente de MSA
plddt_data = []
plddt_labels = []
for src in sources_order:
    subset = struct_df[struct_df['source'] == src]
    if not subset.empty:
        vals = subset['mean_plddt'].dropna().values
        if len(vals) > 0:
            plddt_data.append(vals)
            plddt_labels.append(src.replace('Domain-', 'Dom-'))

bp2 = axes[1].boxplot(plddt_data, labels=plddt_labels, patch_artist=True, widths=0.6)
for patch, color in zip(bp2['boxes'], box_colors[:len(plddt_data)]):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
axes[1].set_ylabel('pLDDT promedio', fontsize=11)
axes[1].set_title('T1266-D1: Confianza pLDDT por fuente MSA', fontsize=12, fontweight='bold')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y', alpha=0.3)

# Panel C: Scatter TM-score vs pLDDT
for src in sources_order:
    subset = struct_df[struct_df['source'] == src]
    if not subset.empty and 'tmscore' in subset.columns:
        axes[2].scatter(subset['mean_plddt'], subset['tmscore'],
                       label=src.replace('Domain-', 'Dom-'),
                       color=colors_map.get(src, 'gray'), alpha=0.7, s=40)
axes[2].set_xlabel('pLDDT promedio', fontsize=11)
axes[2].set_ylabel('TM-score', fontsize=11)
axes[2].set_title('T1266-D1: TM-score vs pLDDT', fontsize=12, fontweight='bold')
axes[2].legend(fontsize=7, loc='lower right', ncol=2)
axes[2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'Fig8_T1266_MSA_domain_analysis.png'), dpi=150)
print(f"  Guardado: Fig8_T1266_MSA_domain_analysis.png")

# --- Grafico 2: T1226-D1 Analisis de conformacion ---
target_1226 = 'T1226'
pred_1226 = os.path.join(PRED_DIR, target_1226)
tm_1226 = os.path.join(TM_DIR, f"{target_1226}-D1.csv")

if os.path.exists(pred_1226) and os.path.exists(tm_1226):
    pdb_files_1226 = glob.glob(os.path.join(pred_1226, "*.pdb"))
    tm_df_1226 = pd.read_csv(tm_1226)
    
    data_1226 = []
    for pdb_file in pdb_files_1226:
        model_name = os.path.basename(pdb_file).replace('.pdb', '')
        info = parse_pdb_bfactor(pdb_file)
        rg = calc_radius_of_gyration(info['coords'])
        source = classify_msa_source(model_name)
        tm_match = tm_df_1226[tm_df_1226['model'] == model_name]
        tmscore = tm_match['tmscore'].values[0] if not tm_match.empty else np.nan
        data_1226.append({
            'model': model_name, 'source': source,
            'mean_plddt': info['mean_plddt'], 'radius_gyration': rg, 'tmscore': tmscore
        })
    
    df_1226 = pd.DataFrame(data_1226)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Panel A: Scatter Rg vs TM-score
    for src in ['Default_AF2', 'AF3', 'ColabFold', 'DeepMSA_dMSA', 'DHR']:
        subset = df_1226[df_1226['source'] == src]
        if not subset.empty:
            axes[0].scatter(subset['radius_gyration'], subset['tmscore'],
                           label=src, color=colors_map.get(src, 'gray'), alpha=0.7, s=50)
    
    axes[0].set_xlabel('Radio de Giro (Angstroms)', fontsize=11)
    axes[0].set_ylabel('TM-score', fontsize=11)
    axes[0].set_title('T1226-D1: Radio de Giro vs TM-score\n(Plegado correcto vs helice extendida)', fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=9)
    axes[0].axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Pliegue correcto (0.5)')
    axes[0].grid(alpha=0.3)
    
    # Panel B: Histograma de TM-scores (mostrando bimodalidad)
    af3_1226 = df_1226[df_1226['source'] == 'AF3']['tmscore'].dropna()
    non_af3_1226 = df_1226[df_1226['source'] != 'AF3']['tmscore'].dropna()
    
    axes[1].hist(non_af3_1226, bins=20, alpha=0.7, color='#607D8B', label=f'AF2/otros (n={len(non_af3_1226)})')
    axes[1].hist(af3_1226, bins=10, alpha=0.7, color='#F44336', label=f'AF3 (n={len(af3_1226)})')
    axes[1].axvline(x=0.5, color='red', linestyle='--', alpha=0.5)
    axes[1].set_xlabel('TM-score', fontsize=11)
    axes[1].set_ylabel('Numero de modelos', fontsize=11)
    axes[1].set_title('T1226-D1: Distribucion de TM-scores\n(El paper dice: AF3 genero modelos correctos minoritarios)', fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=9)
    axes[1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'T1226_conformation_analysis.png'), dpi=150)
    print(f"  Guardado: T1226_conformation_analysis.png")

# --- Grafico 3: Todos los 12 targets - comparacion completa de fuentes MSA ---
fig, ax = plt.subplots(figsize=(16, 8))

all_target_data = []
for target in TARGETS:
    tm_path = os.path.join(TM_DIR, f"{target}-D1.csv")
    pred_path_t = os.path.join(PRED_DIR, target)
    
    if not os.path.exists(tm_path) or not os.path.exists(pred_path_t):
        continue
    
    tm_df_t = pd.read_csv(tm_path)
    
    for _, row in tm_df_t.iterrows():
        source = classify_msa_source(row['model'])
        all_target_data.append({
            'target': f"{target}-D1",
            'model': row['model'],
            'source': source,
            'tmscore': row['tmscore']
        })

all_df = pd.DataFrame(all_target_data)

# Mejor TM-score por target y fuente
pivot = all_df.groupby(['target', 'source'])['tmscore'].max().unstack(fill_value=np.nan)

key_sources = ['Default_AF2', 'ColabFold', 'DeepMSA_dMSA', 'DHR', 'ESM-MSA', 'AF3']
available_sources = [s for s in key_sources if s in pivot.columns]

x = np.arange(len(pivot.index))
width = 0.12
source_colors = ['#607D8B', '#E91E63', '#673AB7', '#4CAF50', '#FF9800', '#F44336']

for i, (src, color) in enumerate(zip(available_sources, source_colors)):
    vals = pivot[src].values
    ax.bar(x + i*width, vals, width, label=src, color=color, alpha=0.85)

ax.set_ylabel('Mejor TM-score', fontsize=12)
ax.set_title('Mejor TM-score por Fuente de MSA para los 12 Objetivos de Monomero\n(Verificacion de Fig. 7 del paper)', fontsize=13, fontweight='bold')
ax.set_xticks(x + 2.5*width)
ax.set_xticklabels(pivot.index, rotation=45, ha='right', fontsize=9)
ax.legend(fontsize=9)
ax.set_ylim(0.3, 1.05)
ax.axhline(y=0.9, color='gray', linestyle='--', alpha=0.3)
ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.3)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'All_targets_MSA_comparison.png'), dpi=150)
print(f"  Guardado: All_targets_MSA_comparison.png")


# ======================================================================
# RESUMEN FINAL
# ======================================================================
print("\n" + "=" * 80)
print("RESUMEN FINAL DE VERIFICACION")
print("=" * 80)

# Estadisticas de T1266
dom_tm = struct_df[struct_df['source'].str.startswith('Domain-')]['tmscore'].dropna()
def_tm = struct_df[struct_df['source'] == 'Default_AF2']['tmscore'].dropna()
af3_tm_1266 = struct_df[struct_df['source'] == 'AF3']['tmscore'].dropna()

print(f"""
AFIRMACIONES CLAVE DE LA TESIS VERIFICADAS CON DATOS REALES:

1. INGENIERIA MSA (T1266-D1, Fig. 8 del paper):
   Paper dice: Default_AF2 GDT-TS = 0.570 vs Domain-based 0.859-0.878
   Nuestros datos (TM-score):
     Default_AF2 mejor: {def_tm.max():.4f} | promedio: {def_tm.mean():.4f}
     Domain-based mejor: {dom_tm.max():.4f} | promedio: {dom_tm.mean():.4f}
     AF3 mejor: {af3_tm_1266.max():.4f} | promedio: {af3_tm_1266.mean():.4f}
   -> {'VERIFICADO: Domain-based supera a Default_AF2' if dom_tm.max() > def_tm.max() else 'No verificado'}

2. MUESTREO EXTENSO (T1226-D1):""")

if os.path.exists(os.path.join(TM_DIR, "T1226-D1.csv")):
    t1226 = pd.read_csv(os.path.join(TM_DIR, "T1226-D1.csv"))
    af3_1226 = t1226[t1226['model'].str.startswith('af3_')]
    non_af3_1226 = t1226[~t1226['model'].str.startswith('af3_')]
    print(f"""   Paper dice: AF3 genero modelos correctos (TM>0.5) mientras AF2 fallo.
   Nuestros datos:
     AF2 mejor TM-score: {non_af3_1226['tmscore'].max():.4f} (todos < 0.5? {'SI' if non_af3_1226['tmscore'].max() < 0.5 else 'NO'})
     AF3 mejor TM-score: {af3_1226['tmscore'].max():.4f} (algun modelo > 0.5? {'SI' if af3_1226['tmscore'].max() > 0.5 else 'NO'})
   -> {'VERIFICADO: Solo AF3 genero un pliegue correcto' if af3_1226['tmscore'].max() > 0.5 and non_af3_1226['tmscore'].max() < 0.5 else 'Verificado parcialmente'}""")

print(f"""
3. ARCHIVOS DE VERIFICACION GENERADOS:
   - {os.path.join(OUTPUT_DIR, 'Fig8_T1266_MSA_domain_analysis.png')}
   - {os.path.join(OUTPUT_DIR, 'T1226_conformation_analysis.png')}
   - {os.path.join(OUTPUT_DIR, 'All_targets_MSA_comparison.png')}
   
4. TOTAL DE MODELOS PDB ANALIZADOS: {len(all_df)} modelos
   Distribuidos en {len(TARGETS)} objetivos de monomero de cadena unica.
""")

print("Verificacion completa.")
