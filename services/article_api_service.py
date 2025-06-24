from services import article_category

def random_category_list():
    #print(f"Debug API: random_category_list")
    list_of_categories = article_category.fetch_10_random_categories()
    return list_of_categories
# Func2: Fetch List of articles in that category and select a random article from that list
def select_random_article(category_selected):
    #print(f"Debug API: select_random_article")
    random_article_title = article_category.select_a_random_article_title(category_selected)
    return random_article_title
def get_hidden_article_summary(hidden_article_title):
    #print(f"Debug API: get_hidden_article_summary")
    random_article_summary = article_category.create_summary_of_selected_hidden_article(hidden_article_title)
    return random_article_summary
# Func3: Fetch a list of 9 articles titles excluding the one selected in Func2
def articles_choice_list(category_selected, article_selected):
    #print(f"Debug API: articles_choice_list")
    choice_list = article_category.create_10_articles_choices(category_selected, article_selected)
    return choice_list



