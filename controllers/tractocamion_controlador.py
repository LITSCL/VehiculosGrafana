from models.dto.tractocamion import Tractocamion
from models.dao.tractocamion_dao import TractocamionDAO

class TractocamionControlador:
    __dao_tractocamion: TractocamionDAO = TractocamionDAO()
    
    def guardar(self, tractocamion: Tractocamion) -> bool:
        return self.__dao_tractocamion.save(tractocamion)
    
    def borrar_todo(self) -> None:
        self.__dao_tractocamion.delete_all()