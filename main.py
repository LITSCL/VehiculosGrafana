import time

from models.dto.tractocamion import Tractocamion
from models.dto.portacontenedor import Portacontenedor
from controllers.tractocamion_controlador import TractocamionControlador
from controllers.portacontenedor_controlador import PortacontenedorControlador

class Main:
    __tractocamion_controlador: TractocamionControlador = TractocamionControlador()
    __portacontenedor_controlador: PortacontenedorControlador = PortacontenedorControlador()
    
    def start(self) -> None:
        contador: int = 0
        while (True):
            tractocamion_1: Tractocamion = Tractocamion("TRA-01")
            tractocamion_2: Tractocamion = Tractocamion("TRA-02")
            portacontenedor_1: Portacontenedor = Portacontenedor("POR-01")
            portacontenedor_2: Portacontenedor = Portacontenedor("POR-02")
            print("SQL TRA-01: " + str(self.__tractocamion_controlador.guardar(tractocamion_1)))
            print("SQL TRA-02: " + str(self.__tractocamion_controlador.guardar(tractocamion_2)))
            print("SQL POR-01: " + str(self.__portacontenedor_controlador.guardar(portacontenedor_1)))
            print("SQL POR-02: " + str(self.__portacontenedor_controlador.guardar(portacontenedor_2)))
            print("-----------------")
            contador+=1
            if (contador == 2500):
                self.__tractocamion_controlador.borrar_todo()
                self.__portacontenedor_controlador.borrar_todo()
            time.sleep(1)
    
main: Main = Main()

main.start()