import socketserver#librería que simplifica la creación de servidores tanto TCP como UDP


class TCPSocketHandler(socketserver.BaseRequestHandler):
  #Clase para manejar las conexiones, se instancia una por cliente

  def handle(self):#self se utiliza como referencia al propio objeto
    #medodo a sobreescribir para nuestro propio manejo
    #self.request se refiere al socket client conectado
    #imprime la dirección IP y el puerto del cliente que se conecta
    print (f"Se han conectado desde: {self.client_address[0]} [{self.client_address[1]}]")
    while True:
      self.data = self.request.recv(128).strip()#recibimos los datos
      print("Datos recibidos: ", self.data)
      #remitimos los mismos datos en mayúscula
      self.request.sendall(self.data.upper())
      if self.data == b"":#si el cliente envía mensaje vacío cerramos conexión
        break
      if self.data ==b"#":
        raise KeyboardInterrupt#si el cliente envía # se genera una excepción y hace que el servidor termine por completo

if __name__ == "__main__":  
  HOST, PORT = "", 2000
  #HOST -> dirección IP del servidor, al estar vacío acpeta conexiones desde cualquier dirección
  #PORT -> puerto en el que el servidor estará escuchando

  # instanciamos el socket servidor con la clase asociada de callback
  # es decir, creación del servidor
  server = socketserver.TCPServer((HOST, PORT), TCPSocketHandler)#la clase TCPSocketHandler defina cómo interactual con los clientes.
 
  # activamos el servidor (ponemos a la espera de clientes)
  # podemos provocar una excepción con Ctrl-C
  try:
    server.serve_forever()#servidor modo escucha
  except KeyboardInterrupt:#si se pulsa ctrl+c se lanza excepción que detiene servidor
    print ("servidor finalizado")
    