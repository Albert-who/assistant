import main
import pandas

def message(msg):
    print('джарвис:', msg)
    voice.speaker(msg)

def start():
    data = ''
    stop_words = ['стоп', 'хватит', 'прекрати', 'давай закончим', 'я не знаю', 'я проиграл']
    cities_data = list(pandas.read_csv('cities.csv', encoding='cp1251').города)
    said_cities = []
    bad_symbols = ['й', 'ц', 'ы', 'ь']
    now_sym = None

    while True:
        while True:
            data = main.get_string()
            if data:
                    break
        #print('пользователь:', data)

        if data in stop_words:
            break

        if (len(data.split()) > 1) & (data not in cities_data):
            message('я вас не расслышала')
            continue

        if data in said_cities:
            message('этот город уже был')
            continue

        if now_sym != None:
            if (data[0] != now_sym):
                message('этот город начинается на другую букву')
                continue

        if data not in cities_data:
            message('я не знаю такой город')
            continue

        said_cities.append(data)

        if random.randint(0, 100) == 2:
            message('я сдаюсь')
            break
            
        n = -1
        while data[n] in bad_symbols:
            n -= 1

        words = []
        for i in cities_data:
            if (i[0] == data[n]) & (i not in said_cities):
                words.append(i)

        if len(words) == 0:
            message('я не знаю других городов, вы выиграли')
            break

        sel_word = words[random.randint(0, len(words)-1)]
        message(sel_word)
        said_cities.append(sel_word)

        n = -1
        while sel_word[n] in bad_symbols:
            n -= 1
        now_sym = sel_word[n]
        voice.speaker('тебе на '+now_sym)

if __name__ == '__main__':
    import random
    import voice
    start()