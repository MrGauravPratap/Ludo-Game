import random

class LudoGame:
    def __init__(self):
        self.players = {'Red': 'R', 'Blue': 'B', 'Green': 'G', 'Yellow': 'Y'}
        self.positions = {player: 0 for player in self.players}
        self.winner = None

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, steps):
        self.positions[player] += steps
        if self.positions[player] > 100:
            self.positions[player] = 100 - (self.positions[player] - 100)

    def check_winner(self):
        for player, position in self.positions.items():
            if position == 100:
                self.winner = player
                return True
        return False

    def draw_board(self):
        print("+" + "-"*52 + "+")
        for row in range(11):
            line = "|"
            for col in range(11):
                if row == 0 or row == 10:
                    if col == 0 or col == 10:
                        line += " "
                    else:
                        line += "-"
                elif col == 0 or col == 10:
                    line += "|"
                else:
                    cell = " "
                    for player, pos in self.positions.items():
                        if (row-1)*10 + col == pos:
                            cell = self.players[player]
                    line += cell
            line += "|"
            print(line)
        print("+" + "-"*52 + "+")

    def play(self):
        while not self.check_winner():
            for player, symbol in self.players.items():
                input(f"{player}'s turn (press Enter to roll the dice)")
                steps = self.roll_dice()
                print(f"{player} rolled a {steps}")
                self.move_player(player, steps)
                print(f"{player} moved to position {self.positions[player]}")
                self.draw_board()
                if self.check_winner():
                    print(f"{self.winner} wins!")
                    return


if __name__ == "__main__":
    game = LudoGame()
    game.play()
