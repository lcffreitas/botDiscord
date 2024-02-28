from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled a {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What do you mean?',
                       'I\'m not sure what you\'re asking for...',
                       'I\'m sorry, I don\'t understand that...',
                       'I don\'t know what you\'re talking about...'])
