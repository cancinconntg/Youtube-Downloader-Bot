from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Şu anda yalnızca Youtube Single'ı destekliyor (Çalma listesi yok) Sadece Youtube Url'si Gönder"
    await message.reply_text(helptxt)
