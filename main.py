import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def get_started():
    player1 = player1_entry.get()
    player2 = player2_entry.get()
    if player1 and player2:
        open_new_window()
    else:
        messagebox.showwarning("Warning", "Please enter both player names.")

# Function to create a gradient background
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
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, 300, i, fill=color)

# Function to open a new window with the same gradient background
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Page")
    new_window.geometry("300x250")

    new_canvas = tk.Canvas(new_window, width=300, height=250)
    new_canvas.pack(fill="both", expand=True)

    create_gradient(new_canvas, "white", "#FF6151")

    home_button = tk.Button(new_window, text="Home", command=new_window.destroy, bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    new_canvas.create_window(30, 20, window=home_button)

    choose_subject_button = tk.Button(new_window, text="Choose Subject", command=lambda: open_subject_window(new_window), bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    new_canvas.create_window(150, 125, window=choose_subject_button)

# Function to open the subject selection window
def open_subject_window(parent_window):
    subject_window = tk.Toplevel(parent_window)
    subject_window.title("Choose Subject")
    subject_window.geometry("200x150")

    math_button = tk.Button(subject_window, text="Math", command=lambda: select_subject(subject_window, "Math"), bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    math_button.pack(pady=10)

    chemistry_button = tk.Button(subject_window, text="Chemistry", command=lambda: select_subject(subject_window, "Chemistry"), bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    chemistry_button.pack(pady=10)

    cms_button = tk.Button(subject_window, text="CMS", command=lambda: select_subject(subject_window, "CMS"), bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    cms_button.pack(pady=10)

# Function to handle subject selection
def select_subject(subject_window, subject):
    subject_window.destroy()
    open_game_window(subject)

# Function to open the game selection window
def open_game_window(subject):
    game_window = tk.Toplevel(root)
    game_window.title("Choose Game")
    game_window.geometry("200x150")

    label = tk.Label(game_window, text=f"Subject: {subject}\nChoose Game", bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    label.pack(pady=10)

    tic_tac_toe_button = tk.Button(game_window, text="Tic-Tac-Toe", command=lambda: select_game(game_window, "Tic-Tac-Toe"), bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    tic_tac_toe_button.pack(pady=5)

    connect_4_button = tk.Button(game_window, text="Connect-4", command=lambda: select_game(game_window, "Connect-4"), bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
    connect_4_button.pack(pady=5)

# Function to handle game selection
def select_game(game_window, game):
    messagebox.showinfo("Game Selected", f"You have chosen {game}.")
    game_window.destroy()

# Create the main application window
root = tk.Tk()
root.title("Study Night")
root.geometry("300x250")

# Create a Canvas widget for the gradient background
canvas = tk.Canvas(root, width=300, height=250)
canvas.pack(fill="both", expand=True)

# Create the gradient background
create_gradient(canvas, "white", "#FF6151")

# Create and place the app name label
app_name_label = tk.Label(root, text="Study Night", bg="#FF6151", fg="white", font=("Arial", 18, "bold"))
app_name_label_window = canvas.create_window(150, 40, window=app_name_label)

# Create and place labels and entry fields for players
player1_label = tk.Label(root, text="Player 1:", bg="#FF6151", fg="white", font=("Arial", 12))
player1_label_window = canvas.create_window(150, 80, window=player1_label)

player1_entry = tk.Entry(root, width=30)
player1_entry_window = canvas.create_window(150, 110, window=player1_entry)

player2_label = tk.Label(root, text="Player 2:", bg="#FF6151", fg="white", font=("Arial", 12))
player2_label_window = canvas.create_window(150, 140, window=player2_label)

player2_entry = tk.Entry(root, width=30)
player2_entry_window = canvas.create_window(150, 170, window=player2_entry)

# Create and place the "Get Started" button
get_started_button = tk.Button(root, text="Get Started", command=get_started, bg="white", fg="#FF6151", font=("Arial", 12, "bold"))
get_started_button_window = canvas.create_window(150, 210, window=get_started_button)

# Run the application
root.mainloop()
