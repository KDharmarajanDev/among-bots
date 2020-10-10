class PlayerData:
    game = 'None'
    def __init__(self, id):
        self.id = id

    def toDict(self):
        return {'id': self.id}