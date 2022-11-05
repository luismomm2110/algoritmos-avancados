from CapitalStrategy import CapitalStrategy
from Loan import Loan


class CapitalStrategyAdvisedLoan(CapitalStrategy):
    def duration(self, loan: Loan) -> float:
        return 10*loan

    def risk_ammount(self, loan: Loan) -> float:
        loan.get_unused_percentage() * loan.get_commitment()
