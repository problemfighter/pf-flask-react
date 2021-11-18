from abc import abstractmethod, ABC


class AuthProcessorABC(ABC):

    @abstractmethod
    def process(self, request, token: str) -> bool:
        pass
