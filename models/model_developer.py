#model_developer.py
import uuid

class Model_Developer():
    def __init__(self, nome: str, cargo: str, habilidades: list= []):
        self.id = uuid.uuid4().__str__().replace("-","")
        self.nome = nome
        self.cargo = cargo
        self.habilidades = habilidades

    def to_json(self):
        return dict(id = self.id, nome= self.nome, cargo= self.cargo, habilidades= [hab.descricao for hab in self.habilidades])