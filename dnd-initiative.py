class Character:
    def __init__(self, initiative, name, is_player):
        self.initiative = initiative
        self.name = name
        self.is_player = is_player

    def __lt__(self, other):
        if self.initiative < other.initiative:
            return True

        # If initiatives are equal, PC:s go before NPC:s.
        if self.initiative == other.initiative:
            return not self.is_player and other.is_player

        return False


def print_error(msg):
    print("error: " + msg)


def read_input():
    UNDO = "r"

    characters = []

    while True:
        line = input()

        if not line:
            break

        if line == UNDO:
            if not characters:
                print_error("Nothing to remove")
            else:
                print("Removed character \"{}\"".format(characters[-1].name))
                del characters[-1]
            continue

        tokens = line.split()

        if len(tokens) < 2:
            print_error("Too few values")
            continue

        is_player = tokens[-1] == "p"

        # Drop the is_player token, so the initiative is the last element.
        if is_player:
            del tokens[-1]

        try:
            initiative = int(tokens[-1])
        except ValueError:
            print_error("Initiative is not a valid integer")
            continue

        name = " ".join(tokens[:-1])

        characters.append(Character(initiative, name, is_player))

    return characters


def main():
    characters = read_input()
    combat_order = sorted(characters, reverse=True)

    for character in combat_order:
        print("{} {}".format(character.initiative, character.name))


main()
