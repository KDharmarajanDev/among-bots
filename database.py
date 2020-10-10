import os
from pymongo import MongoClient

class ConnectionManager:

    def __init__(self):
        self.database = MongoClient(os.environ.get('DATABASE_CONNECTION_URI')).GameStats

    def update_stats_user(self, game, player_data, send_object):
        self.database[game].update(player_data.to_dict(),send_object.to_dict(),upsert=True)
    
    def get_data(self, game, player_data):
        return self.database[game].find_one(player_data.to_dict())
