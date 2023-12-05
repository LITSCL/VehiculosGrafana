from models.dto.portacontenedor import Portacontenedor
from models.dao.portacontenedor_dao import PortacontenedorDAO

class PortacontenedorControlador:
    __dao_portacontenedor: PortacontenedorDAO = PortacontenedorDAO()
    
    def guardar(self, portacontenedor: Portacontenedor) -> bool:
        return self.__dao_portacontenedor.save(portacontenedor)
    
    def borrar_todo(self) -> None:
        self.__dao_portacontenedor.delete_all()