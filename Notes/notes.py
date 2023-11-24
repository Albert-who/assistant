import csv
import os
import main
import voice

NOTES = "notes.csv"

def readNotes():
    i = []
    if os.path.exists(NOTES):
        with open(NOTES, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                i.append(row)
    return i       

def writeNotes(note: str):
    with open(NOTES, 'a', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow([note])
        file.close()

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
            
        
if __name__ == '__main__':
    start()