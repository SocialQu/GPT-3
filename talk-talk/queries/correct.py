from .utils import parseText
import openai


def correct(reply):
    completion = openai.Completion.create(
        engine='curie',
        prompt='Original:' + reply + '\nEspañol Correcto:',
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['\n']
    )

    text = parseText(completion)
    print('Text:', text)

    return text
