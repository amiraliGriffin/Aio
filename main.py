from pyrogram import Client

plug = dict(root="plugins")

bot = Client(
    name = "AIO",
    api_id = 29585063,
    api_hash = "7cbc271846d81539d10bdec6cf36ba6a",
    bot_token = "6916934962:AAFX076YtdvOh0rUEi4cDzn6enxvaSyVKEY",
    plugins = plug
)

bot.run()