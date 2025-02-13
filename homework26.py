from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model


    @abstractmethod
    def info(self):
        return f'Бренд автомобільного засобу {self.brand}, його модель {self.model}'


class Car(Vehicle):
    def __init__(self, brand: str, model: str, num_doors: int):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        return f'Бренд автомобільного засобу  {self.brand}, його модель {self.model}, кількість діерей {self.num_doors}'


class Bike(Vehicle):
    def __init__(self, brand: str, model: str, type: str):
        super().__init__(brand, model)
        self.type = type

    def info(self):
        return f'Бренд автомобільного засобу {self.brand}, його модель {self.model} , його тип {self.type}'


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, capacity: int):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        return (f'Бренд автомобільного засобу {self.brand}, його модель {self.model} , його вантажопідйомність '
                f'{self.capacity} кг')



car = Car(brand='BMV', model='BMW 840d xDrive', num_doors=4)
bike = Bike(brand='Velo Srlad', model='WINNER SPECIAL 27.5" 2022', type='Гірський велосипед')
truck = Truck(brand=' Mercedes', model='Самоскид Mercedes-Benz AROCS 4148', capacity=24500)


print(car.info())
print(bike.info())
print(truck.info())
