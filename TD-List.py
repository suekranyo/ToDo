import os

DATEINAME = "todo.txt"

#Aufgabe aus Datei Laden

def lade_aufgaben():
    aufgaben = []
    if os.path.exists(DATEINAME):
        with open (DATEINAME, "r") as datei:
            aufgaben = [zeile.strip() for zeile in datei.readlines()]
    return aufgaben

def speichere_aufgaben(aufgaben):
    with open(DATEINAME, "w") as datei:
        for aufgabe in aufgaben:
            datei.write(aufgabe + "\n")

def zeige_menü():
    print("\n--- To-Do-Liste ---")
    print("1. Aufageb hinzufügen")
    print("2. Alle Aufgaben anzeigen")
    print("3. Aufgabe bearbeiten")
    print("4. Aufgabe löschen")
    print("5. Beenden")

# Hauptzprogramm
def todo_liste():
    aufgaben = lade_aufgaben()

    while True:
        zeige_menü()
        auswahl = input("Wähle eine Option (1-5): ")

        if auswahl == "1":
            neue_aufgabe = input("Neue Aufgabe: ")
            aufgaben.append(neue_aufgabe)
            speichere_aufgaben(aufgaben)
            print("Aufgabe hinzufügen. ")

        elif auswahl == "2":
            print("\n--- Aufgaben ---")
            if not aufgaben:
                print("Keine Aufgaben vorhanden.")
            else:
                for i, aufgabe in enumerate(aufgaben, 1):
                    print(f"{i}. {aufgabe}")
                try:
                    nummer = int(input("Welche Aufgabe willst du bearbeiten? (Nummer)"))
                    if 1 <= nummer <= len(aufgaben):
                        neue_version = input("Neue Aufgabe: ")
                        aufgaben[nummer - 1] = neue_version
                        speichere_aufgaben(aufgaben)
                        print("Aufgabe bearbeiten.")
                    else:
                        print("Ungültige Nummer.")
                except ValueError:
                    print("Bitte eine gültige Zahl eingeben.")
        elif auswahl == "4":
            if not aufgaben:
                print("Keine Aufageben zum Löschen.")
                continue
            for i, aufgabe in enumerate(aufgaben, 1):
                print(f"{i}. {aufgabe}")
            try:
                nummer = int(input("Welche Aufgaben willst du löschen? (Nummer) :"))
                if 1 <=nummer <= len(aufgaben):
                    geloescht = aufgaben.pop(nummer -1)
                    speichere_aufgaben(aufgaben)
                    print(f"Aufgabe '{geloescht}' gelöscht.")
                else:
                    print("Ungültige Nummer.")
            except ValueError:
                print("Bitte eine gültige zahl eingeben.")

        elif auswahl == "5":
            print(("Programm beendet."))
            break
        else:
            print("Ungültige Auswahl. Bitte Zahl von 1 bis 5 eingeben.")

todo_liste()










