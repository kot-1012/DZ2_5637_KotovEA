class MarketBehaviour:
    def __init__(self):
        self.orders = []
    
    def place_order(self, order):
        """
        Помещает заказ в список заказов.
        """
        self.orders.append(order)
    
    def process_orders(self):
        """
        Обрабатывает заказы.
        """
        for order in self.orders:
            # Обработка заказа
            print(f"Обработка заказа: {order}")
        self.orders = []  # Очищаем список заказов после обработки