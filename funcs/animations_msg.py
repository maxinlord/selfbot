from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
import asyncio
import asyncio
import funcs


async def animation_leapfrog_letters(message: Message, run_time: int = 3):
    text = message.text
    try:
        for i in range(run_time):
            await message.edit_text(text=funcs.leapfrog_letters(text=text, start=i))
            await asyncio.sleep(1)
    except MessageNotModified:
        return
    except Exception as e:
        print(e)
    return await message.edit_text(text=text)


async def animation_flash_text(
    message: Message,
    split_by: str = None,
    time_sleep: float = 0.5,
):
    text = message.text
    if split_by == "":
        text_list = [i for i in text]
    else:
        text_list = text.split(split_by)
    for i in text_list:
        try:
            await message.edit_text(text=i)
            await asyncio.sleep(time_sleep)
        except MessageNotModified:
            continue
        except Exception as e:
            print(e, text)
    return await message.edit_text(text=text)
