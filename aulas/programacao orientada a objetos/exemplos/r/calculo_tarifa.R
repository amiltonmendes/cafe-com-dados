
library(R6)

ProdutoImportado <- R6Class(
 "ProdutoImportado",
 public=list(
  ncm=NULL,
  descricao=NULL,
  valor_cif=NULL,
  aliquota=NULL,

  initialize=function(ncm,descricao,valor_cif,aliquota){
   self$ncm <- ncm
   self$descricao <- descricao
   self$valor_cif <- valor_cif
   self$aliquota <- aliquota
  },

  tarifa_importacao=function(){
   self$valor_cif*self$aliquota
  },

  valor_final=function(){
   self$valor_cif+self$tarifa_importacao()
  }
 )
)

notebook <- ProdutoImportado$new("8471.30.12","Notebook",1000,0.14)
notebook$valor_final()
