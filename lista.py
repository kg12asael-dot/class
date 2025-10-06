from datetime import datetime

class GameList:
    def __init__(self):
        self.games = [
            "Dark Soul",
            "Ghost of Tsushima",
            "Death Stranding",
            "Hollow",
            "God of War"
        ]

    def save_to_file(self, filename="games.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for game in self.games:
                file.write(game + "\n")
            file.write(f"\nActualizado: {datetime.now()}\n")

        # Mostrar contenido del archivo
        with open(filename, "r", encoding="utf-8") as file:
            print("Contenido de 'games.txt':\n")
            print(file.read())

if __name__ == "__main__":
    lista = GameList()
    lista.save_to_file()