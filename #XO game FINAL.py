from tkinter import *
import random

class PlayerNamesWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Player Names")
        self.parent.geometry("300x150")
        self.player1_name = StringVar()
        self.player2_name = StringVar()
        self.create_widgets()

    def create_widgets(self):
        # label and entry for player 1 name
        player1_label = Label(self.parent, text="Player 1 Name: ")
        player1_label.pack()
        player1_entry = Entry(self.parent, textvariable=self.player1_name)
        player1_entry.pack()

        # label and entry for player 2 name
        player2_label = Label(self.parent, text="Player 2 Name: ")
        player2_label.pack()
        player2_entry = Entry(self.parent, textvariable=self.player2_name)
        player2_entry.pack()

        # button to start the game
        start_button = Button(self.parent, text="Start Game", command=self.start_game)
        start_button.pack()

    def start_game(self):
        # close the player names window and start the game
        self.parent.destroy()
        game = TicTacToe(self.player1_name.get(), self.player2_name.get())
        game.show_game()


class TicTacToe:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.window = Tk()
        self.window.title("! Tic-Tac-Toe GAME !")
        self.window.geometry("550x650")
        self.player = ["❌", "⚪"]
        self.player_choice = random.choice(self.player)
        self.buttons = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.label1 = Label(text=self.player1_name + " Plays First \n" + self.player1_name + " vs " + self.player2_name, font=("Courier New", 30))
        self.label1.pack(padx=10, pady=10)
        self.reset_button = Button(text="RESTART", font=("Courier New", 15), command=self.new_game)
        self.reset_button.pack(padx=10, pady=10)
        self.frame = Frame(self.window)
        self.frame.pack()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = Button(self.frame, text="", font=("Courier New", 15), width=10, height=5, command=lambda row=r, column=c: self.next_turn(row, column))
                self.buttons[r][c].grid(row=r, column=c)

    def new_game(self):
        self.player_choice = random.choice(self.player)
        self.label1.config(text=self.player_choice + " Plays First \n" + self.player1_name + " vs " + self.player2_name)
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", bg="#F0F0F0")

    def check_winner(self):
        # checking the values of the rows
        for r in range(3):
            if self.buttons[r][0]["text"] == self.buttons[r][1]["text"] == self.buttons[r][2]["text"] != "":
                self.buttons[r][0].config(bg="LightBlue2")
                self.buttons[r][1].config(bg="LightBlue2")
                self.buttons[r][2].config(bg="LightBlue2")
                return True

        # checking the values of the columns
        for c in range(3):
            if self.buttons[0][c]["text"] == self.buttons[1][c]["text"] == self.buttons[2][c]["text"] != "":
                self.buttons[0][c].config(bg="LightBlue2")
                self.buttons[1][c].config(bg="LightBlue2")
                self.buttons[2][c].config(bg="LightBlue2")
                return True

        # checking the values of the main diagonal
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.buttons[0][0].config(bg="LightBlue2")
            self.buttons[1][1].config(bg="LightBlue2")
            self.buttons[2][2].config(bg="LightBlue2")
            return True

        # checking the values of the counter diagonal
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.buttons[0][2].config(bg="LightBlue2")
            self.buttons[1][1].config(bg="LightBlue2")
            self.buttons[2][0].config(bg="LightBlue2")
            return True

        return False

    def check_tie(self):
        for r in range(3):
            for c in range(3):
                if self.buttons[r][c]["text"] == "":
                    return False
        return True

    def next_turn(self, row, column):
        row = int(row)
        column = int(column)
        if self.buttons[row][column]["text"] == "":
            self.buttons[row][column].config(text=self.player_choice)
            if self.check_winner():
                winner = self.player1_name if self.player_choice == "❌" else self.player2_name
                self.label1.config(text=winner + " Wins !!!")
            elif self.check_tie():
                self.label1.config(text="It's a TIE !!!")
            else:
                self.player_choice = self.player[1] if self.player_choice == self.player[0] else self.player[0]
                self.label1.config(text=self.player_choice + "'s Turn")

    def show_game(self):
        self.window.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = PlayerNamesWindow(root)
    root.mainloop()