from abc import abstractmethod, ABC


class AuthProcessorABC(ABC):

    @abstractmethod
    def process(self, response_details: dict, operator, operator_service):
        pass
