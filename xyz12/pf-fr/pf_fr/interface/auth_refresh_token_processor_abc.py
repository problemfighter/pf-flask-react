from abc import abstractmethod, ABC


class AuthRefreshTokenProcessorABC(ABC):

    @abstractmethod
    def process(self, response_map: dict, jwtPayload: dict, operator_service):
        pass
