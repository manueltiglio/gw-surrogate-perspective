{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8FE-KvpBbcnK"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Configuración de estilo tipográfico para la figura (coherente con LaTeX)\n",
        "plt.rcParams.update({\n",
        "    \"text.usetex\": False,  # True si tenés LaTeX instalado localmente para texto\n",
        "    \"font.family\": \"serif\",\n",
        "    \"font.size\": 10,\n",
        "    \"axes.labelsize\": 11,\n",
        "    \"legend.fontsize\": 9,\n",
        "    \"xtick.labelsize\": 9,\n",
        "    \"ytick.labelsize\": 9\n",
        "})\n",
        "\n",
        "# 1. Simulación de datos para el Benchmark\n",
        "# Eje X: Dimensión de la base reducida (n)\n",
        "n_global = np.array([4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])\n",
        "# Error worst-case global (muestra el plateau algebraico por el transitorio)\n",
        "err_global = 0.8 * (n_global / 4.0)**(-1.2) + 0.05 * np.exp(-n_global / 10.0)\n",
        "err_global[err_global < 4.2e-6] = 4.20e-6 * (48 / n_global[err_global < 4.2e-6])**0.8 # suavizado de meseta\n",
        "\n",
        "# Eje X local por subdominio para hp-greedy (p_max = 8)\n",
        "n_local = np.array([2, 4, 6, 8])\n",
        "# Error worst-case hp-greedy (exponencial por celda)\n",
        "err_hp = 1.2 * np.exp(-1.4 * n_local)\n",
        "\n",
        "# CAMBIO AQUÍ: (2, 1) para apilar verticalmente y ajustar proporciones\n",
        "fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.5, 7.5), constrained_layout=True)\n",
        "\n",
        "# Panel Superior: Convergencia Global vs hp-Greedy\n",
        "ax1.semilogy(n_global, err_global, 'o-', color='#1f77b4', lw=1.8, ms=5, label='Global Greedy (RB/EIM)')\n",
        "ax1.semilogy(n_local, err_hp, 's--', color='#d62728', lw=1.8, ms=6, label='Adaptive $hp$-Greedy ($K=8$ cells)')\n",
        "ax1.axhline(1e-6, color='gray', linestyle=':', lw=1.2, label='Indistinguishability Target ($\\mathcal{M} = 10^{-6}$)')\n",
        "\n",
        "ax1.set_xlabel('Active Basis Dimension ($n$ or $n_k$ per cell)')\n",
        "ax1.set_ylabel('Worst-Case Projection / EIM Error')\n",
        "ax1.set_title('(a) Worst-Case Convergence Rate')\n",
        "ax1.grid(True, which=\"both\", ls=\"--\", alpha=0.5)\n",
        "ax1.set_xlim(0, 50)\n",
        "ax1.set_ylim(1e-8, 1.0)\n",
        "ax1.legend(loc='lower left')\n",
        "\n",
        "# Panel Inferior: Crecimiento de la constante de Lebesgue EIM (Lambda_n)\n",
        "lambda_global = 4.12 * (1.0 + 0.07 * n_global**1.1)\n",
        "lambda_hp = 3.25 * np.ones_like(n_local) + 0.1 * n_local\n",
        "\n",
        "ax2.plot(n_global, lambda_global, 'o-', color='#1f77b4', lw=1.8, ms=5, label='Global EIM ($\\Lambda_n$ growth)')\n",
        "ax2.plot(n_local, lambda_hp, 's--', color='#2ca02c', lw=1.8, ms=6, label='Local $hp$-Greedy ($\\Lambda_n$ bounded)')\n",
        "\n",
        "ax2.set_xlabel('Basis Dimension ($n$)')\n",
        "ax2.set_ylabel('EIM Lebesgue Constant ($\\Lambda_n$)')\n",
        "ax2.set_title('(b) Interpolation Stability ($\\Lambda_n$)')\n",
        "ax2.grid(True, which=\"both\", ls=\"--\", alpha=0.5)\n",
        "ax2.set_xlim(0, 50)\n",
        "ax2.set_ylim(1, 110)\n",
        "ax2.legend(loc='upper left')\n",
        "\n",
        "# Guardar figura en PDF vectorial de alta calidad\n",
        "plt.savefig('hp_rom_benchmark.pdf', format='pdf', dpi=300, bbox_inches='tight')\n",
        "plt.show()\n",
        "print(\"¡Gráfico vertical 'hp_rom_benchmark.pdf' generado con éxito!\")\n"
      ]
    }
  ]
}