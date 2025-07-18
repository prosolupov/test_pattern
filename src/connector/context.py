from abc import ABC, abstractmethod

class Context(ABC):
    @abstractmethod
    def get_session(self):...

    @abstractmethod
    def close_session(self):...