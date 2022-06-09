import json
import re
import longres as lr

# Load JSOn data


def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' Successfully!")
        return json.load(bot_responses)


# Store json DATA
response_data = load_json('bot.json')


def get_response(input_string):
    split_message = re.split(r'\r+|[,;?!.-]\s', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response['required_words']

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required socre
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user have typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # add score to list
        score_list.append(response_score)
        # print(response_score, response['user_input'])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input empty
    if input_string == '':
        return 'Please type something so we can chat :'

    # If there is no good response, return a random one
    if best_response != 0:
        return response_data[response_index]['bot_response']

    return lr.random_string()


while True:
    user_input = input('You:')
    print('bot:', get_response(user_input))
