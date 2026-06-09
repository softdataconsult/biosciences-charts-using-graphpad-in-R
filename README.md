# Biochemical Assay Plots

R and Python scripts for generating **GraphPad Prism-style black-and-white patterned bar charts** for 9 biochemical assays across 5 treatment groups in an AlCl₃-induced neurotoxicity study in *Drosophila melanogaster*.

---

## Study Context

This project visualises the effect of *Annona senegalensis* stem bark extract (AESS) on oxidative stress and neurotoxicity biomarkers in *Drosophila melanogaster* exposed to aluminium chloride (AlCl₃). Five treatment groups were used:

| Group | Treatment |
|-------|-----------|
| Group 1 | Control (untreated) |
| Group 2 | AlCl₃ (0.1 mg/g diet) |
| Group 3 | AlCl₃ + AESS (0.25 mg/g diet) |
| Group 4 | AlCl₃ + AESS (0.5 mg/g diet) |
| Group 5 | AESS only (0.4 mg/g diet) |

---

## Assays Covered

| Code | Parameter | Unit |
|------|-----------|------|
| GLU | Glucose | µmol/mg protein |
| TP | Total Protein | mg/mL |
| NO | Nitric Oxide | nmol/mg protein |
| GSH | Glutathione | µmol/mg protein |
| MAO | Monoamine Oxidase | µmol/mg protein |
| TT | Total Thiol | mmol/mg protein |
| CAT | Catalase | µmol/mg protein |
| GST | Glutathione-S-Transferase | µmol/mg protein |
| ACHE | Acetylcholinesterase | µmol/mL/mg protein |

---

## Output Figures

- **9 individual bar charts** — one per assay (`Fig_GLU.png`, `Fig_TP.png`, etc.)
- **1 combined 3×3 panel** — all assays in one figure (`Fig_ALL_panel.png`)

### Chart Style
- Black-and-white patterned fills (unique hatch per group) — publication-ready, no colour
- Error bars: Mean ± SD (n = 5)
- Significance letters (a, ab, b) above bars in italic
- Slanted x-axis labels (45°)
- Boxed plot frame — matches GraphPad Prism style

---

## Files

```
├── plots_R_script.R        # R script (ggplot2 + ggpattern + patchwork)
├── plots_python_script.py  # Python script (matplotlib + numpy)
├── plots/
│   ├── Fig_GLU.png
│   ├── Fig_TP.png
│   ├── Fig_NO.png
│   ├── Fig_GSH.png
│   ├── Fig_MAO.png
│   ├── Fig_TT.png
│   ├── Fig_CAT.png
│   ├── Fig_GST.png
│   ├── Fig_ACHE.png
│   └── Fig_ALL_panel.png
└── README.md
```

---

## Usage

### R
```r
# Install required packages
install.packages(c("ggplot2", "ggpattern", "patchwork"))

# Run the script
source("thankgod_plots_R_script.R")
```
Plots will be saved to a `plots/` folder in your working directory.

### Python
```bash
# Install required packages
pip install matplotlib numpy

# Run the script
python plots_python_script.py
```
Plots will be saved to a `plots/` folder in your working directory.

---

## Requirements

| Tool | Packages |
|------|----------|
| R (≥ 4.0) | `ggplot2`, `ggpattern`, `patchwork` |
| Python (≥ 3.8) | `matplotlib`, `numpy` |

---

## Citation

Data are presented as Mean ± SD (n = 5). Different superscript letters above bars indicate statistically significant differences between groups at *p* < 0.05.

---

## Author

**Unanimous** — undergraduate research project
Supervised analysis and figure production: [softdataconsult](https://github.com/softdataconsult)