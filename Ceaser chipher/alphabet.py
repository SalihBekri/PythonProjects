import pandas

data = pandas.read_excel("data files/ALPHABETS.xlsx")


def get_lang_names() -> list:
    return list(data.columns.values)


def get_lang_info(lang) -> dict:
    """Returns a dictionary of both the letters and the number of them"""
    letters = list(data[lang].dropna().values)
    number_of_letters = len(letters)
    return dict(letters=letters, number_of_letters=number_of_letters)
