# Importez les modules nécessaires de PyModbus
from pymodbus.client import ModbusSerialClient

# Paramètres de communication série pour votre PZEM-004T
serial_port = "/dev/ttyUSB0"  # Changez cela en fonction de votre configuration

# Créez une instance du client Modbus
client = ModbusSerialClient(method="rtu", port=serial_port, baudrate=9600, stopbits=1, bytesize=8, parity='N')

# Ouvrez la connexion série
client.connect()

# Reset energy count
# 0x01 Slave address
# 0x42 Magic code
# 0x80 CRC for slave address (0x01)
# 0x11 CRC for magic code (0x42)
data = [0x01, 0x42, 0x80, 0x11]

# Utilisez la méthode write_register pour appeler la fonction 42
try:
  print(client.send(data))
  print("Réinitialisation de l'énergie réussie.")
except Exception as e:
  print("Erreur : " + str(e))
                
# Assurez-vous de fermer la connexion après avoir terminé
client.close()
                