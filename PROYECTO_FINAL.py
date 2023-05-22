import sys
import serial
import serial.tools.list_ports
from PyQt5 import uic, QtWidgets

qtCreatorFile = "PROYECTO_FINAL.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        for i in serial.tools.list_ports.comports():
            print(i)
            self.cbxCOM.addItem(str(i)[3:4])
        self.arduino = None
        self.btnConnect.clicked.connect(self.connect)
        self.btnAccept.clicked.connect(self.accept)

    def connect(self):
        if self.arduino == None:
            com = "COM" + self.cbxCOM.itemText(self.cbxCOM.currentIndex())
            self.arduino = serial.Serial(com, baudrate=9600, timeout=1)
            self.lblCOM.setText(com)
        else:
            self.mensaje("Ya se ha realizado la conexión.")

    def accept(self):
        while self.arduino.inWaiting() > 0:
            valor = self.arduino.readline().decode().strip()
            if valor:
                datos = float(valor)
                print(datos)

                self.Et_valores.setText(str(datos))
                N = float(self.Et_valores.text())
                self.Et_numero.setText(str(N))

                if N <= 2.0:
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

                elif N > 2.0 and N <= 4.0:
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

                elif N > 4.0 and N <= 6.0:
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

                elif N > 6.0 and N <= 8.0:
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

                elif N > 8.0:
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
