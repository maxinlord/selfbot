import asyncio

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from filters_msg import filter_by_contains_text
from funcs import (
    animation_flash_text,
    animation_leapfrog_letters,
    remove_prefix,
    text_correct_tool,
)

api_id = 24530550
api_hash = "ac097ceda5d6dece7ed542347c301e04"
app = Client("BotHelper", api_hash=api_hash, api_id=api_id)


@app.on_message(filters=filter_by_contains_text("!flash"))
async def flash_base(client: Client, message: Message):
    message.text = remove_prefix(message.text, prefix="!flash")
    await animation_flash_text(message=message)


@app.on_message(filters=filter_by_contains_text("!emoji"))
async def emoji(client: Client, message: Message):
    message.text = remove_prefix(message.text, prefix="!emoji")
    await animation_flash_text(message=message, split_by="", time_sleep=2.0)


@app.on_message(filters=filter_by_contains_text("!frog"))
async def frog(client: Client, message: Message):
    message.text = remove_prefix(message.text, prefix="!emoji")
    await animation_leapfrog_letters(message=message, run_time=5)


@app.on_message(filters=filter_by_contains_text("!c"))
async def correct_text(client: Client, message: Message):
    message.text = remove_prefix(message.text, prefix="!c")
    matches = text_correct_tool.check(message.text)
    if not matches:
        return await message.edit(message.text)
    for match in matches:
        await client.send_message(
            chat_id="me",
            text=f"Ошибка: {match.message}\n\nИсправление: {match.replacements}",
        )
        await asyncio.sleep(1)
    await client.send_message(
        chat_id="me",
        text=f"Исходный текст: <code>{message.text}</code>",
        parse_mode=ParseMode.HTML,
    )
    corrected_text = text_correct_tool.correct(message.text, matches)
    await message.edit(corrected_text)


if __name__ == "__main__":
    app.run()
