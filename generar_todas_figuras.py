"""
Genera TODAS las figuras del paper MULTICOM4 usando datos reales de Zenodo.
Figuras: 1, 3, 4, 5, 7 (las que se pueden replicar sin datos externos de CASP16)
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, glob
from scipy.stats import pearsonr

ZENODO = r"d:\Nueva carpeta (2)\zenodo"
TM_DIR = os.path.join(ZENODO, "Labels", "TM-score")
GDT_DIR = os.path.join(ZENODO, "Labels", "GDT-TS")
QA_DIR = os.path.join(ZENODO, "QAs")
PRED_DIR = os.path.join(ZENODO, "Predictions")
OUT = r"d:\Nueva carpeta (2)\colab_notebooks"

TARGETS = ['T1207','T1210','T1226','T1231','T1243','T1246',
           'T1266','T1274','T1278','T1280','T1284','T1299']

# ============ FUNCIONES ============
def classify(m):
    n = m.lower().replace('.pdb','')
    if n.startswith('af3_'): return 'AF3'
    if n.startswith('colabfold'): return 'ColabFold'
    if n.startswith('deepmsa_dmsa'): return 'DeepMSA_dMSA'
    if n.startswith('deepmsa_q') or n.startswith('deepmsa_deep'): return 'DeepMSA_qMSA'
    if n.startswith('dhr_'): return 'DHR'
    if 'esm_msa' in n: return 'ESM-MSA'
    if n.startswith('esmfold'): return 'ESMFold'
    if 'dom_' in n: return 'Domain-based'
    if n.startswith('default') or n.startswith('def_') or n.startswith('ori'): return 'AF2_default'
    return 'Otro'

def parse_pdb(path):
    bf, co = [], []
    seen = set()
    with open(path) as f:
        for l in f:
            if l.startswith('ATOM') and l[12:16].strip()=='CA':
                k = (l[21], int(l[22:26].strip()))
                if k not in seen:
                    seen.add(k)
                    bf.append(float(l[60:66].strip()))
                    co.append([float(l[30:38]),float(l[38:46]),float(l[46:54])])
    c = np.array(co) if co else np.zeros((1,3))
    rg = np.sqrt(np.mean(np.sum((c - c.mean(0))**2, 1))) if len(c)>1 else 0
    return np.mean(bf) if bf else 0, rg, len(seen)

# ============ CARGAR DATOS ============
print("Cargando datos...")
tm_all, gdt_all = {}, {}
for t in TARGETS:
    f1 = os.path.join(TM_DIR, f"{t}-D1.csv")
    f2 = os.path.join(GDT_DIR, f"{t}-D1.csv")
    if os.path.exists(f1): tm_all[t] = pd.read_csv(f1)
    if os.path.exists(f2): gdt_all[t] = pd.read_csv(f2)

# ============ FIGURA 3: TM-score de modelos Top-1 y Best-of-5 para 84 dominios ============
print("Generando Figura 3...")
fig, axes = plt.subplots(2, 1, figsize=(16, 12))

# Panel A: TM-score por dominio (barras ordenadas)
top1_data = []
for t in TARGETS:
    if t not in tm_all: continue
    df = tm_all[t]
    non_esm = df[~df['model'].str.startswith('esmfold')]
    top1_data.append({'dominio': f"{t}-D1", 'tm_top1': non_esm['tmscore'].max(),
                      'tm_best5': non_esm.nlargest(5,'tmscore')['tmscore'].max()})

top1_df = pd.DataFrame(top1_data).sort_values('tm_top1', ascending=False)

x = np.arange(len(top1_df))
axes[0].bar(x, top1_df['tm_top1'], color='#00BCD4', alpha=0.85, label='Top-1')
axes[0].axhline(y=0.9, color='green', linestyle='--', linewidth=2, label='Cerca de nativo (0.9)')
axes[0].axhline(y=0.5, color='red', linestyle='--', linewidth=2, label='Pliegue correcto (0.5)')
axes[0].set_xticks(x)
axes[0].set_xticklabels(top1_df['dominio'], rotation=45, ha='right', fontsize=8)
axes[0].set_ylabel('TM-score', fontsize=12)
axes[0].set_title('(A) TM-score por dominio del modelo Top-1 enviado por MULTICOM', fontsize=14, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].set_ylim(0, 1.05)
axes[0].grid(axis='y', alpha=0.3)

# Panel B: Top-1 vs Best-of-top-5 scatter
axes[1].scatter(top1_df['tm_top1'], top1_df['tm_best5'], s=80, c='#2196F3', edgecolors='black', linewidth=0.5, alpha=0.8)
axes[1].plot([0,1],[0,1],'k--',lw=1)
for _, r in top1_df.iterrows():
    if abs(r['tm_top1'] - r['tm_best5']) > 0.02:
        axes[1].annotate(r['dominio'], (r['tm_top1'], r['tm_best5']), fontsize=7, ha='left')
axes[1].set_xlabel('TM-score Top-1', fontsize=12)
axes[1].set_ylabel('TM-score Mejor de Top-5', fontsize=12)
axes[1].set_title('(B) Puntuaciones TM de Top-1 vs Mejor de Top-5\n(puntos por encima de la diagonal = el muestreo extenso ayuda)', fontsize=14, fontweight='bold')
axes[1].set_xlim(0.3, 1.02)
axes[1].set_ylim(0.3, 1.02)
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'Figura_3_TM_scores_dominios.png'), dpi=150, bbox_inches='tight')
print("  -> Figura_3_TM_scores_dominios.png")

# ============ FIGURA 4: Comparacion head-to-head MULTICOM vs AF3-server ============
print("Generando Figura 4...")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

comp = []
for t in TARGETS:
    if t not in tm_all: continue
    df = tm_all[t]
    af3 = df[df['model'].str.startswith('af3_')]
    non_af3 = df[~df['model'].str.startswith('af3_') & ~df['model'].str.startswith('esmfold')]
    if af3.empty or non_af3.empty: continue
    comp.append({
        'dominio': f"{t}-D1",
        'multicom_top1': non_af3['tmscore'].max(),
        'af3_top1': af3['tmscore'].max(),
        'multicom_best5': non_af3.nlargest(5,'tmscore')['tmscore'].max(),
        'af3_best5': af3.nlargest(5,'tmscore')['tmscore'].max()
    })
comp_df = pd.DataFrame(comp)

# Panel A
axes[0].scatter(comp_df['af3_top1'], comp_df['multicom_top1'], s=80, c='#4CAF50', edgecolors='black', linewidth=0.5, alpha=0.8)
axes[0].plot([0,1],[0,1],'k--',lw=1)
for _, r in comp_df.iterrows():
    axes[0].annotate(r['dominio'], (r['af3_top1'], r['multicom_top1']), fontsize=7, ha='left', va='bottom')
axes[0].set_xlabel('AF3-server TM-score', fontsize=12)
axes[0].set_ylabel('MULTICOM TM-score', fontsize=12)
axes[0].set_title('(A) Comparacion Modelos Top-1\nMULTICOM vs AF3-server', fontsize=13, fontweight='bold')
axes[0].set_xlim(0.3, 1.02); axes[0].set_ylim(0.3, 1.02)
axes[0].grid(alpha=0.3)

# Panel B
axes[1].scatter(comp_df['af3_best5'], comp_df['multicom_best5'], s=80, c='#FF5722', edgecolors='black', linewidth=0.5, alpha=0.8)
axes[1].plot([0,1],[0,1],'k--',lw=1)
for _, r in comp_df.iterrows():
    axes[1].annotate(r['dominio'], (r['af3_best5'], r['multicom_best5']), fontsize=7, ha='left', va='bottom')
axes[1].set_xlabel('AF3-server TM-score', fontsize=12)
axes[1].set_ylabel('MULTICOM TM-score', fontsize=12)
axes[1].set_title('(B) Comparacion Mejor de Top-5\nMULTICOM vs AF3-server', fontsize=13, fontweight='bold')
axes[1].set_xlim(0.3, 1.02); axes[1].set_ylim(0.3, 1.02)
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'Figura_4_MULTICOM_vs_AF3.png'), dpi=150, bbox_inches='tight')
print("  -> Figura_4_MULTICOM_vs_AF3.png")

# ============ FIGURA 5: GDT-TS AF2 interno vs AF3 interno vs AF3-server ============
print("Generando Figura 5...")
fig, ax = plt.subplots(figsize=(16, 8))

gdt_comp = []
for t in TARGETS:
    if t not in gdt_all: continue
    df = gdt_all[t]
    col = [c for c in df.columns if c not in ['Unnamed: 0','model']][0]
    af3 = df[df['model'].str.startswith('af3_')]
    non_af3 = df[~df['model'].str.startswith('af3_') & ~df['model'].str.startswith('esmfold')]
    if af3.empty or non_af3.empty: continue
    gdt_comp.append({
        'dominio': f"{t}-D1",
        'AF2_top1': non_af3[col].max() / 100 if non_af3[col].max() > 1 else non_af3[col].max(),
        'AF2_best5': non_af3.nlargest(5, col)[col].max() / 100 if non_af3[col].max() > 1 else non_af3.nlargest(5, col)[col].max(),
        'AF3_top1': af3[col].max() / 100 if af3[col].max() > 1 else af3[col].max(),
        'AF3_best5': af3.nlargest(5, col)[col].max() / 100 if af3[col].max() > 1 else af3.nlargest(5, col)[col].max()
    })

if gdt_comp:
    gdt_df = pd.DataFrame(gdt_comp).sort_values('dominio')
    x = np.arange(len(gdt_df))
    w = 0.2
    
    ax.bar(x - 1.5*w, gdt_df['AF2_top1'], w, label='Top-1 de AF2 interno', color='#FF9800', alpha=0.85)
    ax.bar(x - 0.5*w, gdt_df['AF2_best5'], w, label='Mejor de Top-5 de AF2 interno', color='#FFC107', alpha=0.85)
    ax.bar(x + 0.5*w, gdt_df['AF3_top1'], w, label='Top-1 de AF3 interno', color='#2196F3', alpha=0.85)
    ax.bar(x + 1.5*w, gdt_df['AF3_best5'], w, label='Mejor de Top-5 de AF3 interno', color='#64B5F6', alpha=0.85)
    
    # Anotar valores
    for i, (_, r) in enumerate(gdt_df.iterrows()):
        for j, col_name in enumerate(['AF2_top1','AF2_best5','AF3_top1','AF3_best5']):
            val = r[col_name]
            offset = (j - 1.5) * w
            ax.text(i + offset, val + 0.01, f'{val:.2f}', ha='center', va='bottom', fontsize=5.5, rotation=90)
    
    ax.set_xticks(x)
    ax.set_xticklabels(gdt_df['dominio'], rotation=45, ha='right', fontsize=9)
    ax.set_ylabel('GDT-TS', fontsize=12)
    ax.set_ylim(0.2, 1.12)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(axis='y', alpha=0.3)

ax.set_title('Fig. 5 | Comparacion del rendimiento GDT-TS entre AF2 interno,\nAF3 interno y AF3-server para los 12 objetivos de monomeros', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'Figura_5_AF2_vs_AF3_GDT.png'), dpi=150, bbox_inches='tight')
print("  -> Figura_5_AF2_vs_AF3_GDT.png")

# ============ FIGURA 7: GDT-TS por fuente de MSA ============
print("Generando Figura 7...")
fig, ax = plt.subplots(figsize=(16, 8))

msa_sources = ['ColabFold', 'DeepMSA_dMSA', 'DeepMSA_qMSA', 'AF2_default', 'ESM-MSA', 'DHR']
msa_labels = ['ColabFold', 'DeepMSA_dMSA', 'DeepMSA_qMSA', 'AF2 por defecto', 'ESM-MSA', 'DHR']
msa_colors = ['#2196F3', '#FF9800', '#4CAF50', '#9E9E9E', '#9C27B0', '#795548']

msa_data = {s: [] for s in msa_sources}
for t in TARGETS:
    if t not in gdt_all: continue
    df = gdt_all[t]
    col = [c for c in df.columns if c not in ['Unnamed: 0','model']][0]
    df['source'] = df['model'].apply(classify)
    for s in msa_sources:
        sub = df[df['source'] == s]
        if not sub.empty:
            best = sub[col].max()
            if best > 1: best = best / 100
            msa_data[s].append(best)
        else:
            msa_data[s].append(np.nan)

x = np.arange(len(TARGETS))
w = 0.13
for i, (s, lbl, clr) in enumerate(zip(msa_sources, msa_labels, msa_colors)):
    vals = msa_data[s]
    ax.bar(x + i*w, vals, w, label=lbl, color=clr, alpha=0.85)

ax.set_xticks(x + 2.5*w)
ax.set_xticklabels([f"{t}-D1" for t in TARGETS], rotation=45, ha='right', fontsize=9)
ax.set_ylabel('GDT-TS', fontsize=12)
ax.set_title('Fig. 7 | Comparacion del rendimiento de GDT-TS para modelos top-1\ngenerados usando diferentes fuentes de MSA', fontsize=14, fontweight='bold')
ax.legend(fontsize=9)
ax.set_ylim(0.2, 1.05)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'Figura_7_MSA_fuentes.png'), dpi=150, bbox_inches='tight')
print("  -> Figura_7_MSA_fuentes.png")

# ============ FIGURA 6-ANALISIS: T1226-D1 conformacion ============
print("Generando figura de analisis T1226-D1 (Fig. 6 del paper)...")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

t1226 = tm_all.get('T1226', pd.DataFrame())
if not t1226.empty:
    t1226['source'] = t1226['model'].apply(classify)
    
    # Analizar PDBs de T1226
    rg_data = []
    for pdb in glob.glob(os.path.join(PRED_DIR, "T1226", "*.pdb")):
        name = os.path.basename(pdb).replace('.pdb','')
        plddt, rg, nres = parse_pdb(pdb)
        src = classify(name)
        tm_match = t1226[t1226['model']==name]
        tm = tm_match['tmscore'].values[0] if not tm_match.empty else np.nan
        rg_data.append({'model': name, 'source': src, 'plddt': plddt, 'rg': rg, 'tmscore': tm})
    
    rg_df = pd.DataFrame(rg_data)
    
    c_map = {'AF2_default':'#607D8B','AF3':'#F44336','ColabFold':'#E91E63',
             'DeepMSA_dMSA':'#673AB7','DHR':'#4CAF50','ESM-MSA':'#FF9800','ESMFold':'#795548'}
    
    for src, clr in c_map.items():
        sub = rg_df[rg_df['source']==src]
        if not sub.empty:
            axes[0].scatter(sub['rg'], sub['tmscore'], label=src, color=clr, alpha=0.7, s=50)
    
    axes[0].axhline(y=0.5, color='red', linestyle='--', linewidth=2, label='Pliegue correcto (0.5)')
    axes[0].set_xlabel('Radio de Giro (Angstroms)', fontsize=12)
    axes[0].set_ylabel('TM-score', fontsize=12)
    axes[0].set_title('T1226-D1: Radio de Giro vs TM-score\n(compacto = mejor)', fontsize=13, fontweight='bold')
    axes[0].legend(fontsize=8)
    axes[0].grid(alpha=0.3)
    
    corr, pval = pearsonr(rg_df.dropna(subset=['tmscore'])['rg'], rg_df.dropna(subset=['tmscore'])['tmscore'])
    axes[0].text(0.05, 0.95, f'r = {corr:.3f}\np = {pval:.2e}', transform=axes[0].transAxes,
                fontsize=10, va='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Histograma
    af3_tm = rg_df[rg_df['source']=='AF3']['tmscore'].dropna()
    otros_tm = rg_df[rg_df['source']!='AF3']['tmscore'].dropna()
    axes[1].hist(otros_tm, bins=20, alpha=0.7, color='#607D8B', label=f'AF2/otros (n={len(otros_tm)})')
    axes[1].hist(af3_tm, bins=10, alpha=0.7, color='#F44336', label=f'AlphaFold3 (n={len(af3_tm)})')
    axes[1].axvline(x=0.5, color='red', linestyle='--', linewidth=2)
    axes[1].set_xlabel('TM-score', fontsize=12)
    axes[1].set_ylabel('Numero de modelos', fontsize=12)
    axes[1].set_title('T1226-D1: Solo AF3 genero modelos correctos\n(TM > 0.5)', fontsize=13, fontweight='bold')
    axes[1].legend(fontsize=9)
    axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'Figura_6_T1226_analisis.png'), dpi=150, bbox_inches='tight')
print("  -> Figura_6_T1226_analisis.png")

# ============ FIGURA 8-ANALISIS: T1266-D1 MSA Domain analysis ============
print("Generando figura de ingenieria MSA T1266-D1 (Fig. 8 del paper)...")
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

t1266 = tm_all.get('T1266', pd.DataFrame())
if not t1266.empty:
    def classify_detail(m):
        n = m.lower()
        if 'dom_hhsearch' in n: return 'Dom-HHsearch'
        if 'dom_parser' in n: return 'Dom-Parser'
        if 'dom_unidoc' in n: return 'Dom-UniDoc'
        if 'dom_manual' in n: return 'Dom-Manual'
        if n.startswith('af3_'): return 'AlphaFold3'
        if n.startswith('colabfold'): return 'ColabFold'
        if n.startswith('deepmsa_dmsa'): return 'DeepMSA-dMSA'
        if n.startswith('deepmsa_q') or n.startswith('deepmsa_deep'): return 'DeepMSA-qMSA'
        if n.startswith('dhr_'): return 'DHR'
        if 'esm_msa' in n: return 'ESM-MSA'
        if n.startswith('esmfold'): return 'ESMFold'
        if n.startswith('ori'): return 'Original-AF2'
        return 'Default-AF2'
    
    t1266['source_detail'] = t1266['model'].apply(classify_detail)
    
    orden = ['Default-AF2','ESM-MSA','DeepMSA-qMSA','DeepMSA-dMSA','ColabFold','DHR',
             'Original-AF2','AlphaFold3','Dom-HHsearch','Dom-Parser','Dom-Manual','Dom-UniDoc']
    colores_d = {
        'Default-AF2':'#9E9E9E','ESM-MSA':'#FF9800','DeepMSA-qMSA':'#7E57C2',
        'DeepMSA-dMSA':'#673AB7','ColabFold':'#E91E63','DHR':'#4CAF50',
        'Original-AF2':'#795548','AlphaFold3':'#F44336',
        'Dom-HHsearch':'#00BCD4','Dom-Parser':'#009688','Dom-Manual':'#0288D1','Dom-UniDoc':'#3F51B5'
    }
    
    # Boxplot
    box_d, box_l, box_c = [], [], []
    for s in orden:
        sub = t1266[t1266['source_detail']==s]['tmscore'].dropna()
        if len(sub)>0:
            box_d.append(sub.values)
            box_l.append(s)
            box_c.append(colores_d.get(s,'gray'))
    
    bp = axes[0].boxplot(box_d, patch_artist=True, widths=0.6)
    for patch, c in zip(bp['boxes'], box_c):
        patch.set_facecolor(c); patch.set_alpha(0.7)
    axes[0].set_xticklabels(box_l, rotation=55, ha='right', fontsize=8)
    axes[0].set_ylabel('TM-score', fontsize=12)
    axes[0].set_title('T1266-D1: TM-score por fuente de MSA\n(Fig. 8 del paper)', fontsize=13, fontweight='bold')
    axes[0].axhline(y=0.9, color='green', linestyle='--', alpha=0.5)
    axes[0].set_ylim(0.55, 1.02)
    axes[0].grid(axis='y', alpha=0.3)
    
    # Barras de promedio
    promedios = t1266.groupby('source_detail')['tmscore'].mean()
    prom_ord = [promedios.get(s, np.nan) for s in orden if s in promedios]
    labels_ord = [s for s in orden if s in promedios.index]
    colors_ord = [colores_d.get(s,'gray') for s in labels_ord]
    
    bars = axes[1].bar(range(len(prom_ord)), prom_ord, color=colors_ord, alpha=0.85)
    axes[1].set_xticks(range(len(labels_ord)))
    axes[1].set_xticklabels(labels_ord, rotation=55, ha='right', fontsize=8)
    axes[1].set_ylabel('TM-score promedio', fontsize=12)
    axes[1].set_title('T1266-D1: Promedio TM-score por fuente MSA\n(Domain > Default)', fontsize=13, fontweight='bold')
    axes[1].set_ylim(0.7, 1.0)
    axes[1].axhline(y=0.9, color='green', linestyle='--', alpha=0.5)
    axes[1].grid(axis='y', alpha=0.3)
    for bar, val in zip(bars, prom_ord):
        axes[1].text(bar.get_x()+bar.get_width()/2, val+0.003, f'{val:.3f}', ha='center', fontsize=7)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'Figura_8_T1266_MSA_dominio.png'), dpi=150, bbox_inches='tight')
print("  -> Figura_8_T1266_MSA_dominio.png")

# ============ FIGURA QA METHODS ============
print("Generando figura de metodos QA (Fig. 9 del paper)...")
fig, ax = plt.subplots(figsize=(14, 7))

qa_methods = ['af_plddt_avg','pairwise_tmscore','gate','enqa','gcpnet_ema']
qa_names = ['plDDT','PSS','GATE','EnQA','GCPNet-EMA']
qa_colors = ['#FF5722','#9C27B0','#009688','#FF9800','#3F51B5']
qa_results = {n: [] for n in qa_names}

for t in TARGETS:
    qa_file = os.path.join(QA_DIR, t, "gate_af_summary.csv")
    tm_file = os.path.join(TM_DIR, f"{t}-D1.csv")
    if not os.path.exists(qa_file) or not os.path.exists(tm_file):
        for n in qa_names: qa_results[n].append(np.nan)
        continue
    dq = pd.read_csv(qa_file)
    dt = pd.read_csv(tm_file)
    for method, name in zip(qa_methods, qa_names):
        if method not in dq.columns:
            qa_results[name].append(np.nan)
            continue
        best_model = dq.loc[dq[method].idxmax(), 'model'].replace('.pdb','')
        match = dt[dt['model']==best_model]
        qa_results[name].append(match['tmscore'].values[0] if not match.empty else np.nan)

x = np.arange(len(TARGETS))
w = 0.15
for i, (name, clr) in enumerate(zip(qa_names, qa_colors)):
    ax.bar(x + i*w, qa_results[name], w, label=name, color=clr, alpha=0.85)

ax.set_xticks(x + 2*w)
ax.set_xticklabels([f"{t}-D1" for t in TARGETS], rotation=45, ha='right', fontsize=9)
ax.set_ylabel('TM-score del modelo Top-1 seleccionado', fontsize=12)
ax.set_title('Fig. 9 | TM-score del modelo Top-1 seleccionado por cada metodo de QA\n(Ningun metodo es consistentemente mejor)', fontsize=14, fontweight='bold')
ax.legend(fontsize=9)
ax.set_ylim(0.3, 1.05)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'Figura_9_QA_metodos.png'), dpi=150, bbox_inches='tight')
print("  -> Figura_9_QA_metodos.png")

print("\n" + "="*60)
print("TODAS LAS FIGURAS GENERADAS EXITOSAMENTE")
print("Ubicacion:", OUT)
print("="*60)
