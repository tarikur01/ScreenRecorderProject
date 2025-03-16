class OrderExecution:
    def __init__(self, broker):
        self.broker = broker

    def execute_order(self, order_type, symbol, quantity):
        """Execute a trade order."""
        print(f"Executing {order_type} order for {quantity} units of {symbol} on {self.broker}.")