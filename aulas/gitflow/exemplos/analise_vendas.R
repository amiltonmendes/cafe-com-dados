# Exemplo prático: Análise de Vendas - Alteração feita por Oscar a partir da branch 'desenvolvimento'
# Nova alteração a partir do desenvolvimento.
# Este arquivo será usado para demonstrar fluxo Git

# Carregar bibliotecas necessárias
library(ggplot2)
library(dplyr)

# Função principal de análise
analise_vendas <- function(dados_vendas) {
  # TODO: Na aula, cada aluno criará uma branch para implementar 
  # uma funcionalidade específica nesta função
  
  cat("Iniciando análise de vendas...\n")
  
  # Base para expansion
  resultado <- dados_vendas %>%
    summary()
    
  return(resultado)
}

# Função de exemplo para branch feature/visualizacao
criar_grafico_vendas <- function(dados) {
  # TODO: Implementar na branch feature/visualizacao
  # Esta função será desenvolvida por um dos alunos
  
  cat("Criando gráfico de vendas...\n")
  # Placeholder para implementação
}

# Função de exemplo para branch feature/relatorio
gerar_relatorio <- function(dados) {
  # TODO: Implementar na branch feature/relatorio  
  # Esta função será desenvolvida por outro aluno
  
  cat("Gerando relatório de vendas...\n")
  # Placeholder para implementação
}

# Dados de exemplo para teste
dados_exemplo <- data.frame(
  produto = c("A", "B", "C", "D", "E"),
  vendas = c(150, 230, 180, 120, 200),
  regiao = c("Norte", "Sul", "Centro", "Norte", "Sul")
)

# Executar análise básica
resultado <- analise_vendas(dados_exemplo)
print(resultado)

# Feature - André

funcao_andre <- function(...){print(paste0("Printa o seguinte termo: ", ...))}

funcao_andre("aaa")
