import socket

HOST, PORT = "10.209.86.144", 2000
data = "hola soy mady "


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  #conectar
  sock.connect((HOST, PORT))
  #enviar
  sock.sendall(bytes(data + "\n", "utf-8"))
  #recibir
  recibido = str(sock.recv(64), "utf-8")

print("Enviado:  {}".format(data))
print("Recibido: {}".format(recibido))
input("Press enter to exit...")