from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import sounddevice as sd
import vosk
import json
import queue
import words
from skills import *
import voice
import datetime
import webrtcvad
import pyaudio
import librosa
import numpy as np

vad = webrtcvad.Vad(3)  # создаем экземпляр класса для подавления шума
audio = pyaudio.PyAudio()
FLAG =True 
q = queue.Queue()
model = vosk.Model('model_small')
device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

def recognize(data, vectorizer, clf):
    '''
    Анализ распознанной речи
    '''
    try: 
        # проверяем есть ли имя бота в data, если нет, то return
        trg = words.TRIGGERS.intersection(data.split())
        if not trg:
            return

        # удаляем имя бота из текста
        data = data.replace(list(trg)[0], '')

        if data != '':
            global FLAG
            FLAG = False
            # получаем вектор полученного текста
            # сравниваем с вариантами, получая наиболее подходящий ответ
            text_vector = vectorizer.transform([data]).toarray()[0]
            # print(text_vector, '\n', len(text_vector), sum(text_vector))
            if sum(text_vector) == 0:
                FLAG = False
                voice.speaker('Я Вас не понимаю, повторите еще раз')
                FLAG = True
                return
            answer = clf.predict([text_vector])[0]
            # print(answer)
            # получение имени функции из ответа из data_set
            func_name = answer.split()[0]

            # озвучка ответа из модели data_set
            
            voice.speaker(answer.replace(func_name, ''))
            # print(func_name)

            # запуск функции из skills
            exec(func_name + '()')  

            FLAG = True          
        else: 
            FLAG= False
            voice.speaker('Я слушаю')
            FLAG=True

    except Exception as e:
        print('Ошибка при обработке распознанной речи:', e)


stream = audio.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, 
                            frames_per_buffer=8192)#, stream_callback=callback   
rec = vosk.KaldiRecognizer(model, samplerate)

def micro(stream, rec):
    # stream.start_stream()       
    data = stream.read(8192)
    if rec.AcceptWaveform(data) :
        data = json.loads(rec.Result())['text']
        print('распознано:', data)
        return data
    
def get_string():
    return micro(stream, rec)

def main():
    '''
    Обучаем матрицу ИИ и постоянно слушаем микрофон
    '''
    try:
        # Обучение матрицы на data_set модели
        vectorizer = CountVectorizer()
        vectors = vectorizer.fit_transform(list(words.data_set.keys()))
        clf = LogisticRegression()
        clf.fit(vectors, list(words.data_set.values()))

        del words.data_set

        now = datetime.datetime.now()

        if now.hour >= 6 and now.hour < 12:
            voice.speaker("Доброе утро!")
        elif now.hour >= 12 and now.hour < 18:
            voice.speaker("Добрый день!")
        elif now.hour >= 18 and now.hour < 23:
            voice.speaker("Добрый вечер!")
        else:
            voice.speaker("Доброй ночи!")
        
        memories.remindMe()

        # stream = audio.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, 
        #                     frames_per_buffer=8192)#, stream_callback=callback   
       
        # rec = vosk.KaldiRecognizer(model, samplerate)
        stream.start_stream()
        
        # while True:
        #     data = stream.read(8192)
        #     if rec.AcceptWaveform(data) :
        #         data = json.loads(rec.Result())['text']
        #         print('распознано:', data)
        #         recognize(data, vectorizer, clf)
        while True:
            data = micro(stream, rec)
            if data:
                recognize(data, vectorizer, clf)
                    
                    
    except Exception as e:
        print('Произошла ошибка:', e)

if __name__ == '__main__':
    main()
