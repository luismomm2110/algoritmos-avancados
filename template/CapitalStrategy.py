from abc import ABC, abstractmethod
from Loan import Loan


class CapitalStrategy(ABC):

    def capital(self, loan: Loan) -> float:
        return self.risk_factor_for(loan) * self.duration(loan) * self.risk_ammount(self)

    @abstractmethod
    def duration(self, loan: Loan) -> float:
        pass

    def risk_factor_for(self, loan: Loan) -> float:
        pass

    def risk_ammount(self, loan: Loan) -> float:
        pass
