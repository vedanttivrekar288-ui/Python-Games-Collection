import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x580")
root.configure(bg="#17202A")

player = "X"
buttons = []

def check_winner():
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinations:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            for i in (a, b, c):
                buttons[i].config(bg="green")

            messagebox.showinfo("Winner", f"Player {player} wins!")
            reset_game()
            return True

    if all(b["text"] != "" for b in buttons):
        messagebox.showinfo("Result", "Match Draw!")
        reset_game()
        return True

    return False

def play(index):
    global player

    if buttons[index]["text"] == "":
        buttons[index].config(
            text=player,
            fg="#3498DB" if player == "X" else "#E74C3C"
        )

        if not check_winner():
            player = "O" if player == "X" else "X"
            status.config(text=f"Player {player}'s Turn")

def reset_game():
    global player
    player = "X"

    for button in buttons:
        button.config(text="", bg="#ECF0F1")

    status.config(text="Player X's Turn")

title = tk.Label(
    root,
    text="TIC-TAC-TOE",
    font=("Arial", 24, "bold"),
    bg="#17202A",
    fg="white"
)
title.pack(pady=15)

status = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 15),
    bg="#17202A",
    fg="white"
)
status.pack()

frame = tk.Frame(root, bg="#17202A")
frame.pack(pady=20)

for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 30, "bold"),
        width=4,
        height=2,
        bg="#ECF0F1",
        command=lambda i=i: play(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    buttons.append(button)

tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14),
    bg="#3498DB",
    fg="white",
    command=reset_game
).pack(pady=10)

root.mainloop()
