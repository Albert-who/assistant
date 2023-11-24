import csv
import os
import main
import voice
import pandas as pd
from Memories.extractor import NumberExtractor

NOTES = "notes.csv"

def readNotes():
    i = []
    if os.path.exists(NOTES):
        with open(NOTES, newline="", encoding='cp1251') as file:
            reader = csv.reader(file)
            for row in reader:
                i.append(row)
    return i       

def writeNotes(note: str):
    with open(NOTES, 'a', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow([note])
        file.close()

def delNote(index: int):
    data = pd.read_csv(NOTES, on_bad_lines="skip", delimiter=";", encoding='cp1251')
    data = data.drop(data.index[index]).to_csv(NOTES, index=False, encoding='cp1251')


# Получение datetime
def getNum(data: str):
    i: int = 0
    extractor = NumberExtractor()
    
    try: 
        i = extractor.replace_groups(data)
    except:
        print("Не получилось преобразовать в число")
    return i

#вывести сообщение в консоль и произнести его
def message(msg):
    print('джарвис:', msg)
    voice.speaker(msg)

def get_answer():
    data = None
    while data == None:
        data = main.get_string()
    return data

def start():
    stop_words = ['стоп', 'хватит', 'прекрати', 'давай закончим']
    while True:
        message("Достаю ручку")

        #получаем ответ
        data = get_answer()

        # Если не пусто, то запомнить
        if data != '':
            writeNotes(data)
            message("Записал")
            break
        # Если стоп-слово, то выходим
        elif data in stop_words:
            break

def startDel():
    stop_words = ['стоп', 'хватит', 'прекрати', 'давай закончим']
    while True:
        # message("Что будем удалять? Назовите номер записи")
        message("Что будем удалять?")

        #получаем ответ
        data = get_answer()

        # Если не пусто, то запомнить
        if data != '':
            index = getNum(data)
            i = 0
            try:
                i = int(index)
            except:
                print("Не удается преобразовать в int")

            if i > 0:
                delNote(i - 1)
                message("Зачеркнул")
                break
            else:
                print("Не получилось")
        # Если стоп-слово, то выходим
        elif data in stop_words:
            break
            
        
if __name__ == '__main__':
    start()