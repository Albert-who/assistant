import os
import webbrowser
import sys
import subprocess
import keyboard
import apikey
#import pyautogui
import random
import voice
import requests
import json
import num_text
import wikipedia
#import speedtest
# from yandex_music import Client
# client = Client('token').init()
# client.users_likes_tracks()[0].fetch_track()

my_joke = (
    'Вчера помыл окна, теперь у меня рассвет на два часа раньше...',
    'Почему жирафы так высоко поднимают шею? А они были бы иначе змеями...',
    'Что нужно, чтобы стать хорошим программистом? контрл плюс це, контрл плюс вэ.',
    'Не грусти, питон! Иногда и я не знаю, что делать.',
    'Что говорит программист на свидании? - Языки программирования меняются, но мой интерес к тебе - нет!',

    )

def music():
      pass


def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.youtube.com', new=2)	

def joke():
    voice.speaker(random.choice(my_joke))  

def game():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''
	try:
		subprocess.Popen(r'C:\Users\ganiz\Microsoft VS Code\Code.exe')
	except:
		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def open_presentation():
    '''Открыть презентацию'''
    try:
        os.startfile(r'C:\Users\ganiz\OneDrive\Рабочий стол\assistant\Вокси.pptx')
        # time.sleep(5) # ожидание открытия презентации
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')
	
def close_presentation():
    '''Закрыть презентацию'''
    try:
        os.system('taskkill /f /im POWERPNT.EXE')
    except:
        voice.speaker('Не удалось закрыть презентацию')

def next_slide():
    '''Перейти на следующий слайд'''
    #try:
        #pyautogui.press('right')
    #except:
	#    voice.speaker('Похоже тебе самому придется перелестнуть слайд')

def previous_slide():
    '''Перейти на предыдущий слайд'''
    #try:
        #pyautogui.press('left')
    #except:
	#    voice.speaker('Похоже тебе самому придется вернуть слайд')

def start_slideshow():
    '''Запустить режим демонстрации'''
    #try:
    #    pyautogui.press('f5')
	    
    #except:
    #    voice.speaker('У меня не получилось включить режим демонстрации')

def stop_slideshow():
    '''Остановить режим демонстрации'''
    #try:
    #    pyautogui.press('esc')
	    
    #except:
	#    voice.speaker('У меня не получилось выключить режим демонстрации')


def speak():
	pass


def offpc():
	#Эта команда отключает ПК под управлением Windows

	# os.system(r'shutdown /s')
	
	print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
	try:
		params = {'q': 'Novokuznetsk', 'units': 'metric', 'lang': 'ru', 'appid': apikey.Api}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		# voice.speaker(random.choice(['сейчас скажу', 'один момент, сейчас проверю', 'сейчас гляну', 'сейчас посмотрю', 'можешь посмотреть на градусник, но сейчас я сам проверю']))
		voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	except:
		voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
	'''Отключает бота'''
	sys.exit()


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def check_internet_speed():
    #st = speedtest.Speedtest()
    download_speed = 0 #st.download() / 1000000 # скорость загрузки в мегабайтах в секунду
    upload_speed = 0 #st.upload() / 1000000 # скорость выгрузки в мегабайтах в секунду
    ping = 0 #st.results.ping # пинг
    print(f"Скорость загрузки: {download_speed:.2f} Мб/с")
    print(f"Скорость выгрузки: {upload_speed:.2f} Мб/с")
    print(f"Пинг: {ping} мс")

check_internet_speed


def calc(datas):
    try:
        datas = datas.replace(' сколько будет ', '')
        math_opers = ['плюс', 'прибавить', 'минус', 'вычесть', 'умножить на', 'делить на']
        oper =''
        for i in math_opers:
            if i in datas:
                if oper != '':
                     print('Ошибка: слишком много операторов')
                     voice.speaker('я могу выполнить только одно действие')
                     return
                oper = i
        
        if oper == '':
            voice.speaker('я вас не расслышала')
            print('я вас не расслышала')
            return
        
        num1 = num_text.str_to_num(datas.split(' '+oper+' ')[0])
        num2 = num_text.str_to_num(datas.split(' '+oper+' ')[1])
        result = 0
        match oper:
            case 'плюс' | 'прибавить': result = num1 + num2
            case 'минус' | 'вычесть': result = num1 - num2
            case 'умножить на': result = num1 * num2
            case 'делить на':
                    if num2 != 0:
                        result = num1 // num2
                    else:
                        voice.speaker('ошибка, деление на ноль')
                        print('ошибка, деление на ноль')
                        return
        
        voice.speaker('будет '+num_text.num_to_str(result))
        print('будет '+num_text.num_to_str(result))
    except:
        voice.speaker('повторите запрос')
        print('повторите запрос')


def gen_some_number():
    phrases = ['пусть будет', 'например', '', 'я загадала']
    number = random.randint(1, 100)
    
    result = phrases[random.randint(0, len(phrases)-1)] + ' ' + str(number)
    print(result)
    voice.speaker(result)
    

def gen_some_name():
    phrases = ['пусть будет', 'например', '', 'я загадала']
    fnames = open('desktop/assistant-main/names.txt', 'r')
    index = random.randint(0, 493)
    for i in range(index):
        fnames.readline()
    name = fnames.readline().split('\n')[0]
    fnames.close()
    result = phrases[random.randint(0, len(phrases)-1)]+name
    print(result)
    voice.speaker(result)


def who_is_it():
    from main import get_string
    try:
        data = get_string()
        gender = ''
        if 'кто такой' in data:
            gender = 'male'
        else:
            gender = 'female'
        data = data.replace(' кто такой ', '').replace(' кто такая ', '')
        result = wikipedia.summary(data, sentences=4)
        if gender == 'female':
            result = result.replace('род.', 'родилась')
        else:
            result = result.replace('род.', 'родился')
        if result == None:
            print('джарвис: я ничего не нашла по вашему запросу')
            voice.speaker('я ничего не нашла по вашему запросу')
            return
        print(result)
        voice.speaker(result)
    except:
        print('джарвис: я вас не поняла')
        voice.speaker('я вас не поняла')

wikipedia.set_lang('ru')

def get_dollar_cost():
    #url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE &from_currency=USD &to_currency=RUB &apikey=9NZ3WF59OUSSNOGB"
    data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=9NZ3WF59OUSSNOGB&q=USD_RUB&compact=ultra').json()
    print (data)


def run_cities():
    from cities import start
    start()


def whats_time():
    import datetime
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    hour_end = ''
    minute_end = ''
    if hour in range(5, 19):
         hour_end = 'ов'
    elif hour % 20 > 1:
         hour_end = 'a'

    if (minute % 10 == 1) & (minute != 11):
        minute_end = 'а'
    elif (minute % 10 < 5) & (minute not in range(10, 15)):
        minute_end = 'ы'

    print(F'джарвис: сейчас {hour}:{minute}')
    voice.speaker(F'сейчас {hour} час{hour_end}, {minute} минут{minute_end}')

def run_akinator():
    from my_akinator import start
    start()
