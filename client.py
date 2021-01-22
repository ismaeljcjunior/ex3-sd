import rpyc
from const import *

class Client:
  print(f"Iniciando conexão com server de diretórios : {SERVERDIRETORIO} e porta: {PORTDIRETORIO}")
  
  conn = rpyc.connect(ListaDiretorio , PORTDIRETORIO) # Connect to the server
  
  print(f"Fazendo busca de Pizzaria")
  
  nomeDir  =  conn.root.exposed_buscaServer('MARk III')
  
  print(f"Busca finalizada, Servidor encontrado: ")
  print(nomeDir) # Print the result
