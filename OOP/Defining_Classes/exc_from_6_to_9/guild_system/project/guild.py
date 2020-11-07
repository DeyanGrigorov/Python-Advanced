from exc_from_6_to_9.guild_system.project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.player_list = []

    def assign_player(self, player):
        if player in self.player_list:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.player_list.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        players_names = [p for p in self.player_list if p.name == player_name]
        if players_names:
            self.player_list.remove(players_names[0])
            player = players_names[0]
            player.guild = self.name
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}" + '\n'
        player_info = [f'{p.player_info()}' for p in self.player_list]
        return result + ''.join(l for l in player_info)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())