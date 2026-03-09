
class ProdutoImportado:

    def __init__(self, ncm, descricao, valor_cif, aliquota):
        self.ncm = ncm
        self.descricao = descricao
        self.valor_cif = valor_cif
        self.aliquota = aliquota

    def tarifa_importacao(self):
        return self.valor_cif * self.aliquota

    def valor_final(self):
        return self.valor_cif + self.tarifa_importacao()


produtos = [
    ProdutoImportado("8471.30.12","Notebook",1000,0.14),
    ProdutoImportado("8517.12.31","Smartphone",800,0.16),
    ProdutoImportado("8528.72.00","Televisor",1200,0.20)
]

for p in produtos:
    print(p.descricao, p.valor_final())
