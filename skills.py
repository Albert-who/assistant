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
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import main
import Notes.notes as notes
import Memories.memories as memories


my_joke = (
    'Вчера помыл окна, теперь у меня рассвет на два часа раньше...',
    'Почему жирафы так высоко поднимают шею? А они были бы иначе змеями...',
    'Что нужно, чтобы стать хорошим программистом? контрл плюс це, контрл плюс вэ.',
    'Не грусти, питон! Иногда и я не знаю, что делать.',
    'Что говорит программист на свидании? - Языки программирования меняются, но мой интерес к тебе - нет!',

    )

def micro():
      while True:
            data = main.micro(main.stream, main.rec)
            if data == 'конец':
                  return
      

def night_mode():
    # Получаем доступ к аудио-устройству (в данном случае, к динамикам)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    audio_volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Устанавливаем громкость на определенный уровень (0.0 - 1.0)
    audio_volume.SetMasterVolumeLevelScalar(0.5, None)

    # Установка громкости (значение от 0.0 до 1.0)

    # Устанавливаем яркость экрана (значение от 0 до 100)
    sbc.set_brightness(50)
    voice.speaker('Протокол активирован')

def day_mode():
    # Получаем доступ к аудио-устройству (в данном случае, к динамикам)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    audio_volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Устанавливаем громкость на определенный уровень (0.0 - 1.0)
    audio_volume.SetMasterVolumeLevelScalar(1.0, None)

    # Установка громкости (значение от 0.0 до 1.0)

    # Устанавливаем яркость экрана (значение от 0 до 100)
    sbc.set_brightness(100)
    voice.speaker('Протокол активирован')

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
            
def memorise():
    from Memories.memories import start
    start()

def remind():
    voice.speaker(f"Напоминаю {memories.readMemories()}")

def delMemories():
    from Memories.memories import startDel
    startDel()

def writeNotes():
    from Notes.notes import start
    start()

def delNotes():
    from Notes.notes import startDel
    startDel()

def readNotes():
    i = notes.readNotes()
    print(notes.readNotes())
    if len(i) != 0:
        voice.speaker(i)
    else: 
        voice.speaker("В заметках пусто")

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