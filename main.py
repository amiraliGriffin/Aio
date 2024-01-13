from pyrogram import Client

plug = dict(root="plugins")

bot = Client(
    name = "AIO",
    api_id = 29585063,
    api_hash = "7cbc271846d81539d10bdec6cf36ba6a",
    bot_token = "6369104750:AAHB8bcyMTY1nXOKgn6a4Psm8CXj-yjtFog",
    plugins = plug
)

bot.run()