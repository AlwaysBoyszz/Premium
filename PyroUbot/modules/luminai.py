from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʟᴜᴍɪɴᴀɪ"
__HELP__ = """
<blockquote><b>Bantuan Untuk bard-ai

perintah : <code>{0}lumin</code>
    dapat mengobrol</b></blockquote>
"""


@PY.UBOT("lumin")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .lumin query"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>menjawab....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.diioffc.web.id/api/ai/luminai?query={a}')

            try:
                if "result" in response.json():
                    x = response.json()[""]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
