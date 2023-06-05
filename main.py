from os import getenv
import psycopg2
from dotenv import load_dotenv
from time import sleep

load_dotenv()

PG_DBNAME = getenv('POSTGRES_DBNAME')
PG_HOST = getenv('POSTGRES_HOST')
PG_PORT = getenv('POSTGRES_PORT')
PG_USER = getenv('POSTGRES_USER')
PG_PASSWORD = getenv('POSTGRES_PASSWORD')

def main():
     
    connection = psycopg2.connect(
    dbname=PG_DBNAME,
    host=PG_HOST,
    port=PG_PORT,
    user=PG_USER,
    password=PG_PASSWORD,
)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM questions')

    def start_quiz():
        print('Викторина "Кругозор"')
        answer = input('Готовы ли Вы начать игру (да/нет) :')
        if answer.lower() in ['да' or 'yes']:
            print('Начнем!')
            sleep(0.5)
            return True
        elif answer.lower() in ['нет' or 'no']:
            print('Жаль... Возвращайтесь, когда будете готовы.')
            return False
        else:
            connection.close()

    start_quiz()
    quiz(cursor.fetchall())
    connection.close()


    
def quiz(questions):
    num = 0
    score = 0
    right = questions[num][6]

    while num < len(questions):
            print('{0}\n1) {1}\n2) {2}\n3) {3}\n4 {4}'.format(*questions[num][1:6]))
            inp = input('Введите номер: ')
            try:
                try_answer = int(inp)
            except Exception:
                print('Введите число')
                continue
            if try_answer == right:
                score += 1
                print('Верно!', '\n')
            else:
                print('Неправильный ответ! Верный ответ:', int(questions[num][6]), '\n')
            num += 1

        
            if num == len(questions):
                print('Викторина подошла к концу, спасибо за участие, вы набрали {0}/{1} баллов!'.format(score, len(questions)))
                if input('Хотите сыграть еще раз? (да/нет): ').lower() == 'да':
                    num = 0
                    score = 0
    
if __name__ == '__main__':
    main()
