import untlis_2

def test_is_even_positive():
    number = 6
    expected_result = True
    actual_result = untlis_2.is_even(number)
    assert actual_result == expected_result

def test_is_even_negative():
    number = 5
    expected_result = False
    actual_result = untlis_2.is_even(number)
    assert actual_result == expected_result

def test_get_of_strings():
    items = []
    expected_result = []
    actual_result = untlis_2.get_list_of_strings(items)
    assert actual_result == expected_result

def test_get_of_strings_not_empty():
    items = [22,'apple']
    expected_result = ['apple']
    actual_result = untlis_2.get_list_of_strings(items)
    assert actual_result == expected_result


def test_is_multiply_number():
    number = 5
    expected_result = 50
    actual_result = untlis_2.multiply_ten(number)
    assert actual_result == expected_result

def test_is_multiply_number_negative():
    number = -2.5
    expected_result = 25
    actual_result = untlis_2.multiply_ten(number)
    assert actual_result == expected_result


def test_filter_strings_with_n():
    list_strings = []
    expected_result = []
    actual_result = untlis_2.filter_strings_with_n(list_strings)
    assert actual_result == expected_result

def test_filter_strings_with_n_result():
    list_strings = ['n', 'N' , 'apple']
    expected_result = ['n', 'N' ]
    actual_result = untlis_2.filter_strings_with_n(list_strings)
    assert actual_result == expected_result

def test_return_one_hundred():
    expected_result = 100
    actual_result =untlis_2.return_max_discount()
    assert actual_result == expected_result

def test_get_vowels_from_text_empty_string():
    text = ''
    expected_result = ''
    actual_result = untlis_2.get_vowels_from_text(text)
    assert actual_result == expected_result


def test_get_vowels_from_text_no_param():
    expected_result = ''
    actual_result = untlis_2.get_vowels_from_text()
    assert actual_result == expected_result

def test_get_vowels_from_text_case_1():
    text = 'Alaska'
    expected_result = 'aaa'
    actual_result = untlis_2.get_vowels_from_text(text)
    assert actual_result == expected_result

def test_get_vowels_from_text_case_2():
    text = 'ffff'
    expected_result = ''
    actual_result = untlis_2.get_vowels_from_text(text)
    assert actual_result == expected_result

def test_get_vowels_from_text_case_3():
    text = 'apa'
    expected_result = 'aa'
    actual_result = untlis_2.get_vowels_from_text(text)
    assert actual_result == expected_result