import tkinter as tk
from tkinter import messagebox
import random
import re

class TicTacToe:
    # This function initializes the Tic-Tac-Toe game with the main window and the selected subject
    def __init__(self, root, subject):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.moves_made = 0
        self.subject = subject
        self.create_grid()
        self.create_control_buttons()

    # This function creates the grid of buttons for the Tic-Tac-Toe board.
    def create_grid(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font="Arial 20 bold",
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.ask_question(r, c),
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    # This function creates the control buttons (Reset and Home) below the Tic-Tac-Toe board
    def create_control_buttons(self):
        control_frame = tk.Frame(self.root)
        control_frame.grid(row=3, column=0, columnspan=3)

        reset_button = tk.Button(
            control_frame, text="Reset", font="Arial 12 bold", command=self.reset_game
        )
        reset_button.pack(side=tk.LEFT, padx=10)

        home_button = tk.Button(
            control_frame, text="Home", font="Arial 12 bold", command=self.go_home
        )
        home_button.pack(side=tk.LEFT, padx=10)

    # This function asks a question when a player clicks on a Tic-Tac-Toe cell.
    def ask_question(self, row, col):
        question, answer = self.get_random_question()
        self.question_window = tk.Toplevel(self.root)
        self.question_window.title("Answer the Question")

        question_label = tk.Label(
            self.question_window, text=question, font="Arial 12 bold"
        )
        question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.question_window, font="Arial 12")
        self.answer_entry.pack(pady=10)

        submit_button = tk.Button(
            self.question_window,
            text="Submit",
            font="Arial 12 bold",
            command=lambda: self.check_answer(row, col, answer),
        )
        submit_button.pack(pady=10)

    # This function gets a random question and answer pair based on the selected subject
    def get_random_question(self):
        questions = {
            "Math": [
                ("What is the equation for a linear graph?", "y=mx+c"),
                ("What is 2x + 3x?", "5x"),
                ("What is 2 + 2?", "4"),
                ("What is 5 * 6?", "30"),
            ],
            "Chemistry": [
                ("What is the symbol for Gold?", "Au"),
                ("How many elements are in the periodic table?", "118"),
                ("What is the atomic number for carbon?", "6"),
                ("How many states of matter are there?", "4"),
            ],
            "General Knowledge": [
                ("How many continents are there?", "7"),
                ("What is the eleventh month of the year?", "November"),
                ("What is the color of aircraft black boxes?", "orange"),
                ("What is the colour of the sky?", "blue"),
                ("How many months are there in a year?", "12"),
            ],
        }
        return random.choice(questions[self.subject])

    # This function checks the player's answer and proceed accordingly.
    def check_answer(self, row, col, correct_answer):
        player_answer = self.answer_entry.get()
        self.question_window.destroy()
        if player_answer.lower() == correct_answer.lower():
            self.on_button_click(row, col)
        else:
            messagebox.showinfo(
                "Wrong Answer", f"Incorrect! The correct answer is: {correct_answer}"
            )
            self.ask_question(row, col)

    # Handle a player's move by marking the button and checking for a winner or draw.
    def on_button_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.current_player:
            self.buttons[row][col]["text"] = self.current_player
            self.moves_made += 1
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.current_player = None
            elif self.moves_made == 9:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.current_player = None
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    # Checks if the current player has won the game.
    def check_winner(self, row, col):
        if all(self.buttons[row][i]["text"] == self.current_player for i in range(3)):
            return True
        if all(self.buttons[i][col]["text"] == self.current_player for i in range(3)):
            return True
        if row == col and all(
            self.buttons[i][i]["text"] == self.current_player for i in range(3)
        ):
            return True
        if row + col == 2 and all(
            self.buttons[i][2 - i]["text"] == self.current_player for i in range(3)
        ):
            return True
        return False

    # Resets the game to its initial state.
    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = "X"
        self.moves_made = 0

    # Closes the Tic-Tac-Toe window and go back to the main window.
    def go_home(self):
        self.root.destroy()
        MainWindow().create_main_window()

