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
    characters = []

    while True:
        line = input()

        if not line:
            break

        tokens = line.split()

        if not 2 <= len(tokens) <= 3:
            print_error("Invalid number of values")
            continue

        name = tokens[0]

        try:
            initiative = int(tokens[1])
        except ValueError:
            print_error("Initiative is not a valid integer")
            continue

        is_player = tokens[2] == 'p' if len(tokens) > 2 else False

        characters.append(Character(initiative, name, is_player))

    return characters


def main():
    characters = read_input()
    combat_order = sorted(characters, reverse=True)

    for character in combat_order:
        print("{} {}".format(character.initiative, character.name))


main()
