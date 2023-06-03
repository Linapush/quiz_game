from os import getenv
import psycopg2
from dotenv import load_dotenv

load_dotenv()

PG_DBNAME = getenv('POSTGRES_DBNAME')
PG_HOST = getenv('POSTGRES_HOST')
PG_PORT = getenv('POSTGRES_PORT')
PG_USER = getenv('POSTGRES_USER')
PG_PASSWORD = getenv('POSTGRES_PASSWORD')

connection = psycopg2.connect(
    dbname=PG_DBNAME,
    host=PG_HOST,
    port=PG_PORT,
    user=PG_USER,
    password=PG_PASSWORD,
)
cursor = connection.cursor()

def view_question():
    print('Викторина "Кругозор"')
    answer = input('Готовы ли Вы начать игру (да/нет) :')
    if answer.lower() not in ['да']:
        return False
    return True

    
def get_questions():
    cursor.execute('SELECT * FROM questions')
    questions = []
    for question in cursor.fetchall():
        q_dict = {
            'id': question[0],
            'question': question[1],
            'answer_1': question[2],
            'answer_2': question[3],
            'answer_3': question[4],
            'answer_4': question[5],
            'right_answer': question[6]
        }
        questions.append(q_dict)
    return questions


def check_answer(question, answer):
    return answer == question['right_answer']


def main():
    if not view_question():
        return
    
    total_questions = get_questions()
    elements = 0
    score = 0
    
    while elements < len(total_questions):
        question = total_questions[elements]
        print(question['question'])
        print('1. {0}'.format(question['answer_1']))
        print('2. {0}'.format(question['answer_2']))
        print('3. {0}'.format(question['answer_3']))
        print('4. {0}'.format(question['answer_4']))
        user_answer = input('Введите вариант ответа (1-4): ')

        try:
            try_answer = int(user_answer)
        except ValueError:
            print('Введите цифру от 1 до 4!')
            continue

        if 0 < try_answer <= 4:
            if check_answer(question, try_answer):
                print('Верно!')
                elements += 1
                score += 1
            else:
                print('Ответ неправильный!')
                elements += 1
        else:
            print('Введите цифру от 1 до 4!')
        
        if elements == len(total_questions):
            print('Викторина закончилась, вы набрали {0}/{1} баллов!'.format(score, len(total_questions)))
            if input('Хотите сыграть еще раз? (да/нет): ').lower() == 'да':
                elements = 0
                score = 0
    connection.close()
    
if __name__ == '__main__':
    main()
