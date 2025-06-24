from services import messages_service
from services import article_api_service
from services import hint_api_service

# how are services working, api logic


def show_the_rules():
    messages_service.show_rules()

def welcome_players():
    messages_service.launch_welcome_package()
    ask_user = 0
    while ask_user != 1 and ask_user != 2:
        try:
            ask_user = int(input("do you need to see the rules? \n1. Yes I want to see the rules \n2. No I know the rules.\n"))
        except ValueError:
            print("Please enter a number.")
    if ask_user == 1:
        show_the_rules()
    elif ask_user == 2:
        print("Let's Roll")
    are_players_ready = input("\nPress enter if you are ready to be the next Articleus!")
    if are_players_ready is not None:
        messages_service.clear_game_space()
        return


def set_the_ground_rules():
    print("***Let's set some ground rules***")
    number_of_players = "player"
    while type(number_of_players) is not int:
        try:
            number_of_players = int(input("Please enter the number of players competing to be the next Articleus?\n"))
        except ValueError:
            print("Please enter a number.")

    number_of_rounds = "rounds"
    while type(number_of_rounds) is not int:
        try:
            number_of_rounds = int(input("Please enter the number of rounds you want to play?\n"))
        except ValueError:
            print("Please enter a number.")

    return number_of_players, number_of_rounds

def select_the_category(list_of_categories):
    messages_service.show_category_list(list_of_categories)
    #implement round-robin among players of the game to select the category from the list

    category_selected = ""
    while not category_selected in list_of_categories:
        category_selected = input("Please enter the title of category you want to select from the list above: ")

    return category_selected

def find_random_article(selected_category):
    randomly_selected_article = article_api_service.select_random_article(selected_category)
    return randomly_selected_article

def get_hint_list(hidden_article_for_the_player):
    hints_found = hint_api_service.find_hints(hidden_article_for_the_player)
    return hints_found

def create_choice_list(selected_category, hidden_article_for_the_player):
    choice_list = article_api_service.articles_choice_list(selected_category, hidden_article_for_the_player)
    return choice_list

def ready_to_guess(multiple_choice_list, hidden_article_for_the_player):
    messages_service.show_choice_list(multiple_choice_list)
    user_choice = ""
    while not user_choice in multiple_choice_list:
        user_choice = input("Please enter the title you guessed from the list above: ")
    guessed_right = user_choice in multiple_choice_list and user_choice == hidden_article_for_the_player
    return guessed_right

def toss_the_hint(hints_revealed, multiple_choice_list, hidden_article_for_the_player):
    messages_service.show_revealed_hints(hints_revealed)
    print("Are you ready to guess the article, or you need more hints?")
    ask_user = 0
    while ask_user != 1 and ask_user != 2:
        try:
            ask_user = int(input("1. Yes I am ready to guess 😎:\n2. No I need more hints 😐:\n"))

        except ValueError:
            print("Please enter a number.")

    if ask_user == 1:
        player_guessed_right = ready_to_guess(multiple_choice_list, hidden_article_for_the_player)
        return player_guessed_right
    elif ask_user == 2:
        return False

def show_last_hint(multiple_choice_list, hidden_article_for_the_player):
    messages_service.show_last_hint(article_api_service.get_hidden_article_summary(hidden_article_for_the_player))
    return ready_to_guess(multiple_choice_list, hidden_article_for_the_player)

def start_play(player_number, selected_category):
    print(f"Player {player_number+1} started the round 😃😃😃")
    hidden_article_for_the_player = find_random_article(selected_category)
    hints_for_hidden_article = get_hint_list(hidden_article_for_the_player)
    multiple_choice_list = create_choice_list(selected_category, hidden_article_for_the_player)
    #score = len(hints_for_hidden_article) % ((player_number//2) + 1)
    score = len(hints_for_hidden_article) + 1
    for i in range(1, len(hints_for_hidden_article)+1):
        score -= 1
        player_guessed_right = toss_the_hint(hints_for_hidden_article[:i], multiple_choice_list, hidden_article_for_the_player)
        if player_guessed_right:
            break

    if score == 1:
        player_guessed_on_last_hint = show_last_hint(multiple_choice_list, hidden_article_for_the_player)
        if player_guessed_on_last_hint is False:
            score = 0
    if score > 0:
        messages_service.print_correct_answer_round(score)
    return (player_number+1, score)

def find_max_tuples(tupple_list):
    # Step 1: Find the max value at index 1
    max_value = max(x[1] for x in tupple_list)

    # Step 2: Get all tuples that have this max value
    max_tuples = [t for t in tupple_list if t[1] == max_value]

    return  max_tuples

def announce_round_score(round_scores):
    messages_service.print_scoreboard_round(round_scores)

    max_scorers = find_max_tuples(round_scores)
    round_winners = [t[0] for t in max_scorers]

    return round_winners

def start_the_round(number_of_players, is_tie_breaker=False):
    list_of_categories = article_api_service.random_category_list()
    selected_category = select_the_category(list_of_categories)
    print(f"Selected category for this round is: 👉 {selected_category}")

    round_scores = []
    for i in range(0, number_of_players):
        player_number, score = start_play(i, selected_category)
        round_scores.append((player_number, score))

    winner_player_number = announce_round_score(round_scores)
    return winner_player_number

def announce_game_score(round_winners):
    messages_service.print_scoreboard_game(round_winners)

def announce_game_winners(round_winners):
    max_scorers = find_max_tuples(round_winners)
    round_winners = [t[0] for t in max_scorers]
    messages_service.print_scoreboard_game(round_winners)

def start_the_game(number_of_players, number_of_rounds):
    #create a loop to start the round based on number_of_rounds
    final_round_winners = []
    for i in range(0, number_of_rounds):
        round_winner = start_the_round(number_of_players)
        final_round_winners += round_winner

    print("Game finished")

    counts = {}
    for item in final_round_winners:
        counts[item] = counts.get(item, 0) + 1

    for num in range(1, number_of_players + 1):
        if num not in counts:
            counts[num] = 0  # Add missing numbers with 0 occurrences

    result = list(counts.items())
    final_score = sorted(result, key=lambda x: x[1])
    announce_game_score(final_score)

def main():
    welcome_players()
    number_of_players, number_of_rounds = set_the_ground_rules()
    start_the_game(number_of_players, number_of_rounds)

if __name__ == "__main__":
    main()


