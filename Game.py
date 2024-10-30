import tkinter as tk
from tkinter import ttk
import random
import pygame
import json
import os

# pygame initialisieren
pygame.mixer.init()

# Globale Variablen
choices = ["Stein", "Papier", "Schere", "Echse", "Spock"]
profile_data = {}
player_score = 0
computer_score = 0
draw_count = 0

# JSON-Datei zur Speicherung der Spielerdaten
PROFILE_FILE = "spielerdaten.json"


# Bestehende Profile laden
def load_profile(name):
    global profile_data, player_score, computer_score, draw_count
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            profile_data = json.load(file)
        if name in profile_data:
            stats = profile_data[name]
            player_score = stats["wins"]
            computer_score = stats["losses"]
            draw_count = stats["draws"]
            result_label.config(text=f"Willkommen zurück, {name}!")
        else:
            profile_data[name] = {"wins": 0, "losses": 0, "draws": 0}
            result_label.config(text=f"Neues Profil für {name} erstellt.")
    else:
        profile_data = {name: {"wins": 0, "losses": 0, "draws": 0}}
        result_label.config(text=f"Neues Profil für {name} erstellt.")


# Profile speichern
def save_profile(name):
    profile_data[name] = {
        "wins": player_score,
        "losses": computer_score,
        "draws": draw_count
    }
    with open(PROFILE_FILE, "w") as file:
        json.dump(profile_data, file)


# Sound abspielen
def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


# Ergebnisberechnung und Animation
def play_game(player_choice):
    global player_score, computer_score, draw_count
    computer_choice = random.choice(choices)

    # Animation anzeigen
    animate_choice(player_choice, computer_choice)

    # Spielregeln
    if player_choice == computer_choice:
        result_label.config(text=f"Unentschieden! Beide wählten {player_choice}.")
        draw_count += 1
        play_sound("draw.mp3")
    elif (player_choice == "Stein" and computer_choice in ["Schere", "Echse"]) or \
            (player_choice == "Papier" and computer_choice in ["Stein", "Spock"]) or \
            (player_choice == "Schere" and computer_choice in ["Papier", "Echse"]) or \
            (player_choice == "Echse" and computer_choice in ["Spock", "Papier"]) or \
            (player_choice == "Spock" and computer_choice in ["Schere", "Stein"]):
        result_label.config(text=f"Du gewinnst! {player_choice} schlägt {computer_choice}.")
        player_score += 1
        play_sound("win.mp3")
    else:
        result_label.config(text=f"Computer gewinnt! {computer_choice} schlägt {player_choice}.")
        computer_score += 1
        play_sound("lose.mp3")

    # Punktestand aktualisieren
    score_label.config(text=f"Spieler: {player_score} | Computer: {computer_score} | Unentschieden: {draw_count}")


# Animation der Wahl
def animate_choice(player_choice, computer_choice):
    player_img = tk.PhotoImage(file=f"{player_choice.lower()}.png")
    computer_img = tk.PhotoImage(file=f"{computer_choice.lower()}.png")

    player_choice_label.config(image=player_img)
    computer_choice_label.config(image=computer_img)
    player_choice_label.image = player_img  # Speichern, um Garbage Collection zu verhindern
    computer_choice_label.image = computer_img


# Startbildschirm und Namenseingabe
def start_game():
    player_name = name_entry.get()
    if player_name:
        load_profile(player_name)
        game_frame.pack()
        start_frame.pack_forget()


# Bestenliste anzeigen
def show_best_players():
    best_scores = sorted(profile_data.items(), key=lambda x: x[1]["wins"], reverse=True)[:5]
    leaderboard = "\n".join([f"{name}: {data['wins']} Siege" for name, data in best_scores])
    leaderboard_label.config(text=leaderboard)


# GUI Initialisierung
root = tk.Tk()
root.title("Stein, Papier, Schere, Echse, Spock")
root.geometry("500x500")

# Startbildschirm
start_frame = tk.Frame(root)
tk.Label(start_frame, text="Bitte gib deinen Namen ein:", font=("Helvetica", 14)).pack(pady=10)
name_entry = tk.Entry(start_frame, font=("Helvetica", 12))
name_entry.pack()
tk.Button(start_frame, text="Spiel starten", command=start_game, font=("Helvetica", 12)).pack(pady=10)
tk.Button(start_frame, text="Bestenliste anzeigen", command=show_best_players, font=("Helvetica", 12)).pack(pady=5)
leaderboard_label = tk.Label(start_frame, text="", font=("Helvetica", 12))
leaderboard_label.pack()
start_frame.pack()

# Spielbereich
game_frame = tk.Frame(root)
result_label = tk.Label(game_frame, text="Wähle deine Option", font=("Helvetica", 14))
result_label.pack(pady=20)
score_label = tk.Label(game_frame, text="Spieler: 0 | Computer: 0 | Unentschieden: 0", font=("Helvetica", 12))
score_label.pack()

# Wahl-Anzeige (Animation)
player_choice_label = tk.Label(game_frame)
player_choice_label.pack(side="left", padx=20)
computer_choice_label = tk.Label(game_frame)
computer_choice_label.pack(side="right", padx=20)

# Buttons für die Wahl
button_frame = tk.Frame(game_frame)
button_frame.pack(pady=10)
for choice in choices:
    btn = tk.Button(button_frame, text=choice, width=10, command=lambda c=choice: play_game(c))
    btn.pack(side="left", padx=5)


# Fenster schließen und Profil speichern
def on_close():
    player_name = name_entry.get()
    if player_name:
        save_profile(player_name)
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
