import wikipediaapi
import random

topic = "TODO: Article from SONAM"

Wikiapi_search_engine = wikipediaapi.Wikipedia(user_agent="Articleus", language="en")
selected_article = Wikiapi_search_engine.page(topic)


def get_words_clean(text):
    dirty_list = text.split()
    cleaned_list = []
    for word in dirty_list:
      if word[-1] == "." or word[-1] == ";" or word[-1] == ",":
        cleaned_list.append(word[:-1])
      else:
        cleaned_list.append(word)
    return cleaned_list


def words_frequency(words):
    word_and_ammount = {}
    for word in words:
        if word.islower() or len(word) < 5 or word in topic:
            pass
        else:
            if word not in word_and_ammount:
                word_and_ammount[word] = 0
            word_and_ammount[word] += 1
    return word_and_ammount


def top_n_words(freq, n):
    most_frequent_list = []
    for x in range(n):
      most_frequent = ("",0)
      for word, frequency in freq.items():
        if frequency > most_frequent[1]:
          most_frequent = word, frequency
      del freq[most_frequent[0]]
      most_frequent_list.append(most_frequent[0])
    return most_frequent_list

def get_hint_by_freq(article):
    hint_list_freq = []
    list_of_words = get_words_clean(article)
    dict_of_words_and_ammount = words_frequency(list_of_words)
    top_words_for_hints = top_n_words(dict_of_words_and_ammount, 30)
    for i in range(6):
       rand_counter = random.randint(0,20)
       hint_list_freq.append(top_words_for_hints[rand_counter])
    return hint_list_freq


def get_hints_by_sections(article):
    section_of_article = article.sections
    hint_list = []
    for s in section_of_article:
        hint_list.append(s.title)
    return hint_list[:6]


def find_hints(target_article, number_of_hints = 5):
    print(f"TODO: return list of {number_of_hints} hints for the article {target_article}")
    hints = []
    get_hint_by_freq(selected_article.text)
    get_hints_by_sections(selected_article)
    list_of_ten_hints = get_hint_by_freq(selected_article.text) + get_hints_by_sections(selected_article)
    for i in range(6):
       rand_counter = random.randint(0,10)
       hints.append(list_of_ten_hints[rand_counter])
    return hints


