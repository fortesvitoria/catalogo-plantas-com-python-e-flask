import json 
from models.cls_plantas import Planta

class CatalogoPlantas:
    def __init__(self, arquivo_dados="data/dados_plantas.json"):
        self.__plantas = {}
        self.carregar_dados(arquivo_dados)
    
    def carregar_dados(self, arquivo_dados):
        try:
            with open(arquivo_dados, 'r', encoding='utf-8') as f: dados = json.load(f)
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
                self.__plantas[item.get("id")] = planta
        
        except FileNotFoundError:
            print(f"Erro: O arquivo {arquivo_dados} não foi encontrado.")
        except json.JSONDecodeError:
            print(f"Erro: O arquivo {arquivo_dados} não é um JSON válido.")
    
    def get_plantas(self):
        return [planta.to_dict() for planta in self.__plantas.values()]