import os

class Logger:
    def __init__(self, filename):
        logs_dir = 'logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        self.filepath = os.path.join(logs_dir, filename)
    
    def log(self, message):
        with open(self.filepath, 'a') as file:
            file.write(message + '\n')


# class Logger:
#     def __init__(self, filename):
#         self.filename = filename
    
#     def log(self, message):
#         with open(self.filename, 'a') as file:
#             file.write(message + '\n')
