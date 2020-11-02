class Game:
    def __init__(self):
        self.name = 'Pyopoly'
        self.players = []
        self.player_turn = 0

    def add_player(self, player):
        self.players.append(player)

    def pass_turn(self):
        if (self.player_turn == len(self.players)):
            self.player_turn = 0
        else:
            self.player_turn += 1
