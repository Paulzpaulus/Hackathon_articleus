from services import name_logo
from colorama import Fore, Back, Style, init
init(autoreset=True)

def launch_welcome_package():
    name_logo.create_colored_title()
    name_logo.create_logo()


def clear_game_space():
    print("TODO: Clear console")
    name_logo.create_colored_title()


def show_rules():
    print(Style.BRIGHT + "Set Up the Game:")
    print(Style.NORMAL + "Enter the number of Players for this game.")
    print(Style.NORMAL + "Enter the number of rounds you want to play.")

    print(Style.BRIGHT + "\nStarting the Game:")
    print(Style.NORMAL + "Choose a category.")
    print(Style.NORMAL + "The game selects a random starting article from the chosen category.")
    print(Style.NORMAL + "That's the article you need to find...but it's hidden - A mystery!")

    print(Style.BRIGHT + "\nHow to play:")
    print(Style.NORMAL + "You receive a clue about the target article.")
    print(Style.NORMAL + "The game will present you 10 article titles from the"
                         " of the chosen category.")
    print(Style.NORMAL + "One of them is the article you need to find."
                       + f" The others... are {Fore.RED}'red herrings'{Style.RESET_ALL}")
    print(Style.NORMAL + "You can choose to reveal another hint, OR you guess the correct answer from the list.")
    print(Style.NORMAL + "You have 5 attempts to find the correct target article.")

    print(Style.BRIGHT + "\nMaking Guesses:")
    print(Style.NORMAL + "If you can't guess the correct article within 5 tries, "
                         "you’ll be presented with 5 possible articles—one correct, four false.")
    print(Style.NORMAL + "We don't want you to loose the lead! If you cannot find the correct answer"
                         "after all hints are revealed, we will provide with a little sneak peak"
                         "and you can make a last guess.")
    print(Style.NORMAL + "Choose wisely!")

    print(Style.BRIGHT + "\nWinning the Game:")
    print(Style.NORMAL + "The game proceeds until every Player"
                         " has played once each round.")
    print(Style.BRIGHT + "The player who has found the correct article with least amount of hints wins the round!"
                         "The player who wins the most rounds wins the Game!")



def show_category_list(category_list):
    print(Style.BRIGHT + "You have following categories to choose from: ")

    for category in category_list:
        print(f"-📗 {category}")


def show_revealed_hints(revealed_hints, total_hints= 5):
    hint_list = revealed_hints
    for i in range (len(revealed_hints), total_hints):
        hint_list.append("****************")
    print(Style.BRIGHT + "You have following hints to help you with the guess: ")

    for hint in hint_list:
        print(f"🤔-- {hint}")


def show_choice_list(choice_list):
    print(Style.BRIGHT + "You have following articles to choose from: ")

    for choice in choice_list:
        print(f"-🟢- {choice}")


def reveal_hint(text):
    """Prints text in blue to give a hint to the player."""
    print(Fore.BLUE + "🔎Hint revealed! Use it wisely to uncover the truth.")

def print_wrong_answer_last_chance():
    """Prints text in red to indicate a wrong answer on the final attempt."""
    print(Fore.RED + Style.DIM + "This is it! No more hints left!🫣")

def show_last_hint(article_summary):
    print(Style.BRIGHT + "Here's the summary of the article we found for you, read it and see if you can now guess the article:\n")
    print("👉" + Fore.LIGHTBLUE_EX + Style.DIM + article_summary)


def print_correct_answer_round(score):
    """Prints text in green to indicate a correct answer."""
    print(Fore.GREEN + f"Great job, detective!🕵️‍♂️ You found the correct article! and scored {score}"
           + Fore.GREEN + " Truly articleus!")

def print_scoreboard_round(scoreboard):
    """
    Prints a 2D scoreboard in a structured format.
    Each row represents a player and their score.
    """
    print(Fore.MAGENTA + Style.BRIGHT + "\n Round SCOREBOARD")
    print(Fore.MAGENTA + "=" * 20)

    for player, score in scoreboard:
        print(Fore.CYAN + f"Player {player}, Score:{score}")

    print(Fore.MAGENTA + "=" * 20)


def print_scoreboard_game(scoreboard):
    """
    Prints a 2D scoreboard in a structured format.
    Each row represents a player and their score.
    """
    print(Fore.CYAN + Style.BRIGHT + "The game has finished! The finals scores are:" )
    print(Fore.MAGENTA + Style.BRIGHT + "\n Game total SCOREBOARD")
    print(Fore.MAGENTA + "=" * 20)

    for player, score in scoreboard:
        print(Fore.CYAN + f"Player {player}, Rounds Won:{score}")

    print(Fore.MAGENTA + "=" * 20)



def print_winner_game(players, top_score):
    """Prints the winner message in bright yellow for emphasis."""
    player_text = ""
    for player in players:

        print(Fore.YELLOW +
          Style.BRIGHT + f"{player} won the game with"
                         f" a total score of {total_score}"
                         f" Congratulations! You are Articleus!🕵️‍♂️")

