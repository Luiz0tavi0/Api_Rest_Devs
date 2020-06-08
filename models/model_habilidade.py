# model_habilidade.py
import uuid
from . import model_developer


class Model_Habilidade():
    def __init__(self, descricao: str):
        self.id = uuid.uuid4().__str__().replace("-","")
        self.descricao = descricao

    def __eq__(self, other):
        return self.descricao.lower() == other.descricao.lower()

    def to_json(self):
        return dict(descricao = self.descricao)

    def __hash__(self):
        return hash(self.descricao.lower())

