from Player import Player
from Die import Die


class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):

        print("=========================")
        print("🎲 Welcome to Roll the Dice!")
        print("=========================")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        # Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the values
        self.show_dice(player_value, computer_value)

        # Determine winner and loser
        if player_value > computer_value:
            print("You won the round!")
            self.update_counters(self._player, self._computer)
        elif computer_value > player_value:
            print("Computer won the round, Try again")
            self.update_counters(self._computer, self._player)
        else:
            print("It's Tie!")

        # Show counters
        self.show_counters()

    def print_round_welcome(self):
        print("------ New Round ------")
        input("Press any key to roll the dice.")

    def show_dice(self, player_value, computer_value):
        print("Your die {0}".format(player_value))
        print("Computer die {0}".format(computer_value))

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print("Your counter {0}".format(self._player.counter))
        print("Computer counter {0}".format(self._computer.counter))

    def check_game_over(self):
        if self._player.counter == 0:  # game over the player won
            self.show_game_over(self._player)
            return True

        elif self._computer.counter == 0:  # game over the computer won
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n=======================")
            print(" G A M E   O V E R ✨")
            print("=======================")
            print("The computer won the game. Sorry...")
            print("=================================")
        else:
            print("\n=====================")
            print(" G A M E   O V E R ✨")
            print("=====================")
            print("You won the game! Congratulations")
            print("=================================")



def main():
    player_die = Die()
    computer_die = Die()

    my_player = Player(player_die, is_computer=False)
    computer_player = Player(computer_die, is_computer=True)

    game = DiceGame(my_player, computer_player)
    game.play()


if __name__ == '__main__':
    main()
