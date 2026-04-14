"""
Exemplo prático: Análise de Vendas em Python
Este arquivo será usado para demonstrar fluxo Git
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalisadorVendas:
    """Classe para demonstrar desenvolvimento colaborativo com Git"""
    
    def __init__(self, dados_vendas):
        self.dados = dados_vendas
        print("Analisador de vendas inicializado")
    
    def resumo_basico(self):
        """Análise básica dos dados"""
        # TODO: Na aula, cada aluno criará uma branch para 
        # implementar funcionalidades específicas
        
        print("=== Resumo Básico ===")
        print(f"Total de produtos: {len(self.dados)}")
        print(f"Vendas totais: {self.dados['vendas'].sum()}")
        return self.dados.describe()
    
    def criar_visualizacao(self):
        """TODO: Implementar na branch feature/visualizacao-python"""
        # Esta função será desenvolvida por um dos alunos
        print("Criando visualização... (TODO)")
        pass
    
    def exportar_relatorio(self, formato='html'):
        """TODO: Implementar na branch feature/export-python"""
        # Esta função será desenvolvida por outro aluno
        print(f"Exportando relatório em {formato}... (TODO)")
        pass
    
    def analise_por_regiao(self):
        """TODO: Implementar na branch feature/analise-regional"""
        # Mais uma funcionalidade para demonstrar branches
        print("Analisando vendas por região... (TODO)")
        pass

# Dados de exemplo
def criar_dados_exemplo():
    """Cria dataset de exemplo para demonstrações"""
    return pd.DataFrame({
        'produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
        'vendas': [150, 230, 180, 120, 200],
        'regiao': ['Norte', 'Sul', 'Centro', 'Norte', 'Sul'],
        'mes': ['Jan', 'Jan', 'Fev', 'Fev', 'Mar']
    })

# Executar exemplo básico
if __name__ == "__main__":
    # Criar dados de teste  
    dados = criar_dados_exemplo()
    
    # Inicializar analisador
    analisador = AnalisadorVendas(dados)
    
    # Executar análise básica
    resultado = analisador.resumo_basico()
    print(resultado)