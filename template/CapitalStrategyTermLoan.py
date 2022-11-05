from CapitalStrategy import CapitalStrategy
from Loan import Loan


class CapitalStrategyTermLoan(CapitalStrategy):
    def risk_ammount(self, loan: Loan) -> float:
        return loan.get_commitment()
