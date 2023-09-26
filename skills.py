import os
import webbrowser
import sys
import subprocess
import keyboard
import apikey
import pyautogui
import random
import voice
import requests	
import speedtest
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
    try:
        pyautogui.press('right')
    except:
	    voice.speaker('Похоже тебе самому придется перелестнуть слайд')

def previous_slide():
    '''Перейти на предыдущий слайд'''
    try:
        pyautogui.press('left')
    except:
	    voice.speaker('Похоже тебе самому придется вернуть слайд')

def start_slideshow():
    '''Запустить режим демонстрации'''
    try:
        pyautogui.press('f5')
	    
    except:
        voice.speaker('У меня не получилось включить режим демонстрации')

def stop_slideshow():
    '''Остановить режим демонстрации'''
    try:
        pyautogui.press('esc')
	    
    except:
	    voice.speaker('У меня не получилось выключить режим демонстрации')


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
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000 # скорость загрузки в мегабайтах в секунду
    upload_speed = st.upload() / 1000000 # скорость выгрузки в мегабайтах в секунду
    ping = st.results.ping # пинг
    print(f"Скорость загрузки: {download_speed:.2f} Мб/с")
    print(f"Скорость выгрузки: {upload_speed:.2f} Мб/с")
    print(f"Пинг: {ping} мс")

check_internet_speed