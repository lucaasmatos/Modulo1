from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url_populacao   = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"


# Inicia a class para obter a tabela
wiki_populacao   = Scrapy_Table(url_populacao)


# Pegando as tabelas
tables_populacao   = wiki_populacao.get_tables(0)


print("Municipio")
print("----------------------------")
for linha in tables_populacao[1:1000]:

    nome = linha[2]
    qty = int(linha[4])
    if(qty < 70000):
      print(nome)
