import sys
import serial
import serial.tools.list_ports
from PyQt5 import uic, QtWidgets
import requests

qtCreatorFile = "PROYECTO_FINAL.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        for i in serial.tools.list_ports.comports():
            print(i)
            self.cbxCOM.addItem(str(i)[3:4])
        self.arduino = None
        self.btnConnect.clicked.connect(self.connect)
        self.btnAccept.clicked.connect(self.accept)

    def connect(self):
        if self.arduino is None:
            com = "COM" + self.cbxCOM.itemText(self.cbxCOM.currentIndex())
            self.arduino = serial.Serial(com, baudrate=9600, timeout=1)
            self.lblCOM.setText(com)
        else:
            self.mensaje("Ya se ha realizado la conexión.")

    # Área de los Slots
    #Datos del b.
    def accept(self):
        while self.arduino.inWaiting() > 0:
            valor = self.arduino.readline().decode().strip()
            if valor:
                datos = float(valor)
                print(datos)

                self.Et_valores.setText(str(datos))
                N = float(self.Et_valores.text())
                self.Et_numero.setText(str(N))

                #Datos del sensor
                general = {
                    'valor': N
                }

                #Solicitud
                url = 'http://localhost:3000/api/v1-sensors/sensors'
                headers = {'Content-Type': 'application/json'}
                response = requests.post(url, json=general, headers=headers)

                #Respuesta de API
                if response.status_code == 200:
                    print('Se enviaron los datos a la API')
                else:
                    print('No se enviaron los datos')

                if N <= 20.0:
                    self.Et_Led1.setStyleSheet(
                        "background-color: rgb(0, 255, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led2.setStyleSheet(
                        "background-color: rgb(0, 0, 48);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led3.setStyleSheet(
                        "background-color: rgb(62, 0, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led4.setStyleSheet(
                        "background-color: rgb(0, 0, 48);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led5.setStyleSheet(
                        "background-color: rgb(0, 27, 0);" + "border-radius: 25px;" + "border: 3px solid white;")

                elif N > 20.0 and N <= 40.0:
                    self.Et_Led1.setStyleSheet(
                        "background-color: rgb(0, 255, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led2.setStyleSheet(
                        "background-color: rgb(0, 0, 255);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led3.setStyleSheet(
                        "background-color: rgb(62, 0, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led4.setStyleSheet(
                        "background-color: rgb(0, 0, 48);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led5.setStyleSheet(
                        "background-color: rgb(0, 27, 0);" + "border-radius: 25px;" + "border: 3px solid white;")

                elif N > 40.0 and N <= 60.0:
                    self.Et_Led1.setStyleSheet(
                        "background-color: rgb(0, 255, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led2.setStyleSheet(
                        "background-color: rgb(0, 0, 255);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led3.setStyleSheet(
                        "background-color: rgb(255, 0, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led4.setStyleSheet(
                        "background-color: rgb(0, 0, 48);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led5.setStyleSheet(
                        "background-color: rgb(0, 27, 0);" + "border-radius: 25px;" + "border: 3px solid white;")

                elif N > 60.0 and N <= 80.0:
                    self.Et_Led1.setStyleSheet(
                        "background-color: rgb(0, 255, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led2.setStyleSheet(
                        "background-color: rgb(0, 0, 255);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led3.setStyleSheet(
                        "background-color: rgb(255, 0, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led4.setStyleSheet(
                        "background-color: rgb(0, 0, 255);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led5.setStyleSheet(
                        "background-color: rgb(0, 27, 0);" + "border-radius: 25px;" + "border: 3px solid white;")

                elif N > 80.0:
                    self.Et_Led1.setStyleSheet(
                        "background-color: rgb(0, 255, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led2.setStyleSheet(
                        "background-color: rgb(0, 0, 255);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led3.setStyleSheet(
                        "background-color: rgb(255, 0, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led4.setStyleSheet(
                        "background-color: rgb(0, 0, 255);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led5.setStyleSheet(
                        "background-color: rgb(0, 255, 0);" + "border-radius: 25px;" + "border: 3px solid white;")

                else:
                    self.Et_Led1.setStyleSheet(
                        "background-color: rgb(0, 27, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led2.setStyleSheet(
                        "background-color: rgb(0, 0, 48);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led3.setStyleSheet(
                        "background-color: rgb(62, 0, 0);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led4.setStyleSheet(
                        "background-color: rgb(0, 0, 48);" + "border-radius: 25px;" + "border: 3px solid white;")
                    self.Et_Led5.setStyleSheet(
                        "background-color: rgb(0, 27, 0);" + "border-radius: 25px;" + "border: 3px solid white;")

    def mensaje(self, texto):
        msj = QtWidgets.QMessageBox()
        msj.setText(texto)
        msj.exec_()

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
