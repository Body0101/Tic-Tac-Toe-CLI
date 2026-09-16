from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from pyfiglet import figlet_format


console = Console()

symbols = {"X": False, "O": False}
names = []


# cook your dish here
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def enter_name(self, number):
        while True:
            rprint(
                f"[bold red on white]player {number}, Enter your nick name: ", sep=" "
            )
            name = input()
            if not name.isalpha():
                rprint(
                    f"[italic blue on white]Invalid Name, please enter letters only :)"
                )
            elif name.upper() in names:
                rprint(
                    f"[italic blue on white]Invalid Name, please Enter another name:)"
                )
            else:
                self.name = name
                names.append(name.upper())
                break

    def enter_Symbol(self):
        while True:
            try:
                rprint(
                    f"[bold red on white]{self.name}, Enter your Symbol ( X or O ): ",
                    sep=" ",
                )
                npt = input().upper()
                if not npt.isalpha():
                    rprint(f"[italic blue on white]Invalid Symbol, Enter letters :)")
                elif symbols[npt] == True:
                    rprint(f"[italic blue on white]This symbol is token, try again :) ")
                else:
                    self.symbol = npt
                    symbols[npt] = True
                    break
            except KeyError:
                rprint(f"[italic blue on white]Invalid Symbol, try another symbol :)")


class Menu:
    def start_menu(self):
        print("*" * len("* Welcome you! I am Tic Tak Toe, play With your friend *"))
        print("* Welcome you! I am Tic Tak Toe, play With your friend *")
        print("*" * len("* Welcome you! I am Tic Tak Toe, play With your friend *"))
        while True:
            rprint("[bold red on white]Choose( 1 or 2 )")
            rprint("1. Start session game")
            rprint("2. Quit game")
            try:
                response = int(input(">>> "))
                if 1 <= response <= 2:
                    break
                else:
                    rprint(
                        "[italic blue on white]Invalid value, Enter (1, 2), try again!"
                    )
            except ValueError:
                rprint("[italic blue on white]Invalid value, Enter (1, 2), try again!")
        return response

    def win_menu(self, name):
        winner = figlet_format(text=f"{name} is Winner 🎖️", font="slant")
        rprint(f"[bold red on white]{winner}")

    def end_menu(self):
        print("*" * len("* End Game *"))
        print("* End Game *")
        print("*" * len("* End Game *"))
        while True:
            rprint("[bold red on white]Choose( 1 or 2 )")
            rprint("1. New Game")
            rprint("2. Quit game")
            try:
                response = int(input(">>> "))
                if 1 <= response <= 2:
                    break
                else:
                    rprint(
                        "[italic blue on white]Invalid value, Enter (1, 2), try again!"
                    )
            except ValueError:
                rprint("[italic blue on white]Invalid value, Enter (1, 2), try again!")
        return response


class Board:
    def __init__(self):
        self.positions = [str(num) for num in range(1, 10)]

    def display_board(self):

        table = Table(
            show_header=False,
            show_edge=False,
            box=None,
            padding=(0, 3),
        )

        for row in range(3):
            cells = []

            for col in range(3):
                value = self.positions[row * 3 + col]

                if value == "X":
                    cells.append("[bold red]X[/bold red]")
                elif value == "O":
                    cells.append("[bold blue]O[/bold blue]")
                else:
                    cells.append(f"[dim white]{value}[/dim white]")

            table.add_row(
                f"{cells[0]} [bold white]│[/bold white] "
                f"{cells[1]} [bold white]│[/bold white] "
                f"{cells[2]}"
            )

            if row < 2:
                table.add_row("[dim]──┼───┼────[/dim]")

        panel = Panel(
            Align.center(table),
            title="[bold cyan]TIC TAC TOE[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )

        console.print(panel)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.positions[choice - 1] = symbol
            return True
        return False

    def reset_board(self):
        self.positions = [str(num) for num in range(1, 10)]

    def is_valid_move(self, choice):
        return self.positions[choice - 1].isdigit()


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player = False

    def start_play(self):
        choice = self.menu.start_menu()
        if choice == 1:
            self.play_game()
        else:
            self.quit_game()

    def play_game(self):
        self.enter_players()
        self.session_game()

    def enter_players(self):
        for number, player in enumerate(self.players, start=1):
            player.enter_name(number)
            player.enter_Symbol()

    def session_game(self):
        while True:
            self.display_board()
            self.update_board()
            if self.check_win() or self.check_draw():
                if self.end_game() == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def quit_game(self):
        print("Thank  you for playing!")

    def display_board(self):
        self.board.display_board()

    def update_board(self):
        try:
            while True:
                rprint(
                    f"{self.players[self.current_player].name}, Enter position choice ({self.players[self.current_player].symbol})"
                )
                choice = int(input(">>> "))
                if self.board.update_board(
                    symbol=self.players[self.current_player].symbol, choice=choice
                ):
                    self.current_player = 1 - self.current_player
                    break
                else:
                    rprint("[italic blue on white]Please Enter another position :)")
        except ValueError:
            rprint(
                "[italic blue on white]Invalid value input, choose between 1 and 9 :)"
            )

    def check_win(self):
        ls = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for indeces in ls:
            if (
                self.board.positions[indeces[0]]
                == self.board.positions[indeces[1]]
                == self.board.positions[indeces[2]]
            ):
                if self.players[0].symbol == self.board.positions[indeces[0]]:
                    self.menu.win_menu(self.players[0].name)
                else:
                    self.menu.win_menu(self.players[1].name)
                return True
        return False

    def check_draw(self):
        for pos in self.board.positions:
            if pos.isdigit():
                return False
        rprint("[bold red on white]Game Over!")
        return True

    def restart_game(self):
        self.board.reset_board()
        names.clear()
        symbols = {"X": False, "O": False}
        self.session_game()

    def end_game(self):
        return self.menu.end_menu()


game = Game()
game.start_play()
