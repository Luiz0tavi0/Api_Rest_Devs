from models.modeldeveloper import ModelDeveloper
from models.modelhabilidade import ModelHabilidade

hab1 = ModelHabilidade("Python")
hab2 = ModelHabilidade("Flask")
hab3 = ModelHabilidade("CSS")
hab4 = ModelHabilidade("HTML")
hab5 = ModelHabilidade("PostGree")
hab6 = ModelHabilidade(".Net Core")

lista_habilidades = [hab1, hab2, hab3, hab4, hab5, hab6]

lista_devs = [
    ModelDeveloper("Leandro", "Dev-FullStack"),
    ModelDeveloper("Marcela", "DBA-Oracle")
]
(lista_devs[0]).habilidades=[hab2, hab3, hab6]
(lista_devs[1]).habilidades=[hab1, hab3, hab5, hab4]


