from return_order_interface import iReturnOrder

class PromotionalClient(iReturnOrder):
    promotion_participants = 0  # Поле статическое для хранения общего количества участников в акции
    
    def __init__(self, client_id, action_name):
        self.client_id = client_id
        self.action_name = action_name
        PromotionalClient.promotion_participants += 1  # Увеличиваем количество участников в акции
    
    @classmethod
    def get_promotion_participants(cls):
        """
        Возвращает общее количество участников в акции.
        """
        return cls.promotion_participants
    
    def request_return(self, order_id):
        """
        Запрашивает возврат товара по указанному ID заказа.
        """
        print(f"Клиент {self.client_id} запрашивает возврат товара для заказа с ID {order_id}.")
    
    def process_return_request(self, order_id):
        """
        Обрабатывает запрос на возврат товара по указанному ID заказа.
        """
        print(f"Обработка запроса на возврат товара для заказа с ID {order_id}.")


# from return_order_interface import iReturnOrder

# class PromotionalClient(iReturnOrder):
#     promotion_participants = 0  # Поле статическое для хранения общего количества участников в акции
    
#     def __init__(self, client_id, action_name):
#         self.client_id = client_id
#         self.action_name = action_name
#         PromotionalClient.promotion_participants += 1  # Увеличиваем количество участников в акции
    
#     def request_return(self, order_id):
#         """
#         Запрашивает возврат товара по указанному ID заказа.
#         """
#         print(f"Клиент {self.client_id} запрашивает возврат товара для заказа с ID {order_id}.")
    
#     def process_return_request(self, order_id):
#         """
#         Обрабатывает запрос на возврат товара по указанному ID заказа.
#         """
#         print(f"Обработка запроса на возврат товара для заказа с ID {order_id}.")


# class PromotionalClient:
#     promotion_participants = 0  # Поле статическое для хранения общего количества участников в акции
    
#     def __init__(self, client_id, action_name):
#         self.client_id = client_id
#         self.action_name = action_name
#         PromotionalClient.promotion_participants += 1  # Увеличиваем количество участников в акции
    
#     @classmethod
#     def get_promotion_participants(cls):
#         """
#         Возвращает общее количество участников в акции.
#         """
#         return cls.promotion_participants
