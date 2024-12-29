import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

data1 = 56565
data2 = 0.00
text1 = "fhjdkmfkjfjkfjkfjk"
text2 = "   "
text3 = ""
logging.debug(f"{bool(data1)=}")
logging.debug(f"{bool(data2)=}")
logging.debug(f"{bool(text1)=}")
logging.debug(f"{bool(text2)=}")
logging.debug(f"{bool(text3)=}")




string_length1 = len(text1)
string_length2 = len(text2)
string_length3 = len(text3)
if text1 == text2:
    pass
if text1 == text2 and data1:
    pass


import logging
from pickle import FLOAT

from pywebio.input import input as pw_input, slider
from pywebio.input import PASSWORD as PW_PASSWORD, NUMBER
from pywebio.input import textarea
from pywebio.output import put_text, put_error, put_success, put_warning, put_html

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

LOGIN = 'admin'
PASSWORD = '123'

# HEADER
put_html('<h1>Welcome to the name processor</h1>')
put_html('<h2>demo version</h2>')

# GET LOGGING DATA
login = pw_input(label='Enter your login', required=True)
logging.info(f'User entered login {login}')

password = pw_input(label='Enter your password', required=True, type=PW_PASSWORD)
logging.debug(f'User entered password {password}')

is_correct_login = LOGIN == login
logging.debug(f'User correct login: {is_correct_login}')
is_correct_password = PASSWORD == password
if is_correct_login and is_correct_password:

    put_success('You are logged in')

    given_name = pw_input(label='Enter your name', required=True).strip()
    if given_name == LOGIN:
        put_warning('Your login is similar to your name')
    name_length = len(given_name)
    if name_length == 1:
        put_success(f'Strange name with length {name_length}')



weight1 = pw_input(label='Enter your weight', required=True, type=NUMBER, min=25, max=150, value=50)
weight2 = slider(label='Enter your weight in slider', required=True, type=FLOAT, min=25, default=150, value=50)