

def encode(shift: int, text: str, language_information: dict) -> str:
    new_text = ""
    for i in text:
        if i in language_information["letters"]:
            position = language_information["letters"].index(i)
            new_position = position + shift
            if new_position >= len(language_information["letters"]):
                new_position = new_position % language_information["number_of_letters"]
            new_letter = language_information["letters"][new_position]
            new_text += new_letter
        else:
            new_text += i
    return new_text


def decode(shift: int, text: str, language_information: dict) -> str:
    new_text = ""
    for i in text:
        if i in language_information["letters"]:
            position = language_information["letters"].index(i)
            new_position = position - shift
            if abs(new_position) >= len(language_information["letters"]):
                new_position = -(abs(new_position) % language_information["number_of_letters"])
            new_letter = language_information["letters"][new_position]
            new_text += new_letter
        else:
            new_text += i
    return new_text
