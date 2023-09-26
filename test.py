import pyttsx3

engine = pyttsx3.init()    # Инициализировать голосовой движок.
voices = engine.getProperty('voices')

for voice in voices:    # голоса и параметры каждого
    print('------')
    print(f'Имя: {voice.name}')
    print(f'ID: {voice.id}')
    print(f'Язык(и): {voice.languages}')
    print(f'Пол: {voice.gender}')
    print(f'Возраст: {voice.age}')

# Имя: Microsoft Irina Desktop - Russian
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0
# Язык(и): []
# Пол: None
# Возраст: None
# ------
# Имя: Microsoft David Desktop - English (United States)
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
# Язык(и): []
# Пол: None
# Возраст: None
# ------
# Имя: Microsoft Zira Desktop - English (United States)
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# Язык(и): []
# Пол: None
# Возраст: None
# ------
# Имя: IVONA 2 Maxim OEM
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Maxim RSI Harpo 22kHz
# Язык(и): []
# Пол: None
# Возраст: None
# ------
# Имя: Vocalizer Expressive Katya Harpo 22kHz
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Vocalizer Expressive katya premium-high 22kHz
# Язык(и): []
# Пол: None
# Возраст: None
# PS C:\Users\ganiz\OneDrive\Рабочий стол\джарвис\assistant> 