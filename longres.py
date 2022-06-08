import random


R_EATING = ["I don't like eating anything because I'm a bot obvisously!"]


def unknown():
    response = ['Cloud you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response
