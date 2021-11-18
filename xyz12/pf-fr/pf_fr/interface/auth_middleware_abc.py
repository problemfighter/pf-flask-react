from abc import abstractmethod, ABC


class AuthMiddlewareABC(ABC):

    @abstractmethod
    def validate(self, request, token: str):
        pass
