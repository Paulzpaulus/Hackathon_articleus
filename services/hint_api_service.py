import wikipediaapi
import random
from keybert import KeyBERT

def get_words_clean(text):
    dirty_list = text.split()
    cleaned_list = []
    for word in dirty_list:
        if word[-1] == "." or word[-1] == ";" or word[-1] == ",":
            cleaned_list.append(word[:-1])
        else:
          cleaned_list.append(word)
    return cleaned_list


def words_frequency(words, title):
    word_and_ammount = {}
    for word in words:
        if word.islower() or len(word) < 5 or title in word or word[-2] == "'" or word in title:
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
      if len(most_frequent[0]) > 0:
        del freq[most_frequent[0]]
      most_frequent_list.append(most_frequent[0])
    return most_frequent_list

def get_hint_by_freq(article, title):
    hint_list_freq = []
    list_of_words = get_words_clean(article)
    dict_of_words_and_ammount = words_frequency(list_of_words, title)
    top_words_for_hints = top_n_words(dict_of_words_and_ammount, 30)
    for i in range(9):
       rand_counter = random.randint(0,20)
       hint_list_freq.append(top_words_for_hints[rand_counter])
    return hint_list_freq


def get_hints_by_sections(article):
    section_of_article = article.sections
    hint_list = []
    for s in section_of_article:
        hint_list.append(s.title)
    return hint_list[:7]

def has_number(text: str):
    return any(char.isdigit() for char in text)

def find_hints(target_article, number_of_hints = 5):
    topic = target_article
    hints = []
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

    wiki_wiki = wikipediaapi.Wikipedia(user_agent="Articleus", language="en")
    selected_article = wiki_wiki.page(target_article)
    if len(selected_article.title) == 0 or len(selected_article.text) == 0:
        print(f"there was an article selected by api which either doesn't have a title or a text: {target_article}")
        return []
    list_of_ten_hints = get_hint_by_freq(selected_article.text, selected_article.title) + get_hints_by_sections(selected_article)
    while len(hints) < number_of_hints:
       rand_counter = random.randint(0,len(list_of_ten_hints)-1)
       if list_of_ten_hints[rand_counter] not in hints and list_of_ten_hints[rand_counter] not in month_list and not has_number(list_of_ten_hints[rand_counter]) :
           hints.append(list_of_ten_hints[rand_counter])
    return hints
