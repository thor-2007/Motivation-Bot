## A silly motivational bot made with python using Telegram. 
## This is a customizable bot that writes motivational quotes whenever you want in Norwegian to send to yourself on Telegram on phone for example as a way of notifying!



Steps to make it work:

1. Install Telegram from Google or whatever...

## Creating our bot and getting our Token:
  
3. Search inside Telegram for @BotFather
4. Type to @BotFather "/start"
5. Type to @BotFather "/newbot"
6. Follow the steps it gives...
7. Copy the Token it gives you, either write it in the input later, or remove the input fully from the code and paste the Token there.
8. Click on the name of the Bot you made from @BotFather's message.
9. Type to your new bot "/start", and write afterwards "hello" or anything.


## Now to get our Chat ID for a Private Chat:

1. Search and open our new Telegram bot
1. Click Start or send a message
1. Open this URL in a browser `https://api.telegram.org/bot{our_bot_token}/getUpdates`   
    - See we need to prefix our token with a word `bot`
    - Eg: `https://api.telegram.org/bot63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c/getUpdates`
1. We will see a json like so
    ```
    {
      "ok": true,
      "result": [
        {
          "update_id": 83xxxxx35,
          "message": {
            "message_id": 2643,
            "from": {...},
            "chat": {
              "id": 21xxxxx38,
              "first_name": "...",
              "last_name": "...",
              "username": "@username",
              "type": "private"
            },
            "date": 1703062972,
            "text": "/start"
          }
        }
      ]
    }
    ```
Check the value of `result.0.message.chat.id`, and here is our Chat ID: `21xxxxx38` in this example...
Save the Chat Id somewhere for later use.
## When you run the python file it will ask for the Token and the chat id. Just put those in and the program should work. 

Optional:
If you want to avoid having to input all the time, change this on line 291 & 292:
```
bot_token = input("Skriv inn din Telegram bot token: ")
chat_id = input("Skriv inn Telegram chat ID for å sende meldinger: ")
```
Into this and paste the token and id into the parenthesis:
```
bot_token = "PASTE YOUR TOKEN IN HERE"
chat_id = "PASTE YOUR CHAT ID IN HERE"
```

Now you don't need to paste into the terminal everytime you run the program!
