# 1. Classe planta com seus atributos e métodos
class Planta:
    def __init__(self,id, ambiente, nome, especie, origem, regar, imagem):
        self.__id = id
        self.__ambiente = ambiente
        self.__nome = nome
        self.__especie = especie
        self.__origem = origem
        self.__regar = regar
        self.__imagem = imagem

    # 2. Método get_especie para evitar repetições
    def get_especie(self):
        return self.__especie

    # 3. Método para converter o objeto Planta em um dicionário.
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