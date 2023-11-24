import csv
from datetime import datetime, timedelta, date
from Memories.extractor import NumberExtractor
from googletrans import Translator
import main
import voice
import os
import pandas as pd

NOTES = "memories.csv"

def readMemories():
    i = []
    if os.path.exists(NOTES):
        with open(NOTES, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                i.append(row)
            file.close()
    return i

def writeMemories(memo: str, dt: datetime):
    headers = ['Event', 'Date']
    if os.path.exists(NOTES):
        with open(NOTES, 'a', newline='', encoding='cp1251') as file:
            writer = csv.writer(file, delimiter = ';')
            writer.writerow([memo, dt])
            file.close()
    else: 
        with open(NOTES, 'a', newline='', encoding='cp1251') as file:
            writer = csv.writer(file, delimiter = ';')
            writer.writerow(headers)
            writer.writerow([memo, dt])
            file.close()

def delMemo(index: int):
    data = pd.read_csv(NOTES, on_bad_lines="skip", delimiter=";", encoding='cp1251')
    data = data.drop(data.index[index]).to_csv(NOTES, index=False, encoding='cp1251', sep=';')


def remindMe():
    if os.path.exists(NOTES):
        data = pd.read_csv(NOTES, on_bad_lines="skip", delimiter=";", encoding='cp1251')
        data["Date"] = pd.to_datetime(data["Date"])

        events = data.loc[(data["Date"].dt.date >= date.today()) & (data["Date"] <= (datetime.now() + timedelta(days = 1)))]["Event"].to_list()

        if len(events) > 0:
            message(f"События на ближайшее время: {events}")
        else:
            message("Нет предстоящих событий")


# Получение datetime
def getDateTime(data: str):
    dt = None
    translator = Translator()
    extractor = NumberExtractor()
    
    try:
        enDateTime = translator.translate(extractor.replace_groups(data), src='auto', dest='en')
        dt = datetime.strptime(enDateTime.text, '%B %d, %Y')
    except:
        print("Не получилось преобразовать в дату")
    return dt

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
    event = None
    while True:
        message("Что запоминать?")

        #получаем ответ
        data = get_answer()

        # Если не пусто, то запомнить
        if data != '':
            event = data
            break
        # Если стоп-слово, то выходим
        elif data in stop_words:
            break
            

    while True:
        #Month, day, year
        message("Назовите дату события") # Ex: Второе декабря две тысячи двадцать третьего года
        
        #получаем ответ
        data: str = get_answer()
        dt = getDateTime(data)
        
        try:
            # Если не пусто, то запомнить
            if data != '' and type(dt) is datetime:
                if dt >= datetime.now():
                    writeMemories(event, dt)
                    message(f"Записано на {dt}")
                    break
                else: 
                    message("Старая дата")
            # Если стоп-слово, то выходим
            elif data in stop_words:
                break
        except Exception as e:
            print(f"Обкек {e}")

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
                delMemo(i - 1)
                message("Забыл")
                break
            else:
                print("Не получилось")
        # Если стоп-слово, то выходим
        elif data in stop_words:
            break
        
if __name__ == '__main__':
    start()