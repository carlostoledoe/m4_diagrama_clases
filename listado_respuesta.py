from usuario import Usuario

class ListadoRespuestas():
    def __init__(self, usuario: Usuario, respuestas: list) -> None:
        self.__usuario = Usuario
        self.__respuestas = respuestas
    
    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def respuestas(self) -> List[Respuesta]:
        return self.__respuestas

