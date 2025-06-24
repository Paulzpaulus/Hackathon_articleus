import wikipediaapi
import wikipedia
import textwrap
import random

# Initialize the Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(user_agent="Articuleus", language='en')


def get_subcategories(category_page, depth=1):
    """ Recursively fetch subcategories from a given Wikipedia category page. """
    subcategories = []
    while True:
        try:
            if category_page.exists():
                for title, subcategory in category_page.categorymembers.items():
                    if subcategory.ns == wikipediaapi.Namespace.CATEGORY:  # Ensure it's a category
                        subcategories.append(title.replace("Category:", ""))
                        if depth > 0:
                            subcategories.extend(get_subcategories(subcategory, depth - 1))
            return subcategories
        except Exception as e:
            pass


def fetch_10_random_crime_categories():
    category = wiki_wiki.page("Category:Crime")
    # Fetch crime subcategories
    crime_categories = get_subcategories(category, depth=1)

    # Select 10 random crime categories
    random_crime_categories = random.sample(crime_categories, min(10, len(crime_categories)))
    return random_crime_categories


def display_crime_categories(crime_categories: list):
    """Display the crime categories."""

    # If no categories found, print a message
    if not crime_categories:
        print("No crime categories found.")
    else:
        # Display all crime categories
        print("All Crime Categories:")
        for idx, category in enumerate(crime_categories, 1):
            print(f"{idx}. {category}")


def fetch_number_of_article_titles(category: str, number_of_articles: int):
    articles = []
    while True:
        search_results = wikipedia.search(category, results=number_of_articles)
        if len(articles) >= number_of_articles:
            break
        for result in search_results:
            page = wiki_wiki.page(result)
            if page.exists():
                article_title = page.title.strip().capitalize()
                if article_title not in articles:
                    articles.append(article_title)

    return articles


def select_a_random_article_title(category: str):
    random_article_title = fetch_number_of_article_titles(category, 1)[0]
    return random_article_title


def create_summary_of_selected_hidden_article(random_article_title: str):
    page = wiki_wiki.page(random_article_title)  # Get the page again to fetch the summary
    # Wikipedia API provides a summary attribute
    if page.exists():
        return page.summary
    else:
        print("No article found.")


def fetch_list_of_random_9_articles_titles(category: str):
    return fetch_number_of_article_titles(category, 9)


def create_10_articles_choices(selected_9_articles_titles: list, hidden_article_title: str):
    choices_articles = selected_9_articles_titles
    choices_articles.append(hidden_article_title)
    return choices_articles


# ----------------------
def display_hidden_article_summary(random_article_summary: str):
    try:
        article = random_article_summary.strip().split('\n')
        for paragraph in article:
            formatted_summary = textwrap.fill(paragraph, width=120)
            print(formatted_summary)
    except Exception:
        formatted_summary = textwrap.fill(random_article_summary, width=120)
        print(formatted_summary)


def display_10_choices_articles(articles_titles_choices: list):
    for index, title in enumerate(articles_titles_choices):
        print(f"{index + 1}. {title}")

