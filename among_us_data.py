from player_data import PlayerData

class AmongUsData(PlayerData):
    game = 'AmongUs'
    def __init__(self, id, crew_mate_wins=0, crew_mate_losses=0, impostor_wins=0, impostor_losses=0):
        PlayerData.__init__(self, id)
        self.crew_mate_wins = crew_mate_wins
        self.crew_mate_losses = crew_mate_losses
        self.impostor_wins = impostor_wins
        self.impostor_losses = impostor_losses

    def toDict(self):
        player_dict = PlayerData.toDict(self)
        player_dict.update({
            'crew_mate_wins': self.crew_mate_wins,
            'crew_mate_losses': self.crew_mate_losses,
            'impostor_wins': self.impostor_wins,
            'impostor_losses': self.impostor_losses
        })
        return player_dict