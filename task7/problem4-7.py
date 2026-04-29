class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Team:
    def __init__(self):
        self.members = []  

    def add_player(self, player_object):
        self.members.append(player_object)

pl1 = Player("Omar", 10)
pl2 = Player("Mona", 15)
team = Team()
team.add_player(pl1)
team.add_player(pl2)
for player in team.members:
    print(player.name, player.score)