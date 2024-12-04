import logging
from cProfile import label

from pywebio.input import PASSWORD as PW_PASSWORD
from pywebio.output import put_text, put_error, put_success, put_warning, put_html
from pywebio.input import input as pw_input
from pywebio.input import textarea

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

ASK_1 = "Яка планета є найбільшою у Сонячній системі?"
ANSWER_1 = "Юпітер"
ASK_2 = "Скільки континентів на Землі?"
ANSWER_2 = "7"
ASK_3 = "Як називається столиця Франції?"
ANSWER_3 = "Париж"
ASK_4 = "Який метал є основним у виробництві алюмінієвої фольги?"
ANSWER_4 = "Алюміній"
ASK_5 = "Скільки кольорів у веселці?"
ANSWER_5 = "7"
ASK_6 = "Чи є правильною висновок що елементи поділяються на металічні і неметалічні ?"
ANSWER_6 = "Так"
ASK_7 = "Число  яке можна поділити на 2 без остачі називається?"
ANSWER_7 = "Парним"
ASK_8 = "Автором вірша 'Терпи терпець тебе шліфує' є..."
ANSWER_8 = "Василь Стус"
ASK_9 = ("Прикладка - це..."
         "а)різновид означення"
         "б)різновид дієслова"
         "в)різновид додатка")
ANSWER_9 = "А"
ASK_10 = "Як на англійській мові буде машина?"
ANSWER_10 = "Car"

put_html('<h1>Вітаю, на цікавій вікторині </h1>')
put_html('<h2>Пройдіть її і ви дизнаєтесь багато цікавого(Відповіді писати з великої букви!)</h2>')

given_name = textarea(label="Введіть ім'я", required=True, placeholder="Введіть ім'я тут", minlength=3,
                      maxlength=30)
logging.debug(f'given name: {given_name}')

score = 0

question_1 = pw_input(label='Яка планета є найбільшою у Сонячній системі?', required=True)
logging.debug(f'The user entered the answer {question_1}')
is_correct_reply_1 = ANSWER_1 == question_1
if is_correct_reply_1:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_2 = pw_input(label=ASK_2, required=True)
logging.debug(f'The user entered the answer {question_2}')
is_correct_reply_2 = ANSWER_2 == question_2
if is_correct_reply_2:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_3 = pw_input(label=ASK_3, required=True)
logging.debug(f'The user entered the answer {question_3}')
is_correct_reply_3 = ANSWER_3 == question_3
if is_correct_reply_3:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_4 = pw_input(label=ASK_4, required=True)
logging.debug(f'The user entered the answer {question_4}')
is_correct_reply_4 = ANSWER_4 == question_4
if is_correct_reply_4:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_5 = pw_input(label=ASK_5, required=True)
logging.debug(f'The user entered the answer {question_5}')
is_correct_reply_5 = ANSWER_5 == question_5
if is_correct_reply_5:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_6 = pw_input(label=ASK_6, required=True)
logging.debug(f'The user entered the answer {question_6}')
is_correct_reply_6 = ANSWER_6 == question_6
if is_correct_reply_6:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_7 = pw_input(label=ASK_7, required=True)
logging.debug(f'The user entered the answer {question_7}')
is_correct_reply_7 = ANSWER_7 == question_7
if is_correct_reply_7:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_8 = pw_input(label=ASK_8, required=True)
logging.debug(f'The user entered the answer {question_8}')
is_correct_reply_8 = ANSWER_8 == question_8
if is_correct_reply_8:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_9 = pw_input(label=ASK_9, required=True)
logging.debug(f'The user entered the answer {question_9}')
is_correct_reply_9 = ANSWER_9 == question_9
if is_correct_reply_9:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")

question_10 = pw_input(label=ASK_10, required=True)
logging.debug(f'The user entered the answer {question_10}')
is_correct_reply_10 = ANSWER_10 == question_10
if is_correct_reply_10:
    put_success('Молодець')
    score = score + 1
else:
    put_error("Неправильно")
put_success(f"{score / 10 * 100} %")
put_success('Кінець!')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
put_warning(f"{given_name}")
put_warning(f"{score}")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
