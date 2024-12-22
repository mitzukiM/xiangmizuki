import untlis_homework

def test_calculation_of_area_length_negative():
    length = -9
    width = 5
    expected_result = -45
    actual_result = untlis_homework.calculation_of_area(length,width)
    assert actual_result == expected_result

def test_calculation_of_area_width_is_0():
    length = 8
    width = 0
    expected_result = 0
    actual_result = untlis_homework.calculation_of_area(length,width)
    assert actual_result == expected_result

def test_calculation_of_area_is_not_whole():
    length = 5
    width = 7.7
    expected_result = 38.5
    actual_result = untlis_homework.calculation_of_area(length, width)
    assert actual_result == expected_result
