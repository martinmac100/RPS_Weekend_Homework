class Rps:

    def play_game(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        player = (player1, player2)

        while player1 == False:
        
            player = input("Rock, Paper, Scissors?")
            if player1 == player2:
                print("Tie!")
            elif player1 == "Rock":
                if player2 == "Paper":
                    print("You lose!", player2, "covers", player1)
                else:
                    print("You win!", player1, "smashes", player2)
            elif player1 == "Paper":
                if player2 == "Scissors":
                    print("You lose!", player2, "cut", player1)
                else:
                    print("You win!", player1, "covers", player2)
            elif player1 == "Scissors":
                if player2 == "Rock":
                    print("You lose...", player2, "smashes", player1)
                else:
                    print("You win!", player1, "cut", player2)
            else:
                print("That's not a valid play. Check your spelling!")
 
            player1 = False
          

