# Importez les modules nécessaires de PyModbus
from pymodbus.client import ModbusSerialClient

# Paramètres de communication série pour votre PZEM-004T
serial_port = "/dev/ttyUSB0"  # Changez cela en fonction de votre configuration

# Créez une instance du client Modbus
client = ModbusSerialClient(method="rtu", port=serial_port, baudrate=9600, stopbits=1, bytesize=8, parity='N')

# Ouvrez la connexion série
client.connect()

try:
  adr = 2
  client.write_register(2, adr)
  print("Adresse forcée.")
except Exception as e:
  print("Erreur : " + str(e))
                
client.close()
                