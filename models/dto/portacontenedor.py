from helpers.valor_aleatorio_helper import ValorAleatorioHelper

class Portacontenedor:
    __nombre: str = None
    __rpm: int = None
    __velocidad: int = None
    __temperatura_motor: int = None
    __temperatura_ambiente: int = None
    __porcentaje_carga: int = None
    __horometro: int = None
    __latitud: float = None
    __longitud: float = None
    __fecha: str = None
    
    def __init__(self, nombre: str) -> None:
        coordenadas: list = ValorAleatorioHelper().generar_coordenadas_aleatorias()
        
        self.__nombre = nombre
        self.__rpm = ValorAleatorioHelper().generar_numero_aleatorio(800, 3200)
        self.__velocidad = ValorAleatorioHelper().generar_numero_aleatorio(0, 40)
        self.__temperatura_motor = ValorAleatorioHelper().generar_numero_aleatorio(50, 120)
        self.__temperatura_ambiente = ValorAleatorioHelper().generar_numero_aleatorio(15, 25)
        self.__porcentaje_carga = ValorAleatorioHelper().generar_numero_aleatorio(0, 100)
        self.__horometro = ValorAleatorioHelper().generar_numero_aleatorio(5000, 15000)
        self.__latitud = coordenadas[0]
        self.__longitud = coordenadas[1]

    def get_nombre(self) -> str:
        return self.__nombre

    def get_rpm(self) -> int:
        return self.__rpm

    def get_velocidad(self) -> int:
        return self.__velocidad
    
    def get_temperatura_motor(self) -> int:
        return self.__temperatura_motor

    def get_temperatura_ambiente(self) -> int:
        return self.__temperatura_ambiente
    
    def get_porcentaje_carga(self) -> int:
        return self.__porcentaje_carga
    
    def get_horometro(self) -> int:
        return self.__horometro
    
    def get_latitud(self) -> float:
        return self.__latitud
    
    def get_longitud(self) -> float:
        return self.__longitud
    
    def get_fecha(self) -> str:
        return self.__fecha

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_rpm(self, rpm: int) -> None:
        self.__rpm = rpm
        
    def set_velocidad(self, velocidad: int) -> None:
        self.__velocidad = velocidad

    def set_temperatura_motor(self, temperatura_motor: int) -> None:
        self.__temperatura_motor = temperatura_motor

    def set_temperatura_ambiente(self, temperatura_ambiente: int) -> None:
        self.__temperatura_ambiente = temperatura_ambiente
        
    def set_porcentaje_carga(self, porcentaje_carga: int) -> None:
        self.__horometro = porcentaje_carga
        
    def set_horometro(self, horometro: int) -> None:
        self.__horometro = horometro
        
    def set_latitud(self, latitud: float) -> None:
        self.__latitud = latitud
        
    def set_longitud(self, longitud: float) -> None:
        self.__longitud = longitud
        
    def set_fecha(self, fecha: str) -> None:
        self.__fecha = fecha