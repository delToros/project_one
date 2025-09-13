import json

# A dictionary to hold the loaded translations
strings = {}
current_language = ""


def load_translations(lang_code):
    """Loads the translation file for a given language code."""
    global strings, current_language
    try:
        with open(f'strings/{lang_code}.json', 'r', encoding='utf-8') as f:
            strings = json.load(f)
            current_language = lang_code
            print(f"Language set to: {current_language}")
    except FileNotFoundError:
        print(f"Error: Translation file '{lang_code}.json' not found.")        # Fallback or exit strategy here
        exit()

def get_text(key):
    """Retrieves translated text for a given key."""
    return strings.get(key, f"Translation missing for key: {key}")

def start_game_language():
    print("Choose your language:")
    print("1. English (en)")
    print("2. Spanish (es)")
    print("3. Russian (es)")

    lang_choice = input("> ")
    if lang_choice == '1':
        load_translations('english')
    elif lang_choice == '2':
        load_translations('spanish')
    elif lang_choice == '3':
        load_translations('spanish')
    else:
        print("Invalid choice, defaulting to English.")
        load_translations('en')

def start_game_race():
    print(get_text("prompt_race_select"))
    race_choice = input("> ")

    if race_choice == '1':
        return "elf"
    elif race_choice == '2':
        return "dwarf"
    elif race_choice == '3':
        return "???"
    else:
        # Error handling for invalid race choice
        print("Invalid choice.")
        return None


def play_game_state(inventory, game_states, key):
    current_state = game_states[key]
    print(current_state['message'])

    if "items" in current_state:
        if current_state['items'].get("add") is not None:
            items_to_add = current_state["items"].get("add", [])
            for item in items_to_add:
                inventory.append(item)
                # Use a placeholder in the translation string for the item name
                print(get_text("item_added").format(item=get_text(f"item_{item}")))

        if current_state['items'].get("remove") is not None:
            items_to_remove = current_state["items"].get("remove", [])
            for item in items_to_remove:
                if item in inventory:
                    inventory.remove(item)
                    print(get_text("item_removed").format(item=get_text(f"item_{item}")))
                else:
                    print(get_text("item_not_in_inventory").format(item=get_text(f"item_{item}")))

    end_game = False

    choices = current_state["choices"]

    while not end_game:
        player_choice = input("> ")

        if player_choice in current_state["choices"]:
            next_state_key = choices[player_choice]
            play_game_state(inventory, game_states, next_state_key)
            break
        else:
            print(get_text("No such choice. Choose from choices available in the message"))


def main_game():
    start_game_language()
    player_race = start_game_race()
    inventory = []

    game_states = strings["game_states"]
    start_states = strings["start_states"]

    start_key = start_states[player_race]

    play_game_state(inventory, game_states, start_key)
