import random

class ValorAleatorioHelper:
    
    def generar_numero_aleatorio(self, minimo: int, maximo: int) -> int:
        numero_aleatorio: int = random.randint(minimo, maximo)
        return numero_aleatorio
    
    def generar_coordenadas_aleatorias(self) -> list:
        coordenadas: list = [
            [-33.5920098, -71.6328286],
            [-33.5920098, -71.6333286],
            [-33.5920098, -71.6338286],
            [-33.5920098, -71.6343286],
            [-33.5920098, -71.6348286],
            [-33.5920098, -71.6353286],
            [-33.5920098, -71.6358286],
            [-33.5920098, -71.6363286],
            [-33.5920098, -71.6368286],
            [-33.5920098, -71.6373286]
        ]
        return coordenadas[random.randint(0, 9)]