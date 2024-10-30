import random

# Möglichkeiten
choices = ["Stein", "Papier", "Schere"]

# Eingabe des Spielers
player_choice = input("Wähle Stein, Papier oder Schere: ").capitalize()

# Auswahl des Computers
computer_choice = random.choice(choices)
print(f"Computer hat {computer_choice} gewählt.")

# Überprüfen der Ergebnisse
if player_choice == computer_choice:
    print("Unentschieden!")
elif (player_choice == "Stein" and computer_choice == "Schere") or \
     (player_choice == "Papier" and computer_choice == "Stein") or \
     (player_choice == "Schere" and computer_choice == "Papier"):
    print("Du gewinnst!")
else:
    print("Du verlierst!")
import random

# Möglichkeiten und Zähler für Punkte
choices = ["Stein", "Papier", "Schere"]
player_score = 0
computer_score = 0
rounds = 3  # Anzahl der Spiele

print("Willkommen zu Stein, Papier, Schere – Best of 3!")

for i in range(rounds):
    print(f"\nRunde {i + 1}:")

    # Eingabe des Spielers
    player_choice = input("Wähle Stein, Papier oder Schere: ").capitalize()

    # Auswahl des Computers
    computer_choice = random.choice(choices)
    print(f"Computer hat {computer_choice} gewählt.")

    # Überprüfen der Ergebnisse
    if player_choice == computer_choice:
        print("Unentschieden!")
    elif (player_choice == "Stein" and computer_choice == "Schere") or \
            (player_choice == "Papier" and computer_choice == "Stein") or \
            (player_choice == "Schere" and computer_choice == "Papier"):
        print("Du gewinnst diese Runde!")
        player_score += 1
    else:
        print("Computer gewinnt diese Runde!")
        computer_score += 1

    # Zwischenstand anzeigen
    print(f"Zwischenstand: Spieler {player_score} - {computer_score} Computer")

# Endergebnis
print("\nEndergebnis:")
if player_score > computer_score:
    print("Glückwunsch, du hast gewonnen!")
elif player_score < computer_score:
    print("Leider hat der Computer gewonnen.")
else:
    print("Es ist ein Unentschieden!")
