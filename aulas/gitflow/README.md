# Aula: Git Flow e Controle de Versão

Este projeto contém slides em **Quarto + RevealJS** sobre Git Flow e controle de versão.

## Contexto da aula

**Git Flow e Controle de Versão** - Gestão eficiente de código e colaboração para programadores iniciantes em repositórios.

## Objetivos

- Compreender a filosofia do Git Flow
- Aprender comandos essenciais para controle de versão  
- Praticar criação de branches e merge requests
- Comparar ferramentas: VS Code vs RStudio/Posit
- Desenvolver boas práticas de colaboração

## Requisitos

### Dependencias da aula

As dependencias estao centralizadas no arquivo [environment.yml](environment.yml).

Ele inclui:
- Python e bibliotecas para exemplos (`pandas`, `matplotlib`, `seaborn`)
- Git
- Quarto
- R e pacotes usados nos exemplos (`dplyr`, `ggplot2`)

### Ferramentas necessarias
- VS Code com extensao Git/GitHub
- RStudio/Posit (opcional para comparacao)
- Conta no GitHub/GitLab

## Instalacao do ambiente

Usando Conda:

```bash
conda env create -f environment.yml
conda activate gitflow-aula
```

Se voce ja usa o ambiente `quarto_reports`, pode instalar as dependencias nele:

```bash
conda activate quarto_reports
conda env update --name quarto_reports --file environment.yml
```

## Como executar

No terminal desta pasta:

```bash
quarto preview
```

ou

```bash
quarto render
```

## Estrutura

```
gitflow/
├── slides/
│   └── aula_gitflow.qmd       # Apresentação principal
├── assets/
│   └── capa.css               # Estilos da apresentação
├── _quarto.yml                # Configuração do Quarto
├── _variables.yml             # Variáveis da apresentação
└── README.md                  # Este arquivo
```

## Conteúdo da apresentação

1. **Introdução ao controle de versão**
   - O que é e por que usar
   - Problemas resolvidos

2. **Filosofia do Git Flow**
   - Modelo de ramificação
   - Tipos de branches

3. **Comandos essenciais**
   - Iniciando repositórios
   - Trabalhando com branches
   - Fazendo commits

4. **Fluxos de trabalho**
   - GitHub Flow vs Git Flow
   - Processo completo de desenvolvimento

5. **Ferramentas comparadas**
   - VS Code: interface Git integrada
   - RStudio: Git tab e projetos R

6. **Boas práticas**
   - Estrutura de commits
   - Nomenclatura de branches
   - Pull/Merge Requests

7. **Resolução de problemas**
   - Conflitos de merge
   - Comandos de emergência

## Material complementar

### Recursos práticos inclusos:
- Diagramas Mermaid para visualizar fluxos
- Exemplos de código comentados
- Comparação side-by-side de ferramentas
- Templates de Pull Request
- Checklists de boas práticas

### Para aprofundamento:
- GitHub Learning Lab
- Interactive Git Tutorial
- Git visualization tools