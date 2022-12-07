import jstyleson

with open("settings.json") as write_file:
    json_string = jstyleson.load(write_file)

answers_time = json_string['answers_time']

pressed_dashes = json_string['pressed_dashes']

pressed_dot = json_string['pressed_dot']

language = json_string['language']
