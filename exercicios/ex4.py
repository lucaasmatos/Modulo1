from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url_populacao   = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"


# Inicia a class para obter a tabela
wiki_populacao   = Scrapy_Table(url_populacao)


# Pegando as tabelas
tables_populacao   = wiki_populacao.get_tables(0)

habitantes = []

for linha in tables_populacao[1:]:
    
  habit = int(linha[4])
  habitantes.append(habit)

habitante = min(habitantes)
habitante

for linha in tables_populacao[1:]:
  municipio = linha[2]
  estado = linha[3]
  habit = int(linha[4])
  
  if(habit ==  habitante):
      print("O menor Municipio é ", municipio)
      print("Seu numero de habitantes é ", habit)
      print("Pertencente ao estado de ", estado)
  