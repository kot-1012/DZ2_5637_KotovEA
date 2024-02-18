from abc import ABC, abstractmethod

class iReturnOrder(ABC):
    @abstractmethod
    def request_return(self, order_id):
        """
        Запрашивает возврат товара по указанному ID заказа.
        """
        pass
    
    @abstractmethod
    def process_return_request(self, order_id):
        """
        Обрабатывает запрос на возврат товара по указанному ID заказа.
        """
        pass