class MainWindow:
    # Initializes the main window for the application.
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Study Night")
        self.root.geometry("300x250")
        self.create_widgets()
        self.root.mainloop()

    # Create widgets for the main window, including player name entry and buttons.
    def create_widgets(self):
        canvas = tk.Canvas(self.root, width=300, height=250)
        canvas.pack(fill="both", expand=True)
        self.create_gradient(canvas, "white", "#FF6151")

        app_name_label = tk.Label(
            self.root, text="Study Night", bg="#FF6151", fg="white", font=("Arial", 18, "bold")
        )
        canvas.create_window(150, 40, window=app_name_label)

        player1_label = tk.Label(
            self.root, text="Player 1:", bg="#FF6151", fg="white", font=("Arial", 12)
        )
        canvas.create_window(150, 80, window=player1_label)

        self.player1_entry = tk.Entry(self.root, width=30)
        canvas.create_window(150, 110, window=self.player1_entry)

        player2_label = tk.Label(
            self.root, text="Player 2:", bg="#FF6151", fg="white", font=("Arial", 12)
        )
        canvas.create_window(150, 140, window=player2_label)

        self.player2_entry = tk.Entry(self.root, width=30)
        canvas.create_window(150, 170, window=self.player2_entry)

        get_started_button = tk.Button(
            self.root,
            text="Get Started",
            command=self.get_started,
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        canvas.create_window(150, 210, window=get_started_button)

    # This function creates a gradient background for the canvas.
    def create_gradient(self, canvas, color1, color2):
        width = 300
        height = 250
        limit = height
        (r1, g1, b1) = self.root.winfo_rgb(color1)
        (r2, g2, b2) = self.root.winfo_rgb(color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f"#{nr:04x}{ng:04x}{nb:04x}"
            canvas.create_line(0, i, 300, i, fill=color)

    # Starts the game after player names have been validated.
    def get_started(self):
        player1 = self.player1_entry.get()
        player2 = self.player2_entry.get()

        if not self.validate_player_name(player1) or not self.validate_player_name(player2):
            return

        if player1 and player2:
            self.open_new_window()
        else:
            messagebox.showwarning("Warning", "Please enter both player names.")

    # Validate the entered player name for length and disallowed characters.
    def validate_player_name(self, name):
        if len(name) > 15:
            messagebox.showerror("Error", "Users have a maximum limit of 15 characters")
            return False
        if re.search(r'[!@#$%^&*()]', name):
            messagebox.showerror("Error", "No symbols are allowed.")
            return False
        return True

    # This function opens a new window to select the subject and game.
    def open_new_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Subject + Game Selection")
        new_window.geometry("300x250")

        new_canvas = tk.Canvas(new_window, width=300, height=250)
        new_canvas.pack(fill="both", expand=True)

        self.create_gradient(new_canvas, "white", "#FF6151")

        home_button = tk.Button(
            new_window,
            text="Home",
            command=new_window.destroy,
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        new_canvas.create_window(30, 20, window=home_button)

        choose_subject_button = tk.Button(
            new_window,
            text="Choose Subject",
            command=lambda: self.open_subject_window(new_window),
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        new_canvas.create_window(150, 125, window=choose_subject_button)

    # Open a window to choose the subject for the game.
    def open_subject_window(self, parent_window):
        subject_window = tk.Toplevel(parent_window)
        subject_window.title("Choose Subject")
        subject_window.geometry("200x150")

        math_button = tk.Button(
            subject_window,
            text="Math",
            command=lambda: self.select_subject(subject_window, "Math"),
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        math_button.pack(pady=10)

        chemistry_button = tk.Button(
            subject_window,
            text="Chemistry",
            command=lambda: self.select_subject(subject_window, "Chemistry"),
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        chemistry_button.pack(pady=10)

        general_knowledge_button = tk.Button(
            subject_window,
            text="General Knowledge",
            command=lambda: self.select_subject(subject_window, "General Knowledge"),
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        general_knowledge_button.pack(pady=10)

    # Selects the subject and open the game selection window.
    def select_subject(self, subject_window, subject):
        subject_window.destroy()
        self.open_game_window(subject)

    # This function opens a window to choose the game.
    def open_game_window(self, subject):
        game_window = tk.Toplevel(self.root)
        game_window.title("Choose Game")
        game_window.geometry("200x150")

        label = tk.Label(
            game_window,
            text=f"Subject: {subject}\nChoose Game",
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        label.pack(pady=10)

        tic_tac_toe_button = tk.Button(
            game_window,
            text="Tic-Tac-Toe",
            command=lambda: self.select_game(game_window, subject, "Tic-Tac-Toe"),
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        tic_tac_toe_button.pack(pady=5)

        connect_4_button = tk.Button(
            game_window,
            text="Connect-4",
            command=lambda: self.select_game(game_window, subject, "Connect-4"),
            bg="white",
            fg="#FF6151",
            font=("Arial", 12, "bold"),
        )
        connect_4_button.pack(pady=5)

    # Selects the game and open the corresponding game window.
    def select_game(self, game_window, subject, game):
        game_window.destroy()
        if game == "Tic-Tac-Toe":
            self.open_tic_tac_toe_window(subject)

    # Opens the Tic-Tac-Toe game window with the selected subject.
    def open_tic_tac_toe_window(self, subject):
        tic_tac_toe_window = tk.Toplevel(self.root)
        TicTacToe(tic_tac_toe_window, subject)

if __name__ == "__main__":
    MainWindow()
