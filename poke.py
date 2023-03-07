import random
from colorama import init, Fore, Style

# initialize colorama
init()

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
    print(Fore.RED + f"{attacker['name']} attacked {defender['name']} for {damage} damage!" + Style.RESET_ALL)
    if defender["hp"] <= 0:
        print(Fore.GREEN + f"{defender['name']} fainted!" + Style.RESET_ALL)
        return True
    return False


# game loop
while True:
    # display player and opponent information
    print(Fore.YELLOW + f"{player_pokemon['name']} (HP: {player_pokemon['hp']}) vs. {opponent_pokemon['name']} (HP: {opponent_pokemon['hp']})" + Style.RESET_ALL)

    if player_turn:
        # player's turn
        print(Fore.BLUE + "Choose an action:" + Style.RESET_ALL)
        print("1. Attack")
        print("2. Switch Pokémon")
        action = input("> ")
        if action == "1":
            attack(player_pokemon, opponent_pokemon)
        elif action == "2":
            print(Fore.BLUE + "Switching Pokémon is not implemented yet." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid action." + Style.RESET_ALL)
            continue
    else:
        # opponent's turn
        attack(opponent_pokemon, player_pokemon)

    # check if the battle is over
    if player_pokemon["hp"] <= 0:
        print(Fore.RED + "You lost the battle." + Style.RESET_ALL)
        break
    elif opponent_pokemon["hp"] <= 0:
        print(Fore.GREEN + "You won the battle!" + Style.RESET_ALL)
        break

    # switch turns
    player_turn = not player_turn
