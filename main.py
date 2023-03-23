from news_bot import BotTelegramNews
from keys import TOKEN_API_TELEGRAM,API_NEW_TOKEN


if __name__ == '__main__':
    bot = BotTelegramNews('NewsBot', TOKEN_API_TELEGRAM, API_NEW_TOKEN)
    bot.esperar_comando("start", bot.start)
    bot.esperar_comando("menu", bot.menu_conf)
    bot.contestar_consulta(bot.getNewMessage)
   
    
   