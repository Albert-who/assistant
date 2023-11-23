import pyttsx3	


engine = pyttsx3.init()
# id
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Vocalizer Expressive yuri premium-high 22kHz'
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 160)				#скорость речи

# engine.say('и тебе привет')
# engine.runAndWait()

def speaker(text):
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()


# второй вариант синтеза

# import torch
# import sounddevice as sd


# # Загрузка модели и выбор языка
# language = "ru"
# model_id = "v3_1_ru"
# device = torch.device("cpu")
# model, example_text = torch.hub.load(repo_or_dir="snakers4/silero-models",
#     								model="silero_tts",
#     								language=language,
#     								speaker=model_id,
# 									)
# model.to(device)

# # Синтез речи
# sample_rate = 48000
# speaker = 'baya' # ['aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random']
# put_accent=True
# put_yo=True
# example_text = 'В недрах тундры выдры в г+етрах т+ырят в вёдра ядра к+едров.'



# def speaker(texts):
# 	'''Озвучка текста'''
# 	audio = model.apply_tts(text=texts,
#                         speaker='baya',
#                         sample_rate=48000,
#                         # put_accent=True,
#                         # put_yo=True,
# 						)
# 	sd.play(audio, 48000)
# 	sd.wait()