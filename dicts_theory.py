# login = 'admin'
# password = '123'
box ={}
list_ = []
string = ''

admin_data = {
    'login': 'admin658',
    'password': '123',
    'name': 'Андрій',
    'age': 40,

    'hobbies': ['soccer', 'chess'],
    'address': {
        'city': 'Одеса',
        'post_code': 65088,
        'flat': None,
    },
    'salary':2_000
}
admin_first_hobby = admin_data['hobbies'][0]
admin_login = admin_data['login']
admin_age = admin_data['age']
admin_city = admin_data['address']['city']
admin_street = admin_data['address'].get('street')
admin_flat1 = admin_data['address'].get('flat')

# "якщо я не впевнена що в адресі є вулиця то пишу get.('вулиця яка є або ні')"
admin_flat2 = admin_data['address']['flat']

admin_data['surname'] = 'Дорошенко'
# "добовляємо дані яких не було на момент створення"
admin_surname = admin_data['surname']

# "добовляємо дані яких не було на момент створення в словничку"
admin_data['address']['street'] = 'Садова'

# добовляємо в список один об'єкт
admin_data['hobbies'].append('swimming')

#змінюємо значення яке вже існує
admin_data['age'] = 41


# як видаляти в словнику
admin_data['address'] = None

del admin_data['address']
#оновлюємо дані

extra_admin_data = {
    'salary':10_000 ,
    'address': {
        'city': 'Одеса',
        'post_code': 65088,
        'flat': 125,
        'house': 12 ,
        'street':'Соборна '
    }
}
# об'єднуємо два словника
full_admin_data = admin_data| extra_admin_data



pass





