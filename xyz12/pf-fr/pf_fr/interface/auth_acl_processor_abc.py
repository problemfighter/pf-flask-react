from abc import abstractmethod, ABC


class AuthACLProcessorABC(ABC):

    @abstractmethod
    def process(self, url_info: dict, jwtPayload: dict, authInterceptor):
        pass
