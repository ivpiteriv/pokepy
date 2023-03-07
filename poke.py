import random

# define game variables
player_pokemon = {"name": "Pikachu", "type": "Electric", "hp": 50, "attack": 10, "defense": 5, "speed": 20, "level": 5}
opponent_pokemon = {"name": "Charmander", "type": "Fire", "hp": 40, "attack": 8, "defense": 3, "speed": 15, "level": 5}
player_turn = True

# define game functions


def attack(attacker, defender):
    damage = (2 * attacker["level"] / 5 + 2) * \
        attacker["attack"] / defender["defense"] + 2
    # add some randomness to damage calculation
    damage *= random.uniform(0.9, 1.1)
    damage = int(damage)
    defender["hp"] -= damage
    print(
        f"{attacker['name']} attacked {defender['name']} for {damage} damage!")
    if defender["hp"] <= 0:
        print(f"{defender['name']} fainted!")
        return True
    return False


# game loop
while True:
    # display player and opponent information
    print(
        f"{player_pokemon['name']} (HP: {player_pokemon['hp']}) vs. {opponent_pokemon['name']} (HP: {opponent_pokemon['hp']})")

    if player_turn:
        # player's turn
        print("Choose an action:")
        print("1. Attack")
        print("2. Switch Pokémon")
        action = input("> ")
        if action == "1":
            attack(player_pokemon, opponent_pokemon)
        elif action == "2":
            print("Switching Pokémon is not implemented yet.")
        else:
            print("Invalid action.")
            continue
    else:
        # opponent's turn
        attack(opponent_pokemon, player_pokemon)

    # check if the battle is over
    if player_pokemon["hp"] <= 0:
        print("You lost the battle.")
        break
    elif opponent_pokemon["hp"] <= 0:
        print("You won the battle!")
        break

    # switch turns
    player_turn = not player_turn

