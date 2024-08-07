from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from listado_respuestas import ListadoRespuestas

class Usuario():
    def __init__(self, correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region


    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, correo) -> None:
        self.__correo = correo
    
    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, edad) -> None:
        self.__edad = edad

    @property
    def region(self) -> List[int]:
        return self.__region

    @region.setter
    def region(self, region) -> None:
        self.__region = region


    def contestar_encuesta(self,encuesta: Union[Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion],respuestas: list) -> None:
        encuesta.agregar_respuesta(ListadoRespuestas(self, respuestas))
