import os

arquivo_fonte = './dados.json'
arquivo_destino = './json_data.txt'

# Method one
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

# Method two

open(arquivo_destino, "w").write(open(arquivo_fonte, "r").read())
