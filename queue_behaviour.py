from collections import deque

class QueueBehaviour:
    def __init__(self):
        self.queue = deque()
    
    def join_queue(self, person):
        """
        Помещает человека в очередь.
        """
        self.queue.append(person)
    
    def leave_queue(self):
        """
        Удаляет человека из очереди (первого в очереди).
        """
        if self.queue:
            return self.queue.popleft()
        else:
            return None