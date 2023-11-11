import pandas
import random
import main
import voice

#чтение таблиц из файлов
def load_bases():
        #persons = pandas.read_csv('desktop/assistant-main/big_scary_db.csv', sep=';')
        persons = pandas.read_csv('big_scary_db.csv', sep=';')
        questions = {}
        #file = open('desktop/assistant-main/db_questions.txt', 'r')
        file = open('db_questions.txt', 'r')
        for i in file.readlines():
            questions[i.split('|')[0]] = i.split('|')[1].replace('\n','')
        file.close()
        return persons, questions

#предлог сыграть заново
def try_again():
    message('я не знаю подобного персонажа, загадаете ещё')
    confirm = None
    while confirm == None:
        confirm = main.get_string()
    if confirm == 'да':
        return True
    else:
        return False
    
#вывести сообщение в консоль и произнести его
def message(msg):
    print('джарвис:', msg)
    msg.replace('м/с', 'мультсериала').replace('м/ф', 'мультфильма').replace('к/ф', 'кинофраншизы').replace('т/с', 'телесериала')
    voice.speaker(msg)

def get_answer():
    data = None
    while data == None:
        data = main.get_string()
    return data

def start():
    stop_words = ['стоп', 'хватит', 'прекрати', 'давай закончим']
    persons ,questions = load_bases()
    q_num = 0

    while True:
        column = ''
        #сначала идут типовые вопросы: мужчина или женшина, живой - мертвый, выымышленный или реальный
        q_num += 1
        if q_num == 1:
            if random.randint(0, 1) == 0:
                column = 'Male'
            else:
                column = 'Female'
        elif (q_num == 2):
            if random.randint(0, 1) == 0:
                column = 'Imagine'
            else:
                column = 'Real'
        elif q_num == 3:
            if random.randint(0, 1) == 0:
                column = 'Live'
            else:
                column = 'Dead'
        else:
            column = random.choice(list(questions.keys()))
        #спрашиваем и убираем вопрос, чтобы не повторялся
        if len(questions) > 0:
            message(questions[column])
        else:
            message("мои вопросы не загрузились")
            return
        del questions[column]

        #получаем ответ
        data = get_answer()

        #если стоп-слово, выходим
        if data in stop_words:
            break

        #фильтруем персонажей
        if data == 'да':
            persons = persons[persons[column] == True]
        elif data == 'нет':
            persons = persons[persons[column] == False]

        #убираем столбы с одним значением.
        cols = list(questions.keys())
        for i in cols:
            if (len(persons[i].unique()) == 1):
                questions.pop(i)

        print('персонажи', persons.shape[0]) #для дебага
        
        #если осталось немного персонажей, случайно предлагаем из оставшегося
        if (persons.shape[0] < 5) & (len(questions) < 4) | (persons.shape[0] == 1):
            while persons.shape[0] > 0:
                pers = random.choice(list(persons.Name))
                message('вы загадали '+pers)
                #если персонаж не тот, убираем его. если угадали, предлагаем сыграть заново
                if (get_answer() != 'нет'):
                    message('сыграем еще')
                    if get_answer() != 'да':
                        return
                    break
                persons = persons[persons['Name'] != pers]
            else:
                #если персонажей не осталось, говорим, что такого не знаем, давай по новой
                if not try_again():
                    return
            #грузим данные
            persons ,questions = load_bases()
            q_num = 0
        
if __name__ == '__main__':
    start()
