import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    # This initializes the Tic-Tac-Toe game with the given root window and subject
    def __init__(self, root, subject):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.moves_made = 0
        self.subject = subject
        self.create_grid()
        self.create_reset_button()

    # creates a 3x3 grid of buttons for my Toc-Tac-Toe component
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

    # creates a reset button which will reset the Tic-Tac-Toe game
    def create_reset_button(self):
        reset_button = tk.Button(
            self.root, text="Reset", font="Arial 12 bold", command=self.reset_game
        )
        reset_button.grid(row=3, column=0, columnspan=3)

    # Displays a question to the user when they click on an empty square
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

    # Allows the app to get a random question
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

    # Checks if the users answer is correct, if not it tells them the correct answer
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

    # Handles the button clicks and updates the game within reasonable time
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

    # Checks if the current player has won the game
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

    # Resets the game to its initial/origional state
    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = "X"
        self.moves_made = 0


# Gets the player names and starts the app (shows error message if the user doesn't enter name/s)
def get_started():
    player1 = player1_entry.get()
    player2 = player2_entry.get()
    if player1 and player2:
        open_new_window()
    else:
        messagebox.showwarning("Warning", "Please enter both player names.")


# Creates the gradient background in my app
def create_gradient(canvas, color1, color2):
    width = 300
    height = 250
    limit = height
    (r1, g1, b1) = root.winfo_rgb(color1)
    (r2, g2, b2) = root.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f"#{nr:04x}{ng:04x}{nb:04x}"
        canvas.create_line(0, i, 300, i, fill=color)


# Opens a window for my subject + game selection page
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Subject + Game Selection")
    new_window.geometry("300x250")

    new_canvas = tk.Canvas(new_window, width=300, height=250)
    new_canvas.pack(fill="both", expand=True)

    create_gradient(new_canvas, "white", "#FF6151")

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
        command=lambda: open_subject_window(new_window),
        bg="white",
        fg="#FF6151",
        font=("Arial", 12, "bold"),
    )
    new_canvas.create_window(150, 125, window=choose_subject_button)


# Opens a window for the user to select the subject
def open_subject_window(parent_window):
    subject_window = tk.Toplevel(parent_window)
    subject_window.title("Choose Subject")
    subject_window.geometry("200x150")

    math_button = tk.Button(
        subject_window,
        text="Math",
        command=lambda: select_subject(subject_window, "Math"),
        bg="white",
        fg="#FF6151",
        font=("Arial", 12, "bold"),
    )
    math_button.pack(pady=10)

    chemistry_button = tk.Button(
        subject_window,
        text="Chemistry",
        command=lambda: select_subject(subject_window, "Chemistry"),
        bg="white",
        fg="#FF6151",
        font=("Arial", 12, "bold"),
    )
    chemistry_button.pack(pady=10)

    general_knowledge_button = tk.Button(
        subject_window,
        text="General Knowledge",
        command=lambda: select_subject(subject_window, "General Knowledge"),
        bg="white",
        fg="#FF6151",
        font=("Arial", 12, "bold"),
    )
    general_knowledge_button.pack(pady=10)


# Select the subject and open the game window
def select_subject(subject_window, subject):
    subject_window.destroy()
    open_game_window(subject)


# Opens a window for the user to select the game
def open_game_window(subject):
    game_window = tk.Toplevel(root)
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
        command=lambda: select_game(game_window, subject, "Tic-Tac-Toe"),
        bg="white",
        fg="#FF6151",
        font=("Arial", 12, "bold"),
    )
    tic_tac_toe_button.pack(pady=5)

    connect_4_button = tk.Button(
        game_window,
        text="Connect-4",
        command=lambda: select_game(game_window, subject, "Connect-4"),
        bg="white",
        fg="#FF6151",
        font=("Arial", 12, "bold"),
    )
    connect_4_button.pack(pady=5)


# Select the game and open the corresponding window
def select_game(game_window, subject, game):
    game_window.destroy()
    if game == "Tic-Tac-Toe":
        open_tic_tac_toe_window(subject)


# Open the Tic-Tac-Toe game window
def open_tic_tac_toe_window(subject):
    tic_tac_toe_window = tk.Toplevel(root)
    TicTacToe(tic_tac_toe_window, subject)


root = tk.Tk()
root.title("Study Night")
root.geometry("300x250")

canvas = tk.Canvas(root, width=300, height=250)
canvas.pack(fill="both", expand=True)

create_gradient(canvas, "white", "#FF6151")

app_name_label = tk.Label(
    root, text="Study Night", bg="#FF6151", fg="white", font=("Arial", 18, "bold")
)
canvas.create_window(150, 40, window=app_name_label)

player1_label = tk.Label(
    root, text="Player 1:", bg="#FF6151", fg="white", font=("Arial", 12)
)
canvas.create_window(150, 80, window=player1_label)

player1_entry = tk.Entry(root, width=30)
canvas.create_window(150, 110, window=player1_entry)

player2_label = tk.Label(
    root, text="Player 2:", bg="#FF6151", fg="white", font=("Arial", 12)
)
canvas.create_window(150, 140, window=player2_label)

player2_entry = tk.Entry(root, width=30)
canvas.create_window(150, 170, window=player2_entry)

get_started_button = tk.Button(
    root,
    text="Get Started",
    command=get_started,
    bg="white",
    fg="#FF6151",
    font=("Arial", 12, "bold"),
)
canvas.create_window(150, 210, window=get_started_button)

root.mainloop()
