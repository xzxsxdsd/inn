import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic.utils.decorators.admins import AdminActual
from strings import get_command




def tiktok(url):
    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',# @BENN_DEV & @BENfiles
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
    	'id': url,
    	'locale': 'en',
    	'tt': 'VG5CYm1h',
	}
  
    response = requests.post('https://ssstik.io/abc', headers=headers, data=data).text
    try:
        title = response.split('"maintext">', 1)[1].split("<", 1)[0]
    except IndexError:
        return { "success" : False }
    urls = response.split('<div class="flex-1 result_overlay_buttons pure-u-1 pure-u-sm-1-2">')[1]
    a_voice = urls.split('<a href="')[2]
    voice = a_voice.split('"')[0]
    a_video = urls.split('<a href="')[1]
    video = a_video.split('"')[0]
    result = {"mp4" : video, "mp3" : voice, "title" : title, "id" : url.rsplit("/", 1)[0], "success": True}
    
    return result
     
  
@app.on_message(filters.command(["تيك"],""))
async def ihd(client: Client, message: Message):
    user_id = callback.message.from_user.id
    caption = "يمكنك ارسال الرابط الآن."
    answer = await callback.message.chat.ask(text=caption)
    await client.delete_messages(user_id, answer.id)
    await answer.request.edit_text("Processing...")
    url = answer.text
    response = tiktok(url)
    if not response["success"] :
        await answer.request.delete()
        await answer.reply(
            "الرابط غير صالح",
        )
        return # @BENN_DEV & @BENfiles
    urllib.request.urlretrieve(response["mp4"], f"{response['title']}.mp4")
    bot = await client.get_me ()
    bot_name = bot.first_name
    bot_url = f"{bot.username}.t.me"
    markup = Keyboard([
        [
            Button("- تحميل الصوت-", callback_data=f"tiktokaudio_{response['id']}")
        ]
    ])
    caption = f"title : {response['title']}\n\n● Uploaded By : [{bot_name}]({bot_url})"
    await answer.reply_document(
        document=f"{response['title']}.mp4", 
        caption=caption,
        reply_markup=markup
    )
    await answer.request.delete()
