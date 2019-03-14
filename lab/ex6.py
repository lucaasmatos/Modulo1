from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

site_connect = Scrapy_Table(url)

tables = site_connect.get_tables(5)

partidos =  {}

for linha in tables[1:]:

    partido = linha[1]

    n_voto = float(linha[2].split(" ")[0])

    if partido in partidos:

       partidos[partido] = partidos[partido] + n_voto
    else:

       partidos[partido] = n_voto

for partido in partidos:
    print("O partido ", partido, 'teve',partidos[partido], 'votos.') 