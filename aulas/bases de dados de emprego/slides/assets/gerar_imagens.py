"""
Gera as imagens estáticas utilizadas nos slides:
  - arquitetura_6_camadas.png
  - chart_barras_empilhadas.png
  - chart_slope.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# ── Paleta ─────────────────────────────────────────────────────────────────────
COLORS = {
    "azul":    "#1565C0",
    "verde":   "#2E7D32",
    "roxo":    "#6A1B9A",
    "laranja": "#E65100",
    "indigo":  "#584cd2",
    "teal":    "#006064",
}

TECH_COLORS = ["#1565C0", "#1976D2", "#388E3C", "#F57C00", "#E64A19", "#7B1FA2", "#455A64"]


# ══════════════════════════════════════════════════════════════════════════════
# 1. ARQUITETURA EM 6 CAMADAS
# ══════════════════════════════════════════════════════════════════════════════
def make_arquitetura():
    layers = [
        {
            "color": COLORS["azul"],
            "num": "1",
            "name": "DADOS BRUTOS",
            "sub": "extraídos da fonte original",
            "what": ["Extração dos dados da fonte original",
                     "Armazenamento bruto e íntegro",
                     "Preserva o histórico e a rastreabilidade"],
            "why": ["Garantia de integridade e auditabilidade",
                    "Possibilidade de reprocessamento",
                    "Base confiável e imutável"],
        },
        {
            "color": COLORS["verde"],
            "num": "2",
            "name": "CARREGAMENTO E LIMPEZA",
            "sub": "em sistema gerenciador de banco de dados",
            "what": ["Carregamento dos dados brutos",
                     "Validação, padronização e deduplicação",
                     "Criação de modelo relacional"],
            "why": ["Dados confiáveis e consistentes",
                    "Governança e segurança",
                    "Única fonte da verdade"],
        },
        {
            "color": COLORS["roxo"],
            "num": "3",
            "name": "CONSTRUÇÃO DE VISÕES",
            "sub": "agregações otimizadas para consulta",
            "what": ["Criação de visões materializadas",
                     "Agregações por tema, tempo, geografia, setor",
                     "Estruturas otimizadas para performance"],
            "why": ["Consultas mais rápidas e eficientes",
                    "Simplifica o consumo dos dados",
                    "Padronização de métricas e definições"],
        },
        {
            "color": COLORS["laranja"],
            "num": "4",
            "name": "API DE ACESSO",
            "sub": "serviços padronizados para consumo",
            "what": ["Exposição das visões via API REST",
                     "Controle de acesso e autenticação",
                     "Paginação, filtros e parâmetros"],
            "why": ["Acesso seguro e controlado",
                    "Integração fácil com sistemas",
                    "Reduz carga no banco de dados"],
        },
        {
            "color": COLORS["indigo"],
            "num": "5",
            "name": "BIBLIOTECA / CATÁLOGO",
            "sub": "centralização de informações de acesso",
            "what": ["Catálogo de APIs, tabelas e indicadores",
                     "Documentação e dicionário de dados",
                     "Gestão de permissões e uso"],
            "why": ["Facilidade de descoberta e uso",
                    "Autonomia e agilidade para o usuário",
                    "Transparência e governança"],
        },
        {
            "color": COLORS["teal"],
            "num": "6",
            "name": "CONSUMO E GERAÇÃO DE VALOR",
            "sub": "insights, análises e decisões",
            "what": ["Consumo via API, ferramentas ou BI",
                     "Análises, relatórios e visualizações",
                     "Geração de conhecimento e políticas"],
            "why": ["Decisões mais rápidas e assertivas",
                    "Dados acessíveis e confiáveis",
                    "Cultura data-driven"],
        },
    ]

    fig_h = 14
    fig = plt.figure(figsize=(20, fig_h), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 20)
    ax.set_ylim(0, fig_h)
    ax.axis("off")

    # Título
    ax.text(10, 13.45, "ARQUITETURA DE DADOS EM 6 CAMADAS",
            ha="center", va="center", fontsize=22, fontweight="bold", color="#212121")
    ax.text(10, 13.0, "Cada camada utiliza o que foi construído na anterior e agrega mais valor para a próxima.",
            ha="center", va="center", fontsize=11, color="#555555")

    # Cabeçalhos das colunas
    for x, lbl in [(4.5, "CAMADA E FLUXO"), (11.5, "O QUE A CAMADA FAZ"), (17.2, "VANTAGENS PRINCIPAIS")]:
        ax.text(x, 12.55, lbl, ha="center", va="center", fontsize=10,
                fontweight="bold", color="#333333",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#f0f0f0", edgecolor="none"))

    row_h = 1.85
    y_start = 12.1

    for i, L in enumerate(layers):
        y_top = y_start - i * row_h
        y_mid = y_top - row_h / 2

        # ── left band ──────────────────────────────────────────────────────────
        band = FancyBboxPatch((0.2, y_top - row_h + 0.05), 8.6, row_h - 0.1,
                              boxstyle="round,pad=0.05",
                              facecolor=L["color"] + "18", edgecolor=L["color"] + "40", linewidth=0.8)
        ax.add_patch(band)

        # número + círculo colorido
        circ = plt.Circle((1.15, y_mid), 0.42, color=L["color"], zorder=3)
        ax.add_patch(circ)
        ax.text(1.15, y_mid, L["num"], ha="center", va="center",
                fontsize=16, fontweight="bold", color="white", zorder=4)

        ax.text(2.1, y_mid + 0.25, L["name"],
                ha="left", va="center", fontsize=9.5, fontweight="bold", color=L["color"])
        ax.text(2.1, y_mid - 0.2, L["sub"],
                ha="left", va="center", fontsize=8, color="#555555", style="italic")

        # ── middle ─────────────────────────────────────────────────────────────
        mid_box = FancyBboxPatch((9.0, y_top - row_h + 0.05), 6.2, row_h - 0.1,
                                 boxstyle="round,pad=0.05",
                                 facecolor="#FAFAFA", edgecolor="#E0E0E0", linewidth=0.8)
        ax.add_patch(mid_box)
        for j, bullet in enumerate(L["what"]):
            ax.text(9.3, y_top - 0.38 - j * 0.48, f"• {bullet}",
                    ha="left", va="center", fontsize=8.2, color="#333333")

        # ── right ──────────────────────────────────────────────────────────────
        right_box = FancyBboxPatch((15.4, y_top - row_h + 0.05), 4.35, row_h - 0.1,
                                   boxstyle="round,pad=0.05",
                                   facecolor=L["color"] + "0D", edgecolor=L["color"] + "50", linewidth=0.8)
        ax.add_patch(right_box)
        for j, bullet in enumerate(L["why"]):
            ax.text(15.65, y_top - 0.38 - j * 0.48, f"✓ {bullet}",
                    ha="left", va="center", fontsize=8, color=L["color"])

        # seta entre linhas (exceto última)
        if i < len(layers) - 1:
            ax.annotate("", xy=(4.5, y_top - row_h + 0.05),
                        xytext=(4.5, y_top - row_h + 0.05 - 0.0),
                        arrowprops=dict(arrowstyle="-|>", color="#AAAAAA", lw=1.2))

    # rodapé
    ax.text(10, 0.25, "Um processo contínuo de valor: Extrair → Limpar → Agregar → Disponibilizar → Documentar → Consumir",
            ha="center", va="center", fontsize=9, color="#777777")

    fig.savefig(os.path.join(OUT, "arquitetura_6_camadas.png"), dpi=120, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("✓  arquitetura_6_camadas.png")


# ══════════════════════════════════════════════════════════════════════════════
# 2. GRÁFICO DE BARRAS EMPILHADAS
# ══════════════════════════════════════════════════════════════════════════════
def make_barras_empilhadas():
    years = list(range(2015, 2025))
    groups = [
        "Alta tecnologia",
        "Média-alta tecnologia",
        "Média tecnologia",
        "Baixa tecnologia",
        "Intensivo em escala",
        "Fornecedores especializados",
        "Outros/N.class.",
    ]

    data = np.array([
        [18.5, 18.7, 19.0, 19.8, 20.5, 20.9, 20.8, 21.5, 22.0, 22.3],  # alta
        [20.3, 20.1, 19.8, 19.6, 19.4, 19.8, 19.0, 19.2, 18.7, 18.6],  # med-alta
        [17.8, 17.6, 17.4, 17.3, 17.1, 17.0, 18.8, 17.0, 17.2, 17.2],  # media
        [16.5, 16.2, 16.3, 16.2, 15.9, 15.9, 15.7, 15.3, 15.1, 15.0],  # baixa
        [11.8, 10.7, 10.4, 10.2, 10.4, 10.0, 10.2,  9.9,  9.2,  9.3],  # int-escala
        [ 8.3,  8.1,  8.1,  8.1,  8.1,  8.1,  8.0,  7.5,  7.4,  7.4],  # fornec
        [ 6.8,  8.6,  9.0,  8.8,  8.6,  8.3,  7.5,  9.6,  9.4,  9.2],  # outros
    ])

    fig, ax = plt.subplots(figsize=(13, 6.5))
    bottoms = np.zeros(len(years))
    bars = []
    for i, (grp, color) in enumerate(zip(groups, TECH_COLORS)):
        b = ax.bar(years, data[i], bottom=bottoms, color=color,
                   label=grp, edgecolor="white", linewidth=0.5)
        bars.append(b)
        # rótulo dentro da barra se houver espaço
        for j, (val, bot) in enumerate(zip(data[i], bottoms)):
            if val > 4.5:
                ax.text(years[j], bot + val / 2, f"{val:.1f}%",
                        ha="center", va="center", fontsize=6.2, color="white", fontweight="bold")
        bottoms += data[i]

    ax.set_xlim(years[0] - 0.6, years[-1] + 0.6)
    ax.set_ylim(0, 108)
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], fontsize=10)
    ax.set_ylabel("Participação no emprego formal (%)", fontsize=10)
    ax.set_title("Distribuição dos Empregos na Indústria por\nSetores de Intensidade Tecnológica",
                 fontsize=12, fontweight="bold", pad=12)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=4,
              fontsize=8, frameon=False)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.tick_params(left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "chart_barras_empilhadas.png"), dpi=130,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("✓  chart_barras_empilhadas.png")


# ══════════════════════════════════════════════════════════════════════════════
# 3. SLOPE CHART
# ══════════════════════════════════════════════════════════════════════════════
def make_slope_chart():
    groups = [
        "Alta tecnologia",
        "Média-alta tecnologia",
        "Média tecnologia",
        "Baixa tecnologia",
        "Intensivo em escala",
        "Fornecedores especializados",
        "Outros/N.class.",
    ]
    years = [2010, 2015, 2020, 2025]
    # participação (%) no valor adicionado
    vals = [
        [ 6.7,  7.0,  7.8,  8.6],   # alta
        [15.0, 15.0, 16.4, 16.4],   # med-alta
        [20.7, 20.2, 19.6, 18.7],   # media
        [24.8, 23.6, 22.0, 20.1],   # baixa
        [16.8, 16.8, 15.8, 14.6],   # intensivo
        [ 9.3,  9.1,  8.5, 13.7],   # fornec
        [ 7.2,  8.4, 10.0,  7.9],   # outros
    ]

    fig, ax = plt.subplots(figsize=(11, 7))
    x_pos = [0, 1, 2, 3]

    for i, (grp, row) in enumerate(zip(groups, vals)):
        color = TECH_COLORS[i]
        ax.plot(x_pos, row, color=color, marker="o", markersize=6,
                linewidth=2.0, zorder=3)

        # rótulo início
        ax.text(-0.08, row[0], f"{row[0]:.1f}%",
                ha="right", va="center", fontsize=8, color=color, fontweight="bold")
        # rótulo fim
        offset_y = 0
        ax.text(3.08, row[-1] + offset_y, f"{row[-1]:.1f}%",
                ha="left", va="center", fontsize=8, color=color, fontweight="bold")

    ax.set_xlim(-0.5, 4.2)
    ax.set_ylim(2, 30)
    ax.set_xticks(x_pos)
    ax.set_xticklabels([str(y) for y in years], fontsize=11, fontweight="bold")
    ax.set_ylabel("Participação (%)", fontsize=10)
    ax.set_title("Participação dos Setores de Intensidade Tecnológica\n"
                 "na Economia (%) — Evolução da participação no valor adicionado",
                 fontsize=11, fontweight="bold", pad=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.tick_params(left=False, bottom=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle="--", alpha=0.4)

    # legenda à direita
    handles = [mpatches.Patch(color=TECH_COLORS[i], label=g)
               for i, g in enumerate(groups)]
    ax.legend(handles=handles, loc="upper center",
              bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "chart_slope.png"), dpi=130,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("✓  chart_slope.png")


if __name__ == "__main__":
    make_arquitetura()
    make_barras_empilhadas()
    make_slope_chart()
    print("Todas as imagens geradas com sucesso.")
