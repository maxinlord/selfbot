import language_tool_python


def leapfrog_letters(text: str, start: int = 0):
    # Если start четная цифра то начало с верхнего регистра, если не четная то с нижнего регистра
    t = ""
    for idx, i in enumerate(text, start=start):
        if idx % 2 == 0:
            t += i.upper()
        else:
            t += i
    return t


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text  # or whatever


text_correct_tool = language_tool_python.LanguageTool("ru")

