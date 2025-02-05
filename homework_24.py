class Car:

    def __init__(self, year_of_release: str, producer: str, car_model: str, fuel_flow: float, price: float):
        self.year_of_release = year_of_release
        self.producer = producer
        self.car_model = car_model
        self.fuel_flow = fuel_flow
        self.price = price
        self.car_mileage = 0

    def __str__(self) -> str:
        return f'<Я авто марки ,{self.car_model} їду по справам господаря  >'

    def drive(self) -> None:
        print(self)

    @property
    def category(self) -> str:
        if self.price > 15000:
            return f'Крутяк'
        else:
            return "тачелла"


corolla_car = Car(year_of_release='2021', producer='Toyota', car_model='Corolla Live', fuel_flow=110, price=28000)
yaris_car = Car(year_of_release='2020', producer='Yaris', car_model='Yaris Гібрид', fuel_flow=56, price=30000)
corolla_car.car_mileage = 1130
yaris_car.drive()
pass
