# Importez les modules nécessaires de PyModbus
from pymodbus.client import ModbusSerialClient

# Paramètres de communication série pour votre PZEM-004T
serial_port = "/dev/ttyUSB0"  # Changez cela en fonction de votre configuration

# Créez une instance du client Modbus
client = ModbusSerialClient(method="rtu", port=serial_port, baudrate=9600, stopbits=1, bytesize=8, parity='N')

# Ouvrez la connexion série
client.connect()

try:
    data = client.read_input_registers(0, 10, slave=1)
    if data:
        print("Valeurs lues : " + str(data.registers))
        voltage = data.getRegister(0) / 10.0 # [V]
        current = (data.getRegister(1) + (data.getRegister(2) << 16)) / 1000.0 # [A]
        power = (data.getRegister(3) + (data.getRegister(4) << 16)) / 10.0 # [W]
        energy = data.getRegister(5) + (data.getRegister(6) << 16) # [Wh]
        frequency = data.getRegister(7) / 10.0 # [Hz]
        powerFactor = data.getRegister(8) / 100.0
        alarm = data.getRegister(9) # 0 = no alarm# La réponse contient les valeurs lues
        print('Voltage [V]: ', voltage)
        print('Current [A]: ', current)
        print('Power [W]: ', power) # active power (V * I * power factor)
        print('Energy [Wh]: ', energy)
        print('Frequency [Hz]: ', frequency)
        print('Power factor []: ', powerFactor)
        print('Alarm : ', alarm)
    else:
        print("Aucune réponse.")
except Exception as e:
    print("Erreur : " + str(e))

# Assurez-vous de fermer la connexion après avoir terminé
client.close()
                
print("************************")                