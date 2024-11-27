import phrase
import menu_price
print(phrase.PHRASE_1)
phrase_0 = input("Як я можу до вас звертатися : ")
print(phrase.PHRASE_2)
meal_1 = "borsch"
meal_2 = "Cottage cheese at sour cream"
meal_3 = "dumplings"
meal_4 = "trout"
meal_5 = "cheese omelet"
print(meal_1)
print(menu_price.borsch_price)
print(meal_2)
print(menu_price.Cottage_cheese_at_sour_cream_price)
print(meal_3)
print(menu_price.dumplings_price)
print(meal_4)
print(menu_price.trout_price)
print(meal_5)
print(menu_price.cheese_omelet_price)
print(phrase.PHRASE_3)
phrase_1 = input("Чи не хочете обрати щось окрім форелі: ")
print(phrase.PHRASE_4)
print(phrase.PHRASE_5)
total = menu_price.trout_price
print("*" * 50)
print("RECEIPT")
print(f"Total amount of money for your dinner = {total} ")
print("*" * 50)
print(phrase.PHRASE_6)
print(phrase.PHRASE_7)















