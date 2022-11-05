from CapitalStrategy import CapitalStrategy
from Loan import Loan


class CapitalStrategyRevolver(CapitalStrategy):
    def capital(self, loan: Loan):
        return super().capital()*self.unused_capital(loan)

    def unused_capital(self,  loan: Loan) -> float:
        return loan.get_unused_percentage()*self.duration()*self.risk_factor_for()

    def risk_factor_for(self, loan: Loan) -> float:
        return loan.unused_risk_amount()
