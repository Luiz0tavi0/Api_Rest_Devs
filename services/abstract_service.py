from abc import ABC, abstractmethod


class Abstract_Service(ABC):

    def __init__(self, bdlist):
        self.bdlist = bdlist

    def select(self, id: str = None):
        resp = [elem for elem in self.bdlist if elem.id == id]
        return resp[0].to_json() if resp else None

    def selectAll(self):
        return [{elem.id: elem.to_json()} for elem in self.bdlist]

    def delete(self, id: str = None):
        for indice in range(len(self.bdlist)):
            if self.bdlist[indice].id == id:
                self.bdlist.pop(indice)
                return True
        return False

    @abstractmethod
    def create(self, **kwargs): ...

    @abstractmethod
    def update(self, id: str = None, **kwargs): ...

