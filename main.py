from market import Market
from queue_behaviour import QueueBehaviour
from market_behaviour import MarketBehaviour
from promotional_client import PromotionalClient

# Создание акционных клиентов
client1 = PromotionalClient(1, "Sale")
client2 = PromotionalClient(2, "Discount")
client3 = PromotionalClient(3, "Special Offer")

# Получение общего количества участников в акции
total_participants = PromotionalClient.get_promotion_participants()
print("Общее количество участников в акции:", total_participants)  # Выведет: Общее количество участников в акции: 3

# Пример использования
# market = Market()
market = Market("market_log.txt")
market.join_queue("Person1")
market.join_queue("Person2")
print(market.leave_queue())  # Выведет: Person1

market_behaviour = MarketBehaviour()
market_behaviour.place_order("Order1")
market_behaviour.place_order("Order2")
market_behaviour.process_orders()  # Выведет: Обработка заказа: Order1 \n Обработка заказа: Order2