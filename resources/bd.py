from models.model_developer import Model_Developer
from models.model_habilidade import Model_Habilidade

hab1 = Model_Habilidade("Python")
hab2 = Model_Habilidade("Flask")
hab3 = Model_Habilidade("CSS")
hab4 = Model_Habilidade("HTML")
hab5 = Model_Habilidade("PostGree")

lista_habilidades = [hab1, hab2, hab3, hab4, hab5]

lista_devs = [
    Model_Developer("Leandro", "Dev-FullStack"),
    Model_Developer("Marcela", "DBA-Oracle")
]
(lista_devs[0]).habilidades.append(Model_Habilidade("Python"))
(lista_devs[1]).habilidades.append(Model_Habilidade(".Net Core"))


class TblHabilidades:

    def select(self, id=None):
        resp = [hab for hab in lista_habilidades if hab.id == id]
        return resp[0].to_json() if resp else None

    def selectAll(self):
        return [{hab.id: hab.to_json()} for hab in lista_habilidades]

    def delete(self, id: str = None):
        for hab in range(lista_habilidades.__len__()):
            if lista_habilidades[hab].id == id:
                lista_habilidades.pop(hab)
                return True
        return False

    def create(self, **habilidade):
        hab = Model_Habilidade(habilidade.get('descricao'))
        if not any(descr == hab.descricao for descr in [h.descricao for h in lista_habilidades]):
            lista_habilidades.append(hab)
            return hab.id
        return None

    def update(self, id=None, **habilidade):
        for hab in range(lista_habilidades.__len__()):
            if lista_habilidades[hab].id == id:
                lista_habilidades[hab].descricao = habilidade.get('descricao')
                return True
        return False




