import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app, Telegram
import random



@app.on_message(filters.regex("^تحميل$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين ياحلو\n-› هذي روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=Keyboard([
            [
               Button("- Instagram -", callback_data="instagram"),
               Button("- TikTok -", callback_data="tiktok")
            ],
            [
                Button("- Pintrest -", callback_data="pintrest"),
                Button("- Snapchat -", callback_data="snapchat")
            ],
            [
                Button("- YouTube - ", callback_data="youtube"),
                Button("- SoundCloud -", callback_data="soundcloud") # @BENN_DEV & @BENfiles
            ],
            [
                Button("- المطور -", url="BENN_DEV.t.me")
            ]
        ])
    )
