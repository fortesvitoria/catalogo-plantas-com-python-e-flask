class Planta:
    def __init__(self,id, ambiente, nome, especie, origem, regar, imagem):
        self.__id = id
        self.__ambiente = ambiente
        self.__nome = nome
        self.__especie = especie
        self.__origem = origem
        self.__regar = regar
        self.__imagem = imagem

    def to_dict(self):
        return {
        "id": self.__id,
        "ambiente": self.__ambiente,
        "nome": self.__nome,
        "especie": self.__especie,
        "origem": self.__origem,
        "regar": self.__regar,
        "imagem": self.__imagem
        }