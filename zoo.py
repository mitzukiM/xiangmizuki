import logging
from pywebio.output import put_text, put_error, put_success, put_html
from pywebio.input import input as pw_input, NUMBER
import discount

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

put_html('<h1>Вітаю в нашому зоопарку!</h1>')

age = pw_input(label='Введіть вік відвідувача', required=True, type=NUMBER, min=1, max=100)
if age < 6:
    finel_price = discount.discount_6 * discount.price
    put_text(f"Ваш квиток коштує  {finel_price} грн")

elif 6 <= age <= 12:
    finel_price = discount.discount_6_12 * discount.price
    put_text(f"Ваш квиток коштує {finel_price} грн")

elif 13 <= age <= 17:
    finel_price = discount.discount_13_17 * discount.price
    put_text(f"Ваш квиток коштує {finel_price} грн")

elif 18 <= age <= 60:
    finel_price = discount.discount_18_60 * discount.price
    put_text(f"Ваш квиток коштує  {finel_price} грн")

elif 60 <= age <= 100:
    finel_price = discount.discount_60_100 * discount.price
    put_text(f"Ваш квиток коштує {finel_price} грн")

put_text(f"Дякую за покупку !")
