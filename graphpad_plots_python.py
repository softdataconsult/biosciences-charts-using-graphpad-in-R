"""
GraphPad-style plotting utilities in Python
- reads summarized `example_data.csv` or per-subject `example_subjects.csv`
- creates bar charts (mean ± SD) with hatch patterns
- creates box/violin plots from per-subject data

Run:
    python thankgod_graphpad_plots_python.py

Requires: matplotlib, numpy, pandas, seaborn
"""
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


OUTDIR = Path("plots_python_polished")
OUTDIR.mkdir(exist_ok=True)

# Default hatch patterns for groups
HATCHES = ["x", "+", "|", "/", "."]


def load_summary(path="example_data.csv"):
    return pd.read_csv(path)


def load_subjects(path="example_subjects.csv"):
    return pd.read_csv(path)


def make_bar_chart_from_summary(df, assay, outdir=OUTDIR):
    d = df[df.assay == assay].copy()
    groups = d.group.tolist()
    means = d.mean.values
    sds = d.sd.values

    x = np.arange(len(groups))
    fig, ax = plt.subplots(figsize=(5, 4.2))
    bars = ax.bar(x, means, width=0.6, color='white', edgecolor='black', linewidth=0.9, zorder=2)
    for bar, hatch in zip(bars, HATCHES):
        bar.set_hatch(hatch)

    ax.errorbar(x, means, yerr=sds, fmt='none', color='black', capsize=4, capthick=0.8, elinewidth=0.8, zorder=3)
    for i, (m, s, ltr) in enumerate(zip(means, sds, d.letter.tolist())):
        top = m + s + max(means + sds) * 0.06
        ax.text(i, top, ltr, ha='center', va='bottom', fontsize=9, style='italic')

    ax.set_ylim(0, max(means + sds) * 1.25)
    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=9, rotation=45, ha='right')
    ax.set_ylabel(d.iloc[0].ylabel if 'ylabel' in d.columns else '')
    ax.set_xlabel('Treatment')
    ax.set_title(d.iloc[0].title if 'title' in d.columns else assay, fontsize=9, style='italic')
    for spine in ax.spines.values():
        spine.set_linewidth(0.8)
    ax.tick_params(axis='both', direction='out', labelsize=9)
    ax.set_facecolor('white')
    ax.grid(False)

    fname = outdir / f"Fig_{assay}.png"
    plt.tight_layout()
    plt.savefig(fname, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {fname}")


def make_combined_panels_from_summary(df, outdir=OUTDIR):
    assays = df.assay.unique().tolist()
    n = len(assays)
    cols = 3
    rows = int(np.ceil(n / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4.2 * rows))
    axes = axes.reshape(rows, cols)
    for i, assay in enumerate(assays):
        r, c = divmod(i, cols)
        ax = axes[r, c]
        d = df[df.assay == assay]
        make_bar_chart_from_summary(d, assay, outdir=outdir)
        # Instead of replotting into the big figure, just insert saved image into grid
        img = plt.imread(outdir / f"Fig_{assay}.png")
        ax.imshow(img)
        ax.axis('off')

    # Turn off any unused axes
    for j in range(i + 1, rows * cols):
        r, c = divmod(j, cols)
        axes[r, c].axis('off')

    combined_path = outdir / "Fig_ALL_panel.png"
    plt.tight_layout()
    plt.savefig(combined_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {combined_path}")


def make_box_violin_from_subjects(df_subjects, assay, outdir=OUTDIR):
    d = df_subjects[df_subjects.assay == assay].copy()
    plt.figure(figsize=(5, 4.2))
    ax = plt.gca()
    sns.boxplot(x='group', y='value', data=d, color='white', showcaps=True, boxprops={'edgecolor':'black'})
    sns.stripplot(x='group', y='value', data=d, color='black', size=4, jitter=0.12)
    ax.set_xlabel('Treatment')
    ax.set_ylabel(d.iloc[0].ylabel if 'ylabel' in d.columns else '')
    ax.set_title(d.iloc[0].title if 'title' in d.columns else assay, fontsize=9, style='italic')
    plt.xticks(rotation=45, ha='right')
    fname = outdir / f"Box_{assay}.png"
    plt.tight_layout()
    plt.savefig(fname, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {fname}")


def main():
    # Summarized plots (bar + panel)
    summary_path = Path('example_data.csv')
    if summary_path.exists():
        df_sum = load_summary(summary_path)
        assays = df_sum.assay.unique().tolist()
        for a in assays:
            make_bar_chart_from_summary(df_sum, a)
        make_combined_panels_from_summary(df_sum)
    else:
        print('No example_data.csv found; skipping summary bar charts.')

    # Per-subject plots (box/violin)
    subj_path = Path('example_subjects.csv')
    if subj_path.exists():
        df_sub = load_subjects(subj_path)
        assays = df_sub.assay.unique().tolist()
        for a in assays:
            make_box_violin_from_subjects(df_sub, a)
    else:
        print('No example_subjects.csv found; skipping box/violin plots.')


if __name__ == '__main__':
    main()
