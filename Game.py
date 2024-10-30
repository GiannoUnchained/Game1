import random

# Möglichkeiten und Punktzähler
choices = ["Stein", "Papier", "Schere"]

def spiele_runde():
    # Zähler für Punkte
    player_score = 0
    computer_score = 0

    print("\nNeue Runde startet!")

    # Eingabe der Spielerwahl
    while True:
        player_choice = input("Wähle Stein, Papier oder Schere (oder 'Ende' zum Beenden): ").capitalize()
        if player_choice == "Ende":
            print("Spiel wird beendet. Danke fürs Spielen!")
            return player_score, computer_score, True

        # Validierung der Eingabe
        if player_choice not in choices:
            print("Ungültige Eingabe. Bitte versuche es erneut.")
            continue

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

        # Nach jeder Runde fragen, ob das Spiel fortgesetzt werden soll
        fortsetzen = input("Möchtest du eine weitere Runde spielen? (ja/nein): ").lower()
        if fortsetzen != "ja":
            break

    return player_score, computer_score, False

# Hauptprogramm
def hauptprogramm():
    print("Willkommen zu Stein, Papier, Schere!")

    while True:
        # Frage nach Anzahl der Runden
        try:
            runden = int(input("Wie viele Runden möchtest du spielen? (Gib eine Zahl ein): "))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
            continue

        gesamter_player_score = 0
        gesamter_computer_score = 0

        # Spiele die gewählte Anzahl von Runden
        for i in range(runden):
            print(f"\n--- Runde {i + 1} von {runden} ---")
            player_score, computer_score, beendet = spiele_runde()
            gesamter_player_score += player_score
            gesamter_computer_score += computer_score

            if beendet:
                return

        # Endergebnis
        print("\nEndergebnis nach allen Runden:")
        print(f"Spieler {gesamter_player_score} - {gesamter_computer_score} Computer")
        if gesamter_player_score > gesamter_computer_score:
            print("Glückwunsch, du hast gewonnen!")
        elif gesamter_player_score < gesamter_computer_score:
            print("Leider hat der Computer gewonnen.")
        else:
            print("Es ist ein Unentschieden!")

        # Frage, ob das Spiel neu gestartet werden soll
        neustart = input("\nMöchtest du das Spiel erneut spielen? (ja/nein): ").lower()
        if neustart != "ja":
            print("Danke fürs Spielen! Bis zum nächsten Mal!")
            break

# Spiel starten
hauptprogramm()
