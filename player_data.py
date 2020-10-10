class PlayerData:
    game = 'None'
    def __init__(self, id):
        self.id = id

    def to_dict(self):
        return {'id': self.id}

    @classmethod
    def from_dict(cls, data):
        return PlayerData(data.get('id',0))