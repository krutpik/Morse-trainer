import jstyleson

with open("settings.json") as write_file:
    json_string = jstyleson.load(write_file)

answers_time = json_string['answers_time']

pressed_dashes = json_string['pressed_dashes']

pressed_dot = json_string['pressed_dot']

language = json_string['language']

dash_song = json_string['dash_song']

with open("ABC.json") as ABC:
    json_string = jstyleson.load(ABC)

abc_ru = json_string['abc_ru']    

abc_en = json_string['abc_en']
