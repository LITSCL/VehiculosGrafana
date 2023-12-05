from database.conexion import Conexion
from models.dto.tractocamion import Tractocamion

class TractocamionDAO:
    __db: Conexion = Conexion()
    
    def save(self, tractocamion: Tractocamion) -> bool:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"INSERT INTO tractocamion VALUES('{tractocamion.get_nombre()}', {tractocamion.get_rpm()}, {tractocamion.get_velocidad()}, {tractocamion.get_temperatura_motor()}, {tractocamion.get_temperatura_ambiente()}, {tractocamion.get_porcentaje_carga()}, {tractocamion.get_horometro()}, {tractocamion.get_latitud()}, {tractocamion.get_longitud()}, NOW())"
                
                cursor.execute(query)
                conexion.commit()
                
                if (cursor.rowcount >= 1):
                    return True
                else:
                    return False
            except:
                return False 
            finally:
                cursor.close()
                conexion.close()
        else:
            return False
        
    def delete_all(self) -> bool:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"DELETE FROM tractocamion"
                
                cursor.execute(query)
                conexion.commit()
                return True
            except:
                return False 
            finally:
                cursor.close()
                conexion.close()
        else:
            return False