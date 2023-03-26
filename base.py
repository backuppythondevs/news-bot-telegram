from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler
import logging

class BotTelegram:
    """Clase base para crear instancias de un Bot de Telegram
        >>> MiBot = BotTelegram(nombre, token)
    """

    def __init__(self, nombre, token):
        """Inicializa las variables básicas para que el bot de Telegram funcione."""
        # loggin: Sirve para enviar un registro de las actividades.
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(nombre)
        # Updater: es el encargado de contestar a los comandos que envíe el usuario.
        self.updater = Updater(token=token, use_context=True)
        # Polling se pone a la espera de que se ingresen comandos
        self.updater.start_polling()
        # Dispatcher: está al pendiente de todas las ventanas donde se encuentra el bot.
        self.dispatcher = self.updater.dispatcher
        
    def enviar_mensaje(self, bot, id_usuario, mensaje, parse_mode=None, reply_markup=None):
        """Función que envía un mensaje desde un bot y a un usuario en particular.
        Parámetros:
            bot: objeto Bot de el módulo telegram.
                Tipo: telegram.bot
            usuario: id de telegram del usuario.
                Tipo: (int)
            text: mensaje a enviar.
                Tipo: (str)
            parse_mode: establece como se 'parsea' el texto enviado.
                Tipo: (str)
                Ejm: 'Markdown'; 'HTML'.
            """
        bot.send_message(chat_id=id_usuario, text=mensaje, parse_mode=parse_mode,reply_markup=reply_markup)

    def esperar_comando(self, comando, function):
        """
        Función que espera que se ingrese en el chat el comando y ejecuta la función que se ingresen como parámetro.
        Parámetros:
            comando: texto que colocará el usuario acompañado de una barra '/' en el chat de Telegram..
                Tipo: (str)
                Ejemplo: 'start'
            function: función que se ejecutará cuando el usuario realice determinado comando.
                Tipo: (fn)
        """
        self.dispatcher.add_handler(CommandHandler(comando, function))
          
    def contestar_consulta(self, function):
        """Función que espera que el usuario presione un botón que se despliega en el chat de telegram y ejecuta la
        función que se pase como parámetro.
        Parámetro:
            función: función que se ejecuta al presionar un botón (InlineKeyboardButton) en el chat.
                Tipo: (fn)"""
        self.dispatcher.add_handler(CallbackQueryHandler(function))
    
    def contestar_mensaje(self, function):
        """ Espera cualquier cosa en el chat que no sea un comando (mensajes) y ejecuta la función que se pase como
            parámetro.
        Parámetro:
        función: función que se ejecuta al recibir un mensaje en el chat.
            Tipo:: (fn)"""
        mensaje_recibido = MessageHandler(Filters.text & (~Filters.command), function)
        self.dispatcher.add_handler(mensaje_recibido)

    def enviar_mensaje_canal(self, id_canal, mensaje, parse_mode=None, reply_markup=None):
        """Función que envía un mensaje desde un bot y a un canal en particular.
        Parámetros:
            bot: objeto Bot de el módulo telegram.
                Tipo: telegram.bot
            id_canal: id de telegram del canal.
                Tipo: (int)
            text: mensaje a enviar.
                Tipo: (str)
            parse_mode: establece el modo de texto que se envía.
                Tipo: (str)
                Ejm: 'Markdown'; 'HTML'.
            """
        self.updater.bot.send_message(chat_id=id_canal, text=mensaje, parse_mode=parse_mode,reply_markup=reply_markup)
