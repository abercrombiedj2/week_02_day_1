class Team:

    def __init__(self, team_name, player_name, coach_name):
        self.name = team_name
        self.players = player_name
        self.coach = coach_name
        self.points = 0

    def add_player(self, player):
        self.players.append(player)
    
    def has_player(self, search_player):
        # for player in self.players:
        #     if player == search_player:
        #         return True
        # return False

        # if search_player in self.players:
        #     return True
        # else:
        #     return False

        return search_player in self.players
    
    def play_game(self, won):
        if won == True:
            self.points += 3
        else:
            pass
