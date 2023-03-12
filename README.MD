# Bot de telegram de noticias de México

Este es un bot de Telegram que te mantiene al día con las últimas noticias. Este bot utiliza la [API de noticias](https://newsapi.org/) para obtener los titulares más recientes y enviártelos directamente a través de Telegram.


## ¿Qué es News API?
> News API es una API de noticias que te permite buscar y obtener noticias de todo el mundo. Puedes buscar noticias por categoría, fuente, idioma, país y más. Puedes obtener noticias en tiempo real y noticias de hace varios días. Puedes obtener noticias de fuentes como CNN, BBC News, The New York Times, The Washington Post, The Wall Street Journal, The Guardian, The Times of India, The Hindu, The Telegraph, The Sydney Morning Herald, The Age, The Australian, The Daily Telegraph, The Daily Mail, The Daily Mirror, The Daily Express, The Daily Star, The Daily Record, The Daily Telegraph, The Dai



## Instalación y configuración
> Para instalar este bot, necesitas tener instalado Python 3.6 o superior. Puedes descargar Python desde [aquí](https://www.python.org/downloads/).

1. haz un fork de este repositorio y clona el repositorio en tu computadora.
2. Crea un entorno virtual.
```bash
pip install virtualenv

# Linux
source virtualenv nombre_del_entorno
source nombre_del_entorno/bin/activate
```
3. Ejecuta el siguiente comando en tu terminal:
> Este comando instalará todas las dependencias necesarias para ejecutar el bot.
```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes variables de entorno:
> Puedes obtener una API KEY de [News API](https://newsapi.org/) registrándote en su sitio web y creando una cuenta gratuita. Para generar el API KEY de Telegram, puedes crear un bot de Telegram y obtener su API KEY con el [BotFather](https://t.me/botfather).

```bash
# API KEY de News API
TELEGRAM_TOKEN_API=TU_BOT_API_KEY
API_NEW_TOKEN=API_KEY_DE_NEWS_API
```
5. Ejecuta el archivo `main.py` para iniciar el bot.

## ¿Cómo funciona?
> El bot se conecta a la API de noticias así mismo obtiene los titulares más recientes y envía los titulares a través de Telegram.

1. Busca el bot en Telegram [@newsMX_bot](https://t.me/newsMX_bot).
2. Envía el comando /start para iniciar el bot.
3. El bot te enviará una lista de categorías de noticias.
4. Elige la categoría que te interesa.
5. El bot te enviará los titulares de la categoría que elegiste.
6. Si quieres ver de nuevo el menú de las categorías, escribe el comando /menu.


## ¿Cómo puedo contribuir?
> Si quieres contribuir a este proyecto, puedes hacerlo de varias maneras.
1. Puedes hacer un fork de este repositorio y hacer un pull request.
2. Puedes reportar un bug o sugerir una mejora en la sección de issues.
3. Puedes hacer una donación para apoyar el desarrollo de este bot.



## ¿Cómo puedo hacer una donación?
> Puedes hacer una donación a través de [PayPal](https://paypal.me/pythondevs?country.x=MX&locale.x=es_XC).


## Licencia
> Este proyecto está bajo la licencia MIT. Puedes ver el archivo LICENSE para más detalles.