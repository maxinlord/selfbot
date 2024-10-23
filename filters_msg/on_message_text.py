from pyrogram import filters


def filter_by_definite_text(text: str = None):
    async def func(flt, client, update):
        if flt.text is None:
            return True
        return flt.text == update.text

    return filters.create(func, text=text)

def filter_by_contains_text(text: str = None):
    async def func(flt, client, update):
        if flt.text is None:
            return True
        return flt.text in update.text

    return filters.create(func, text=text)