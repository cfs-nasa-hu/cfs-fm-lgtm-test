import socket
import os

def run():
  return 'HOSTNAME: {}'.format(socket.gethostbyname())
