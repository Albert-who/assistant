import pandas
import random
import main
import voice

def init_bases():
        persons = pandas.read_csv('desktop/assistant-main/big_scary_db.csv', sep=';')
        #persons = pandas.read_csv('big_scary_db.csv', sep=';')
        questions = {}
        file = open('desktop/assistant-main/db_questions.txt', 'r')
        #file = open('db_questions.txt', 'r')
        for i in file.readlines():
            questions[i.split('|')[0]] = i.split('|')[1].replace('\n','')
        file.close()
        return persons, questions

def try_again():
    message('я не знаю подобного персонажа, загадаете ещё')
    while confirm == None:
        confirm = main.get_string()
    if confirm == 'да':
        return True
    else:
        return False
    
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
    persons ,questions = init_bases()
    q_num = 0

    while True:
        column = ''
        q_num += 1
        if q_num == 1:
            if random.randint(0, 1) == 0:
                column = 'Male'
            else:
                column = 'Female'
        elif (q_num == 2):
            if 'Imagine' in questions:
                column = 'Imagine'
            elif 'Real' in questions:
                column = 'Real'
            else:
                column = random.choice(list(questions.keys()))
        elif q_num == 3:
            if 'Live' in questions:
                column = 'Live'
            elif 'Dead' in questions:
                column = 'Dead'
            else:
                column = random.choice(list(questions.keys()))
        else:
            column = random.choice(list(questions.keys()))
        message(questions[column])
        del questions[column]

        data = get_answer()
        #print('пользователь:', data)

        if data in stop_words:
            break

        if data == 'да':
            persons = persons[persons[column] == True]
        elif data == 'нет':
            persons = persons[persons[column] == False]

        cols = list(questions.keys())
        for i in cols:
            if (len(persons[i].unique()) == 1):
                questions.pop(i)

        print('персонажи', persons.shape[0]) #для дебага
        
        if persons.shape[0] == 0:
            if not try_again():
                break

        elif persons.shape[0] < 5:
            while persons.shape[0] > 0:
                pers = random.choice(list(persons.Name))
                message('вы загадали '+pers)
                if (get_answer() != 'нет'):
                    message('сыграем еще')
                    if get_answer() != 'да':
                        return
                persons = persons[persons['Name'] != pers]
            else:
                if not try_again():
                    return
            persons ,questions = init_bases()
        
if __name__ == '__main__':
    start()