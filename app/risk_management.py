class RiskManagement:
    def __init__(self, balance, risk_per_trade=0.02):
        self.balance = balance
        self.risk_per_trade = risk_per_trade

    def calculate_position_size(self, stop_loss):
        """Calculate position size based on risk management."""
        risk_amount = self.balance * self.risk_per_trade
        position_size = risk_amount / stop_loss
        return position_size