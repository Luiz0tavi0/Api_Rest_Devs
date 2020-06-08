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
