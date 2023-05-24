import sys
import serial
import serial.tools.list_ports
from PyQt5 import uic, QtWidgets
from API import *

qtCreatorFile = "PROYECTO_FINAL.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

qtCreatorFile_dos = "untitled.ui"  # Nombre del archivo de la segunda ventana aquí.
Ui_SecondWindow, QtBaseClass = uic.loadUiType(qtCreatorFile_dos)

class SecondWindow(QtWidgets.QMainWindow, Ui_SecondWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_SecondWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.bt_regresar.clicked.connect(self.regresar_primera)
        self.btn_buscar.clicked.connect(self.buscar)
        self.bt_regresar_2.clicked.connect(self.regresar_primera_dos)
        self.btn_ok.clicked.connect(self.ok)
        self.btn_borrar.clicked.connect(self.borrar)

    # Área de los Slots
    def regresar_primera(self):
        self.primera_ventana = MyApp()  # Instancia de la primera ventana
        self.primera_ventana.show()  # Muestra la primera ventana

    def buscar(self):
        codigo = int(self.line_codigo.text())
        updateSensor_wPatch(id)

    def regresar_primera_dos(self):
        self.primera_ventana = MyApp()  # Instancia de la primera ventana
        self.primera_ventana.show()  # Muestra la primera ventana

    def ok(self):
        codigo_dos = int(self.line_codigo_dos.text())
        updateSensor_wPatch(id)

    def borrar(self):

        deleteSensor(id)

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
    def accept(self):
        id = 0
        while self.arduino.inWaiting() > 0:
            valor = self.arduino.readline().decode().strip()
            if valor:
                datos = float(valor)
                insertRecord_wPost(id, datos)
                id += 1

                self.Et_valores.setText(str(datos))
                N = float(self.Et_valores.text())

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

                self.segundo_ventana = SecondWindow()  # Instancia de la segunda ventana
                self.segundo_ventana.show()  # Muestra la segunda ventana

    def mensaje(self, texto):
        msj = QtWidgets.QMessageBox()
        msj.setText(texto)
        msj.exec_()

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())