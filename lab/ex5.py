from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

site_connect = Scrapy_Table(url)

tables = site_connect.get_tables(5)

partidos = { }

for linha in tables[1:]:


    partido = linha[1]

    if partido in partidos:

       partidos[partido] += 1
    else:

       partidos[partido] = 1

num_vereadores = 0
nome_partido   = 0

for part in partidos:

    if partidos[part] > num_vereadores:

        nome_partido   = part
        num_vereadores =  partidos[part] 
            
print("O partido ", nome_partido,' foi o que elegeu mais vereadores, com um total de: ',num_vereadores,'vereadores') 