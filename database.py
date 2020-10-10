import os
from pymongo import MongoClient

class ConnectionManager:

    def __init__(self):
        self.database = MongoClient(os.environ.get('DATABASE_CONNECTION_URI'))['AmongBots']
    
    def get_stats(self, user_id):
        return self.database.find_one({'user_id': user_id})

    def set_stats(self, send_object):
        self.database.insert(send_object)