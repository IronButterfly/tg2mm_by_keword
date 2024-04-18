# Description
Telegram Bot to publish messages with the specified keywords from your Telegram Chat to your Mattermost Channel.

Please replace:

'YOUR_TELEGRAM_BOT_TOKEN',
'YOUR_MATTERMOST_URL', 
'YOUR_MATTERMOST_LOGIN_ID', 
'YOUR_MATTERMOST_PASSWORD ' and 
'YOUR_MATTERMOST_CHANNEL_ID' 

with the appropriate values. You can also change the keywords list to your keywords.

# Prerequisites
To correct work, you have to install the following Python libraries:
```
pip install pyTelegramBotAPI mattermostdriver
```
**Note:** The script doesn't work if you have 2FA enabled for Mattermost.
