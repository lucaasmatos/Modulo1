from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url_populacao   = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
url_fecundidade = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"

# Inicia a class para obter a tabela
wiki_populacao   = Scrapy_Table(url_populacao)
wiki_fecundidade = Scrapy_Table(url_fecundidade)


# Pegando as tabelas
tables_populacao   = wiki_populacao.get_tables(0)
tables_fecundidade = wiki_fecundidade.get_tables(1)

habitantes = []

for linha in tables_populacao[1:]:
    
  habit = int(linha[4])
  habitantes.append(habit)

habitanteMin = min(habitantes)
habitanteMax = max(habitantes)

for linha in tables_populacao[1:]:

  habit = int(linha[4])
  
  if(habit ==  habitanteMin):      
    estadoMin = linha[3]
    cidadeMin = linha[2]

  if(habit ==  habitanteMax):      
    estadoMax = linha[3]
    cidadeMax = linha[2]

for linha1 in tables_fecundidade[1:]:
  estado = linha1[1]
  taxa = linha1[2]

  if(estado ==  estadoMax):
    print("Maior taxa de fecundidade ",taxa, " Cidade ",cidadeMax," Estado ",estado)
    print("")
   
   

  if(estado ==  estadoMin):
    print("Menor taxa de fecundidade ",taxa, " Cidade ",cidadeMin, " Estado ",estado)
    print("")
