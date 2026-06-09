# ============================================================
# GraphPad-style B&W patterned bar charts — Python/matplotlib
# Thankgod data — 9 biochemical assays, 5 groups
# Run: python thankgod_plots_python_script.py
# Requires: matplotlib, numpy  (pip install matplotlib numpy)
# ============================================================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("plots_python", exist_ok=True)

groups = ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5"]

data = {
    "GLU":  {"mean": [0.481,0.404,0.397,0.474,0.412], "sd":[0.144,0.104,0.075,0.055,0.118],
             "letter":["a","a","a","a","a"], "ylabel":"GLU activity (µmol/mg protein)"},
    "TP":   {"mean": [0.526,0.464,0.526,0.437,0.406], "sd":[0.071,0.038,0.078,0.059,0.023],
             "letter":["a","ab","a","ab","b"],  "ylabel":"TP level (mg/mL)"},
    "NO":   {"mean": [2.681,2.609,2.745,2.645,2.736], "sd":[0.279,0.259,0.267,0.318,0.267],
             "letter":["a","a","a","a","a"],   "ylabel":"NO level (nmol/mg protein)"},
    "GSH":  {"mean": [0.069,0.086,0.067,0.084,0.083], "sd":[0.009,0.060,0.020,0.010,0.021],
             "letter":["a","a","a","a","a"],   "ylabel":"GSH level (µmol/mg protein)"},
    "MAO":  {"mean": [0.096,0.113,0.081,0.145,0.080], "sd":[0.052,0.055,0.033,0.041,0.020],
             "letter":["a","a","a","a","a"],   "ylabel":"MAO activity (µmol/mg protein)"},
    "TT":   {"mean": [0.125,0.144,0.135,0.152,0.183], "sd":[0.021,0.055,0.048,0.039,0.057],
             "letter":["a","a","a","a","a"],   "ylabel":"Total thiol level (mmol/mg protein)"},
    "CAT":  {"mean": [0.1442,0.1312,0.1288,0.1339,0.1182], "sd":[0.0202,0.0061,0.0102,0.0260,0.0254],
             "letter":["a","ab","ab","ab","b"],"ylabel":"CAT activity (µmol/mg protein)"},
    "GST":  {"mean": [0.852,0.633,0.739,0.741,0.843], "sd":[0.211,0.066,0.177,0.229,0.158],
             "letter":["a","a","a","a","a"],   "ylabel":"GST activity (µmol/mg protein)"},
    "ACHE": {"mean": [0.1218,0.1111,0.0869,0.1045,0.0939], "sd":[0.0175,0.0133,0.0188,0.0607,0.0165],
             "letter":["a","a","a","a","a"],   "ylabel":"AChE activity (µmol/mL/mg protein)"},
}

titles = {
    "GLU":  "Effect of AESS on glucose level in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "TP":   "Effect of AESS on total protein level in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "NO":   "Effect of AESS on nitric oxide level in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "GSH":  "Effect of AESS on glutathione level in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "MAO":  "Effect of AESS on monoamine oxidase activity in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "TT":   "Effect of AESS on total thiol level in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "CAT":  "Effect of AESS on catalase activity in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "GST":  "Effects of AESS on glutathione-S-transferase activity in AlCl₃-induced\nneurotoxicity in D. melanogaster",
    "ACHE": "Effect of AESS on acetylcholinesterase activity in AlCl₃-induced\nneurotoxicity in D. melanogaster",
}

# Hatch patterns: Group1=diagonal cross, Group2=checkerboard, Group3=vertical, Group4=diagonal, Group5=dense grid
hatches = ['x', '+', '|', '/', '++']

def make_bar_chart(assay, ax, show_xlabel=True):
    d = data[assay]
    means   = np.array(d["mean"])
    sds     = np.array(d["sd"])
    letters = d["letter"]
    ylabel  = d["ylabel"]

    x = np.arange(len(groups))
    bars = ax.bar(x, means, width=0.6, color='white', edgecolor='black',
                  linewidth=0.8, zorder=2)
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)

    ax.errorbar(x, means, yerr=sds, fmt='none', color='black',
                capsize=4, capthick=0.8, elinewidth=0.8, zorder=3)

    for i, (m, s, ltr) in enumerate(zip(means, sds, letters)):
        top = m + s + max(means) * 0.06
        ax.text(i, top, ltr, ha='center', va='bottom', fontsize=9, style='italic')

    ax.set_ylim(0, max(means + sds) * 1.25)
    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=9, rotation=45, ha='right')   # <-- slanted labels
    ax.set_ylabel(ylabel, fontsize=9)
    if show_xlabel:
        ax.set_xlabel("Treatment", fontsize=9)
    ax.set_title(titles[assay], fontsize=8, style='italic', pad=6)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.8)
    ax.tick_params(axis='both', direction='out', labelsize=9)
    ax.set_facecolor('white')
    ax.grid(False)

assay_list = list(data.keys())

# Individual plots
for assay in assay_list:
    fig, ax = plt.subplots(figsize=(5, 4.2))
    fig.patch.set_facecolor('white')
    make_bar_chart(assay, ax)
    plt.tight_layout()
    plt.savefig(f"plots_python/Fig_{assay}.png", dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: plots_python/Fig_{assay}.png")

# 3x3 combined panel
fig, axes = plt.subplots(3, 3, figsize=(15, 13))
fig.patch.set_facecolor('white')
for i, assay in enumerate(assay_list):
    row, col = divmod(i, 3)
    make_bar_chart(assay, axes[row][col], show_xlabel=(row == 2))
    if row < 2:
        axes[row][col].set_xlabel("")

caption = ("Data are presented as Mean ± SD (n = 5). Different superscript letters indicate significant differences at p < 0.05.\n"
           "Group 1 = control; Group 2 = AlCl₃ (0.1 mg/g diet); Group 3 = AlCl₃ + AESS (0.25 mg/g diet);\n"
           "Group 4 = AlCl₃ + AESS (0.5 mg/g diet); Group 5 = AESS (0.4 mg/g diet) only.")
fig.text(0.5, 0.01, caption, ha='center', fontsize=7.5, style='italic')
plt.tight_layout(rect=[0, 0.06, 1, 1])
plt.savefig("plots_python/Fig_ALL_panel.png", dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: plots_python/Fig_ALL_panel.png")
