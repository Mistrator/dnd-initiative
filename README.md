# dnd-initiative
Create a sorted initiative list to determine the order of battle.

## Usage

List all the characters taking part in the battle, one character per line. An
empty line finishes and prints the battle order.

Character syntax: `<character name> <initiative> [p]`, where

* `p`: the character is a player character, and thus it should go before NPC:s with
an equal initiative in the battle order

Inputting a single `r` removes the previously added character.

## Example

### Input

```
$ python dnd-initiative.py
Dragon 14
Cultist 7
Erya 14 p
Orc 16
<empty line>

```

### Output

```
16 Orc
14 Erya
14 Dragon
7 Cultist
```
