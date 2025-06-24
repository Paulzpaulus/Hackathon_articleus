from colorama import Fore, Back, Style, init
init(autoreset=True)
from PIL import Image
import pyfiglet


from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform compatibility and to prevent from having ro reset everytime...
init(autoreset=True)

def print_wrong_answer_round():
    """Prints text in red to indicate a wrong answer."""
    print(Fore.RED + "Not quite! The truth is still out there. Try again or reveal a hint.")

def print_wrong_answer_last_chance():
    """Prints text in red to indicate a wrong answer on the final attempt."""
    print(Fore.RED + "This is it! No more hints left! Make your final call, detective.")

def print_correct_answer_round():
    """Prints text in green to indicate a correct answer."""
    print(Fore.GREEN + "Great job, detective!🕵️‍♂️ You found the correct article!",
          "Truly articleus!")


def print_hint(text):
    """Prints text in blue to give a hint to the player."""
    print(Fore.BLUE + "🔎Hint revealed! Use it wisely to uncover the truth.")


def print_winner_game(text):
    """Prints the winner message in bright yellow for emphasis."""
    print(Fore.YELLOW +
          Style.BRIGHT + f"{player} has won the game with"
                         f" a total score of {total_score}"
                         f" Congratulations! You are truly an Articleus!🕵️‍♂️")


#def print_scoreboard_round(scoreboard):

    #Prints a 2D scoreboard in a structured format.
    #Each row represents a player and their score.

    #print(Fore.MAGENTA + "\n Round SCOREBOARD")
    #print(Fore.MAGENTA + "=" * 20)

    #for player, score in scoreboard.items():
        #print(Fore.CYAN + f"Player {player}:{score}")
    #print(Fore.MAGENTA + "=" * 20)


def print_scoreboard_game(scoreboard):
    """
    Prints a 2D scoreboard in a structured format.
    Each row represents a player and their score.
    """
    print(Fore.MAGENTA + "\n Round SCOREBOARD")
    print(Fore.MAGENTA + "=" * 20)

    for player, score in scoreboard.items():
        print(Fore.CYAN + f"{player}: {score}")
    print(Fore.MAGENTA + "=" * 20)


def print_colored_title(text, color=Fore.CYAN):
    ascii_art = pyfiglet.figlet_format(text, font="block")
    print(color + ascii_art)



ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image_path, new_width=200):
    img = Image.open(image_path).convert("L")

    # adjust size
    width, height = img.size
    new_height = int((height / width) * new_width * 0.5)
    img = img.resize((new_width, new_height))

    # transform Pixel to ASCII-chars
    pixels = img.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel//32] for pixel in pixels)  # identify the row location of "::"

    # line formatting
    ascii_str = "\n".join(
        ascii_str[i: i + new_width] for i in range(0, len(ascii_str), new_width)
    )

    return ascii_str


# Example usage of the functions
if __name__ == "__main__":
    print_colored_title("Articleus", Fore.YELLOW)  #
    ascii_art_image = image_to_ascii("services/articleus.png", new_width=76)  # transform image
    print(Fore.BLUE + ascii_art_image)
    print_hint("Hint: Think about the capital city of France.")

    example_scoreboard = {"Alice": 5, "Bob": 3, "Charlie": 7}
    print_scoreboard_round(example_scoreboard)
    print_scoreboard_game(example_scoreboard)





