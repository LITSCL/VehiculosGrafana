from database.conexion import Conexion
from models.dto.portacontenedor import Portacontenedor

class PortacontenedorDAO:
    __db: Conexion = Conexion()
    
    def save(self, portacontenedor: Portacontenedor) -> bool:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"INSERT INTO portacontenedor VALUES('{portacontenedor.get_nombre()}', {portacontenedor.get_rpm()}, {portacontenedor.get_velocidad()}, {portacontenedor.get_temperatura_motor()}, {portacontenedor.get_temperatura_ambiente()}, {portacontenedor.get_porcentaje_carga()}, {portacontenedor.get_horometro()}, {portacontenedor.get_latitud()}, {portacontenedor.get_longitud()}, NOW())"
                
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
                query: str = f"DELETE FROM portacontenedor"
                
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