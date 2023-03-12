from base import BotTelegram
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from BaseNewsAPI import BaseNewsAPI
from time import sleep
import datetime
import locale



class BotTelegramNews(BotTelegram, BaseNewsAPI):
    def __init__(self, nombre, token, api_key):
        BotTelegram.__init__(self, nombre, token)
        BaseNewsAPI.__init__(self, api_key)

        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        self.case = {
            'business': 'negocios',
            'entertainment': 'entretenimiento',
            'general': 'general',
            'health': 'salud',
            'science': 'ciencia',
            'sports': 'deportes',
            'technology': 'tecnología'
        }
        self.keyboard = [[
            InlineKeyboardButton("Negocios 💰", callback_data='business'),
             InlineKeyboardButton("Tecnología 🤖", callback_data='technology'),
            InlineKeyboardButton("General 🌏", callback_data='general')],
            [InlineKeyboardButton("Salud ⚕", callback_data='health'),
             InlineKeyboardButton("Ciencia 🧪", callback_data='science'),
             InlineKeyboardButton("Deportes ⚽", callback_data='sports')],
            [InlineKeyboardButton("Entretenimiento 🎬", callback_data='entertainment')]]

        self.reply_markup = InlineKeyboardMarkup(self.keyboard)

    def start(self, update, context) -> None:
        name = (update.message.chat.first_name + ' ' + update.message.chat.last_name
                if update.message.chat.last_name != None else update.message.chat.first_name)

        self.enviar_mensaje(context.bot, update.effective_user.id, f"Hola 👋🏻 *{name}* Pulsa un botón para comenzar",
                            parse_mode="Markdown", reply_markup=self.reply_markup)

    def menu_conf(self, update, context) -> None:
        name = (update.message.chat.first_name + ' ' + update.message.chat.last_name
                if update.message.chat.last_name != None else update.message.chat.first_name)

        self.enviar_mensaje(context.bot, update.effective_user.id,
                            f"Hola 👋🏻 *{name}* Pulsa un botón para comenzar", parse_mode="Markdown", reply_markup=self.reply_markup)

    def getNewMessage(self, update, context) -> None:
        """Función que se ejecuta cuando el usuario presiona un botón en el chat de Telegram."""
        query = update.callback_query
        query.answer()

        self.enviar_mensaje(context.bot, update.effective_user.id, f"Has seleccionado la categoría {self.case[query.data]}")
        news = self.getArticles(query.data)
        self.sendArticles(update, context, news)
        self.enviar_mensaje(context.bot, update.effective_user.id,
         (f"Pulsa un botón para ver más noticias 📰 de hoy {datetime.date.today().day}  de {datetime.date.today().strftime('%B')} de {datetime.date.today().year}."),
           reply_markup=self.reply_markup)
                
        
    def getMessage(self, article):
        return f"""📰 {self.getTitle(article)}\n{self.getDescription(article)}\n{self.getUrl(article)}\n{self.getImage(article)}\n\n©️ Autor: {self.getAuthor(article)}\n📅 Fecha: {self.getPublished(article)}"""

    def sendArticles(self, update, context, news):

        for article in news:
            try:
                self.enviar_mensaje(context.bot, update.effective_user.id, self.getMessage(article))
                sleep(2.5)         
                break       
            except Exception as e:
                print(e)
                continue
