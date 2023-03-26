from base import BotTelegram
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from BaseNewsAPI import BaseNewsAPI
from random import choice
import datetime

class BotTelegramNews(BotTelegram, BaseNewsAPI):
    def __init__(self, nombre, token, api_key, channel_id):
        BotTelegram.__init__(self, nombre, token)
        BaseNewsAPI.__init__(self, api_key)

        self.channel_id = channel_id
        self.meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        self.case = { 
            'business': 'negocios',  'entertainment': 'entretenimiento',
            'general': 'general' ,  'health': 'salud',
            'science': 'ciencia',  'sports': 'deportes', 
            'technology': 'tecnología'
        }
    
        self.keyboard = [[
            InlineKeyboardButton("Negocios 💰", callback_data='business'),
             InlineKeyboardButton("Tecnología 🤖", callback_data='technology'),
            InlineKeyboardButton("General 🌏", callback_data='general')],
            [InlineKeyboardButton("Salud ⚕", callback_data='health'),
             InlineKeyboardButton("Ciencia 🧪", callback_data='science'),
             InlineKeyboardButton("Deportes ⚽", callback_data='sports')],
            [InlineKeyboardButton("Entretenimiento 🎬", callback_data='entertainment')],
            [InlineKeyboardButton("Canal de deportes 🏀🥊🏎️", url='https://t.me/noticias_sport_mx')]
            ]
        self.reply_markup = InlineKeyboardMarkup(self.keyboard)

    def start(self, update, context) -> None:
        name = (update.message.chat.first_name + ' ' + update.message.chat.last_name
                if update.message.chat.last_name != None else update.message.chat.first_name)

        self.enviar_mensaje(context.bot, update.effective_user.id, (f"""Hola 👋🏻 *{name}*  estos son los comandos que puedes usar:\n\n/start - Iniciar el bot\n/menu - Mostrar el menú de categorías\n\n*NOTA:* Si quieres ver las noticias de una categoría en concreto, pulsa el botón correspondiente en el menú de categorías."""),parse_mode="Markdown")

    def menu_conf(self, update, context) -> None:
        name = (update.message.chat.first_name + ' ' + update.message.chat.last_name
                if update.message.chat.last_name != None else update.message.chat.first_name)
        self.enviar_mensaje(context.bot, update.effective_user.id,
         (f"Pulsa un botón para ver más noticias 📰 de hoy {datetime.date.today().day}  de {self.meses[datetime.date.today().month-1]} del año {datetime.date.today().year}"),
           reply_markup=self.reply_markup)
                

    def getNewMessage(self, update, context) -> None:
        """Función que se ejecuta cuando el usuario presiona un botón en el chat de Telegram."""
        query = update.callback_query
        
        self.enviar_mensaje(context.bot, update.effective_user.id, f"Has seleccionado la categoría {self.case[query.data]}")
        news = self.getArticles(query.data)
        try:
            article =choice(news)
            self.enviar_mensaje(context.bot, update.effective_user.id, self.getMessage(article))
            self.enviar_mensaje(context.bot, update.effective_user.id, f"¿Quieres ver más noticias de la categoría {self.case[query.data]}?", 
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Ver más noticias", callback_data=query.data)]]))
        except Exception as e:
            print(e)
            self.enviar_mensaje(context.bot, update.effective_user.id, "No hay más noticias para mostrar 😔")
        
    def getMessage(self, article):
        return f"""📰 {self.getTitle(article)}\n{self.getDescription(article)}\n{self.getUrl(article)}\n{self.getImage(article)}\n\n©️ Autor: {self.getAuthor(article)}\n📅 Fecha: {self.getPublished(article)}"""

    def sendSportNews(self):
        news = self.getArticles('sports')
        try:
            for article in news:
                self.enviar_mensaje_canal(self.channel_id, self.getMessage(article))
        except Exception as e:
            print(e)