import json

# A dictionary to hold the loaded translations
translations = {}
current_language = ""


def load_translations(lang_code):
    """Loads the translation file for a given language code."""
    global translations, current_language
    try:
        with open(f'strings/{lang_code}.json', 'r', encoding='utf-8') as f:
            translations = json.load(f)
            current_language = lang_code
            print(f"Language set to: {current_language}")
    except FileNotFoundError:
        print(f"Error: Translation file '{lang_code}.json' not found.")        # Fallback or exit strategy here
        exit()

def get_text(key):
    """Retrieves translated text for a given key."""
    return translations.get(key, f"Translation missing for key: {key}")

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
        print(get_text("welcome_message_elf"))
    elif race_choice == '2':
        print(get_text("welcome_message_dwarf"))
    elif race_choice == '3':
        print(get_text("welcome_message_human"))
    else:
        # Error handling for invalid race choice
        print("Invalid choice.")

def main_game():
    start_game_language()
    start_game_race()


    end_game = False
    while not end_game:
        pass
