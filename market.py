from collections import deque
from logger import Logger

class Market:
    def __init__(self, log_filename):
        self.queue = deque()
        self.orders = []
        self.logger = Logger(log_filename)
    
    def join_queue(self, person):
        """
        Помещает человека в очередь и записывает действие в лог.
        """
        self.queue.append(person)
        self.logger.log(f"{person} встал в очередь.")
    
    def leave_queue(self):
        """
        Удаляет человека из очереди и записывает действие в лог.
        """
        if self.queue:
            person = self.queue.popleft()
            self.logger.log(f"{person} покинул очередь.")
            return person
        else:
            return None
    
    def place_order(self, order):
        """
        Помещает заказ в список заказов и записывает действие в лог.
        """
        self.orders.append(order)
        self.logger.log(f"Поступил заказ: {order}")
    
    def process_orders(self):
        """
        Обрабатывает заказы и записывает действия в лог.
        """
        for order in self.orders:
            # Обработка заказа
            self.logger.log(f"Обработан заказ: {order}")
        self.orders = []  # Очищаем список заказов после обработки
    
    def return_items(self, items):
        """
        Возвращает товары и записывает действие в лог.
        """
        for item in items:
            self.logger.log(f"Возвращен товар: {item}")


# from collections import deque

# class Market:
#     def __init__(self):
#         self.queue = deque()
#         self.orders = []
    
#     def join_queue(self, person):
#         """
#         Помещает человека в очередь.
#         """
#         self.queue.append(person)
    
#     def leave_queue(self):
#         """
#         Удаляет человека из очереди (первого в очереди).
#         """
#         if self.queue:
#             return self.queue.popleft()
#         else:
#             return None
    
#     def place_order(self, order):
#         """
#         Помещает заказ в список заказов.
#         """
#         self.orders.append(order)
    
#     def process_orders(self):
#         """
#         Обрабатывает заказы.
#         """
#         for order in self.orders:
#             # Обработка заказа
#             print(f"Обработка заказа: {order}")
#         self.orders = []  # Очищаем список заказов после обработки
    
#     def update(self):
#         """
#         Обновляет состояние магазина.
#         """
#         self.process_orders()