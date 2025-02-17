import requests
import telebot
from bs4 import BeautifulSoup
from settings import API_TOKEN
from telebot import types
import json

bot = telebot.TeleBot(API_TOKEN)

url = "https://habr.com/ru/feed/"
url_development = "https://habr.com/ru/flows/develop/"
url_admin = "https://habr.com/ru/flows/admin/"
url_design = "https://habr.com/ru/flows/design/"
url_management = "https://habr.com/ru/flows/management/"
url_marketing = "https://habr.com/ru/flows/marketing/"
url_popsci = "https://habr.com/ru/flows/popsci/"










headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет!" + " Это бот парсинга сайта хабр")



@bot.message_handler(commands=["articles"])
def handler_arcticles(message):
    flows = arctcles_get_url(url)
    for flow in flows:
        msg = f"{flow['name']}\n{flow['url']}"
        bot.send_message(message.chat.id, msg)

def arctcles_get_url(url):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    try:
        arcticle_find = soup.find_all("h2", attrs={"tm-title tm-title_h2"})


        if arcticle_find:
            articles = []
            for el in arcticle_find[:10]:
                article = {"name" : el.text,
                           "url" : "https://www.habr.com/" + el.find("a")["href"]
                           }
                articles.append(article)

            return articles



        else:
            print("Элемент не найден")
            return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""


@bot.message_handler(commands=["complaint"])
def handler_complaint(message):

    bot.send_message(message.chat.id, "Напишите жалобу")
    bot.register_next_step_handler_by_chat_id(
        message.chat.id,
        save_complaint
    )


def add_complaint(client,  text)  :
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"complaint"  :  []}
    new_complaint = {"client" : client, "text"  :  text}
    data["complaint"].append(new_complaint)

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def save_complaint(message):
    client = message.chat.id
    text = message.text
    add_complaint(client , text)
    bot.send_message(message.chat.id , "Спасибо за жалобу")









@bot.message_handler(commands=["articles_by_flows"])
def handler_articles_by_flow(message):
    bot.send_message(message.chat.id, "Выберете и напишите пожалуйста поток хабра:\n" + "Разработка\n" + "Администрация\n" + "Дизайн\n" + "Менеджемент\n" + "Маркетинг\n" + "Научпоп\n")
    bot.register_next_step_handler_by_chat_id(
        message.chat.id,
        echo_all
    )


def echo_all(message):
    if message.text == "Разработка" or message.text == "разработка":
        bot.reply_to(message , "Вы выбрали разработку")
        flow_article_development(message)

    elif message.text == "Администрация" or message.text == "администрация":
        bot.reply_to(message , "Вы выбрали администрацию")
        flow_article_admin(message)

    elif message.text == "Дизайн" or message.text == "дизайн":
        bot.reply_to(message , "Вы выбрали дизайн")
        flow_article_design(message)

    elif message.text == "Менеджемент" or message.text == "менеджемент":
        bot.reply_to(message , "Вы выбрали менеджемент")
        flow_article_management(message)


    elif message.text == "Маркетинг" or message.text == "маркетинг":
        bot.reply_to(message , "Вы выбрали маркетинг")
        flow_article_marketing(message)



    elif message.text == "Научпоп" or message.text == "научпоп":
        bot.reply_to(message , "Вы выбрали научпоп")
        flow_article_popsci(message)









def flows_articles_development_get_url(url):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    try:
        arcticle_find = soup.find_all("h2", attrs={"tm-title tm-title_h2"})


        if arcticle_find:
            articles = []
            for el in arcticle_find[:10]:
                article = {"name" : el.text,
                           "url" : "https://www.habr.com" + el.find("a")["href"]
                           }
                articles.append(article)

            return articles

        else:
            print("Элемент не найден")
            return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""

def flow_article_development(message):
    flows = flows_articles_development_get_url(url_development)
    for flow in flows:
        msg = f"{flow['name']}\n{flow['url']}"
        bot.send_message(message.chat.id, msg)

def flows_articles_admin_get_url(url):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    try:
        arcticle_find = soup.find_all("h2", attrs={"tm-title tm-title_h2"})

        if arcticle_find:
            articles = []
            for el in arcticle_find[:10]:
                article = {"name" : el.text,
                           "url" : "https://www.habr.com" + el.find("a")["href"]
                           }
                articles.append(article)

            return articles

        else:
            print("Элемент не найден")
            return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""

def flow_article_admin(message):
    flows = flows_articles_admin_get_url(url_admin)
    for flow in flows:
        msg = f"{flow['name']}\n{flow['url']}"
        bot.send_message(message.chat.id, msg)


def flows_articles_design_get_url(url):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    try:
        arcticle_find = soup.find_all("h2", attrs={"tm-title tm-title_h2"})
        if arcticle_find:
            articles = []
            for el in arcticle_find[:10]:
                article = {"name" : el.text,
                           "url" : "https://www.habr.com" + el.find("a")["href"]
                           }
                articles.append(article)

            return articles


        else:
            print("Элемент не найден")
            return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""


def flow_article_design(message):
    flows = flows_articles_design_get_url(url_design)
    for flow in flows:
        msg = f"{flow['name']}\n{flow['url']}"
        bot.send_message(message.chat.id, msg)


def flows_articles_management_get_url(url):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    try:
        arcticle_find = soup.find_all("h2", attrs={"tm-title tm-title_h2"})
        if arcticle_find:
            articles = []
            for el in arcticle_find[:10]:
                article = {"name" : el.text,
                           "url" : "https://www.habr.com" + el.find("a")["href"]
                           }
                articles.append(article)

            return articles

        else:
            print("Элемент не найден")
            return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""


def flow_article_management(message):
    flows = flows_articles_management_get_url(url_management)
    for flow in flows:
        msg = f"{flow['name']}\n{flow['url']}"
        bot.send_message(message.chat.id, msg)



def flows_articles_marketing_get_url(url):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    try:
        arcticle_find = soup.find_all("h2", attrs={"tm-title tm-title_h2"})
        if arcticle_find:
            articles = []
            for el in arcticle_find[:10]:
                article = {"name" : el.text,
                           "url" : "https://www.habr.com" + el.find("a")["href"]
                           }
                articles.append(article)

            return articles



        else:
            print("Элемент не найден")
            return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""


def flow_article_marketing(message):
    flows = flows_articles_marketing_get_url(url_marketing)
    for flow in flows:
        msg = f"{flow['name']}\n{flow['url']}"
        bot.send_message(message.chat.id, msg)


def flows_articles_popsci_get_url(url):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    try:
        arcticle_find = soup.find_all("h2", attrs={"tm-title tm-title_h2"})
        if arcticle_find:
            articles = []
            for el in arcticle_find[:10]:
                article = {"name" : el.text,
                           "url" : "https://www.habr.com" + el.find("a")["href"]
                           }
                articles.append(article)

            return articles



        else:
            print("Элемент не найден")
            return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""


def flow_article_popsci(message):
    flows = flows_articles_design_get_url(url_popsci)
    for flow in flows:
        msg = f"{flow['name']}\n{flow['url']}"
        bot.send_message(message.chat.id, msg)















if __name__ == "__main__":
    bot.polling(non_stop=True, interval=2)