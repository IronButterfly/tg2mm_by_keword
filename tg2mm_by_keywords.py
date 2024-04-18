import telebot
from mattermostdriver import Driver

# Setting up a Telegram bot
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Setting up the Mattermost driver
mm = Driver({
    'url': 'YOUR_MATTERMOST_URL',
    'login_id': 'YOUR_MATTERMOST_LOGIN_ID',
    'password': 'YOUR_MATTERMOST_PASSWORD',
    'scheme': 'https',
    'port': 443,
    'basepath': '/api/v4',
    'verify': True
})

# Keyword list
keywords = ['key word 1', 'key word 2', 'key word 3']

@bot.message_handler(func=lambda message: any(keyword in message.text for keyword in keywords))
def send_to_mattermost(message):
    # Connection to Mattermost
    mm.login()
    
    # Creating a link to a message in Telegram
    chat_id = message.chat.id
    message_id = message.message_id
    invite_link = bot.export_chat_invite_link(chat_id)
    message_link = f"{invite_link}/{message_id}"
    
    # Sending a message and a link to the message to the Mattermost channel
    mm.posts.create_post({
        'channel_id': 'YOUR_MATTERMOST_CHANNEL_ID',
        'message': f"{message.text}\n\nLink: {message_link}"
    })
    
    # Disconnecting from Mattermost
    mm.logout()

# Launching a Telegram bot
bot.polling()
