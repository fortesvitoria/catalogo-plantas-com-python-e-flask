import json 
from models.cls_plantas import Planta
import uuid #biblioteca para gerar id unico

# 1. Cria classe catalogo plantas
class CatalogoPlantas:
    def __init__(self, arquivo_dados="data/dados_plantas.json"):
        self.arquivo_dados = arquivo_dados # Guarda o nome do arquivo
        self.__plantas = {} # Dicionario para armazenar dados
        self.carregar_dados(arquivo_dados) # Chama metodo para carregar dados
    
    #2. Metodo para carregar dados
    def carregar_dados(self, arquivo_dados):
        try:
            with open(arquivo_dados, 'r', encoding='utf-8') as f: dados = json.load(f)
            # Looping para instanciar os objetos da classe Planta, do arquivo cls_plantas na pasta models
            # Ao instanciar, pegamos os dados do arquivo .json e transformamos em um objeto
            for item in dados['plantas']:
                planta = Planta(
                    id=item.get("id"),
                    ambiente=item.get("ambiente"),
                    nome=item.get("nome"),
                    especie=item.get("especie"),
                    origem=item.get("origem"),
                    regar=item.get("regar"),
                    imagem=item.get("imagem")
                )
                # Armazena o objeto planta recém-criado dentro do dicionário self.__plantas, usando o ID da planta como chave.
                self.__plantas[item.get("id")] = planta
        
        except (FileNotFoundError, json.JSONDecodeError):
            self.__plantas = {}
    
    # 3. Método que converte cada objeto Planta em um dicionário e retorna todos em uma lista.
    def get_plantas(self):
        return [planta.to_dict() for planta in self.__plantas.values()]
    
    # 4. Método para criar, adicionar e salvar a nova planta no arquivo .json
    def add_planta(self, nome, especie, ambiente, origem, regar, imagem):
        nova_especie_lower = especie.lower()

        # Verifica se já existe a especie salva
        for planta_existente in self.__plantas.values():
            if planta_existente.get_especie().lower() == nova_especie_lower:
                print(f"Não foi possível cadastrar. A espécie {especie} já existe no catálogo.")
                return False #falhou
        
        # Formata nome
        nome_formatado = nome.capitalize()

        novo_id = f"p-{uuid.uuid4().hex[:3]}" # Gera id único aleatório.

        # Cria uma instância da nova planta
        nova_planta = Planta(
            id=novo_id,
            nome=nome_formatado,
            especie=especie,
            ambiente=ambiente,
            origem=origem,
            regar=regar,
            imagem=imagem
        )

        # Adiciona ao dicionario
        self.__plantas[novo_id] = nova_planta

        # Salva os dados atualizado no arquivo .json
        self._salvar_dados()

        return True
    
    # 5. Método para salvar os dados no arquivo .json
    def _salvar_dados(self):
        salvar_dados = {
            "plantas": self.get_plantas()
        }

        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(salvar_dados, f, indent=4)

