from abc import ABC, abstractmethod

class AbstractRepository(ABC):

    @abstractmethod
    def create(self, employee):
        pass

    
    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
       
    @abstractmethod
    def get_all(self):
        pass