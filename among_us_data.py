from player_data import PlayerData

class AmongUsData(PlayerData):
    game = 'AmongUs'

    # IDs for Various Statistics
    IMPOSTOR_LOSS = 0
    IMPOSTOR_WIN = 1
    CREW_LOSS = 2
    CREW_WIN = 3

    # CHANGE MODES
    INCREASE = 1
    DECREASE = -1
    SET_AMOUNT = 0

    def __init__(self, id, crew_mate_wins=0, crew_mate_losses=0, impostor_wins=0, impostor_losses=0):
        PlayerData.__init__(self, id)
        self.crew_mate_wins = crew_mate_wins
        self.crew_mate_losses = crew_mate_losses
        self.impostor_wins = impostor_wins
        self.impostor_losses = impostor_losses

    def to_dict(self):
        player_dict = PlayerData.toDict(self)
        player_dict.update({
            'crew_mate_wins': self.crew_mate_wins,
            'crew_mate_losses': self.crew_mate_losses,
            'impostor_wins': self.impostor_wins,
            'impostor_losses': self.impostor_losses
        })
        return player_dict

    @classmethod
    def from_dict(cls, data, id=0):
        if data == None:
            return AmongUsData(id)
        return AmongUsData(data.get('id',id), data.get('crew_mate_wins',0), data.get('crew_mate_losses',0), data.get('impostor_wins',0), data.get('impostor_losses',0))

    def modify(self, statistic, change_mode, amount):
        delta_change = change_mode * amount
        if change_mode == AmongUsData.SET_AMOUNT:
            delta_change = amount
        if statistic == AmongUsData.CREW_WIN:
            self.crew_mate_wins += delta_change
        elif statistic == AmongUsData.CREW_LOSS:
            self.crew_mate_losses += delta_change
        elif statistic == AmongUsData.IMPOSTOR_LOSS:
            self.impostor_losses += delta_change
        elif statistic == AmongUsData.IMPOSTOR_WIN:
            self.impostor_wins += delta_change
