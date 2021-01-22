import rpyc
import socket
from const import * 
from rpyc.utils.server import ThreadedServer
 
class MARKIII(rpyc.Service):
  value = []

  def exposed_append(self, data):
    
    print(f"Concatenando valor: {data}")
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    print(f"Retornando valor")
    return self.value
  
  def exposed_remove(self, data):
    if data in self.value:
      print(f"Removendo valor")
      self.value.remove(data)
      return self.value

  def exposed_search(self, data):
    if data in self.value:
      print(f"Retornando valor e posicao")
      return (data, self.value.index(data) + 1) 
           
if __name__ == "__main__":
  print(f"Criaando server MARK III") 
  server = ThreadedServer(MARKIII, port = PORT)
  print(f"Conectando ao Server de diretório")  
  ListaDiretorio  = rpyc.connect(ListaDiretorio ,PORTDIRETORIO)
  print(f"Obtendo IPadress da MARK III")  
  ipAdress = socket.gethostbyname(socket.gethostname())
  print(f"Registrando no Server de diretório") 
  ListaDiretorio .root.exposed_registraServer('MARK III',ipAdress,PORT)
  server.start()

