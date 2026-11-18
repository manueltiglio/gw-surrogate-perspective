# Surrogate Modeling and Reduced-Order Methods in Gravitational-Wave Physics and Numerical Relativity

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-Preprint-B31B1B.svg)](https://arxiv.org)
[![Journal](https://img.shields.io/badge/Universe-MDPI-blue.svg)](https://www.mdpi.com/journal/universe)

Official source code, LaTeX manuscripts, and numerical benchmark assets for the Perspective article: 
*"Surrogate Modeling and Reduced-Order Methods in Gravitational-Wave Physics and Numerical Relativity: From Spectral Representations to Adaptive Compression"*.

---

## 🧭 Abstract & Overview

As current ground-based gravitational-wave detectors operate alongside upcoming third-generation facilities (Einstein Telescope, Cosmic Explorer) and space-borne observatories (LISA), direct numerical relativity simulations face severe computational bottlenecks. 

This repository contains the complete material accompanying our Perspective manuscript, which critically examines:
* The mathematical foundations of projection-based reduced-order modeling (ROM) and Empirical Interpolation Methods (EIM).
* Fundamental approximation barriers governed by slow Kolmogorov $n$-width decay due to phase accumulation and localized transient features.
* The role of adaptive $hp$-greedy domain decomposition and multi-scale spectral compression.
* A forward-looking comparison between certified physics-based surrogates and modern scientific machine learning (SciML) architectures.

---

## 📂 Repository Structure

```text
├── perspective.tex         # Main LaTeX source file (standard article class)
├── hp_rom_benchmark.pdf    # High-resolution vector graphic for benchmark analysis
├── generate_plots.py       # Python / Matplotlib script used to generate vector assets
└── README.md               # Project documentation and compilation guide
```

---

## ⚙️ Local Compilation

To compile the LaTeX manuscript locally into a PDF, ensure you have a standard TeX distribution (such as TeX Live or MacTeX) installed. Run the following commands in your terminal:

```bash
# Clone the repository
git clone https://github.com/TU_USUARIO/gw-surrogate-perspective.git
cd gw-surrogate-perspective

# Compile the document (run twice to resolve cross-references)
pdflatex perspective.tex
pdflatex perspective.tex
```

---

## 📊 Reproducing Figures

The vector graphic (`hp_rom_benchmark.pdf`) used in Section 4 can be regenerated or modified using the provided Python script. 

1. Install required dependencies:
   ```bash
   pip install matplotlib numpy
   ```
2. Execute the script:
   ```bash
   python generate_plots.py
   ```

---

## 📜 Citation

If you use or build upon the insights, code, or assets provided in this repository, please cite our manuscript:

```bibtex
@article{tiglio2026perspective,
  author  = {Tiglio, Manuel},
  title   = {Surrogate Modeling and Reduced-Order Methods in Gravitational-Wave Physics and Numerical Relativity},
  journal = {Universe},
  year    = {2026}
}
```

---

## 📄 License

MIT License

Copyright (c) 2026 Manuel Tiglio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.