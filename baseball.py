import sys
import re

class Player:
    def __init__(self, name):
        self.name = name
        self.at_bats = 0
        self.hits = 0

    def add_performance(self, at_bats, hits):
        self.at_bats += at_bats
        self.hits += hits

    def batting_average(self):
        return self.hits / self.at_bats if self.at_bats > 0 else 0
    
def read_file(file_path):
    players = {}
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r' (.+) batted (\d+) times with (\d+) hits and \d+ runs', line)
            if match:
                name, at_bats, hits = match.groups()
                if name not in players:
                    players[name] = Player(name)
                players[name].add_performance(int(at_bats), int(hits))
    return players
    
def main():
    if len(sys.argv) != 2:
        print('Usage: baseball.py <file_path>')
        sys.exit(1)

    file_path = sys.argv[1]
    players = read_file(file_path)
    sorted_players = sorted(players.values(), key=lambda player: player.batting_average(), reverse=True)

    for player in sorted_players:
        print(f'{player.name}: {player.batting_average():.3f}')

if __name__ == '__main__':
    main()
