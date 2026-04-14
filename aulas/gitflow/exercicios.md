# Exercícios Práticos - Git Flow

## Exercício 1: Criando seu primeiro branch

**Objetivo**: Cada aluno criará um branch e implementará uma funcionalidade específica.

### Passos:

1. **Clone o repositório** (se ainda não fez)
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd cafe-com-dados
   ```

2. **Atualize o branch principal**
   ```bash
   git checkout main
   git pull origin main
   ```

3. **Crie seu branch pessoal**
   ```bash
   git checkout -b feature/[SEU_NOME]-[FUNCIONALIDADE]
   ```

   **Exemplos de nomes de branch:**
   - `feature/maria-visualizacao`
   - `feature/joao-relatorio`
   - `feature/ana-analise-regional`

4. **Implemente sua funcionalidade** (escolha uma):

   ### Opção A: Visualização de Dados
   - Arquivo: `exemplos/analise_vendas.R` ou `exemplos/analise_vendas.py`
   - Implementar função `criar_grafico_vendas()` ou `criar_visualizacao()`
   - Criar gráfico de barras ou linha com os dados

   ### Opção B: Relatório Automático
   - Implementar função `gerar_relatorio()` ou `exportar_relatorio()`
   - Gerar summary estatístico dos dados
   - Salvar em arquivo .txt ou .html

   ### Opção C: Análise por Região
   - Implementar função `analise_por_regiao()`
   - Agrupar vendas por região
   - Calcular médias e totais

5. **Teste sua implementação**
   ```bash
   # Para R
   Rscript exemplos/analise_vendas.R
   
   # Para Python  
   python exemplos/analise_vendas.py
   ```

6. **Commit suas mudanças**
   ```bash
   git add .
   git commit -m "Implementa [DESCRICAO_DA_FUNCIONALIDADE]"
   ```

7. **Push do branch**
   ```bash
   git push origin feature/[SEU_NOME]-[FUNCIONALIDADE]
   ```

## Exercício 2: Pull Request / Merge Request

1. **Abra PR no GitHub/GitLab**
   - Vá para o repositório na web
   - Clique "Compare & pull request"
   - Preencha título e descrição

2. **Template para descrição do PR**:
   ```markdown
   ## Funcionalidade implementada
   [Descreva o que foi implementado]

   ## Arquivos alterados
   - exemplos/analise_vendas.R (ou .py)

   ## Como testar
   1. Execute: `Rscript exemplos/analise_vendas.R`
   2. Verifique se [resultado esperado]

   ## Screenshots/Output
   [Cole aqui o resultado da execução]
   ```

3. **Aguarde review do instrutor**

4. **Faça merge após aprovação**

## Exercício 3: Conflitos e Resoluções

**Cenário**: Dois alunos modificaram a mesma linha de código.

1. **Simular conflito** (instrutor direcionará)
2. **Tentar fazer merge**
3. **Resolver conflito manualmente**
4. **Commit da resolução**

## Exercício 4: Workflow Completo

**Objetivo**: Simular um dia de trabalho real.

1. **Pegar nova task** (instrutor atribuirá)
2. **Criar branch apropriado** 
3. **Desenvolver funcionalidade**
4. **Escrever testes** (se aplicável)
5. **Documentar mudanças**
6. **Abrir PR com review**
7. **Merge após aprovação**
8. **Limpeza de branches**

## Dicas e Boas Práticas

### Commits:
- ✅ `git commit -m "Adiciona gráfico de vendas por mês"`
- ❌ `git commit -m "mudanças"`

### Branches:
- ✅ `feature/dashboard-vendas`
- ❌ `nova-funcao`

### Pull Requests:
- Sempre incluir descrição detalhada
- Testar antes de enviar
- Responder reviews construtivamente

## Comandos de Emergência

```bash
# Desfazer mudanças não salvas
git checkout -- nome_arquivo.R

# Voltar para commit anterior
git reset --hard HEAD~1

# Ver diferenças
git diff

# Ver status atual
git status

# Ver histórico
git log --oneline

# Listar branches
git branch -a
```

## Próximos Passos

Após dominar estes exercícios:
1. **GitHub Actions** para CI/CD
2. **Semantic Versioning** para releases  
3. **Conventional Commits** para padronização
4. **Git Hooks** para validações automáticas