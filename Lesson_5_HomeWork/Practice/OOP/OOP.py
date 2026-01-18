class SmartPhone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = min(100, self.battery_level + 10)

    def get_status(self):
        return f"Телефон {self.brand} {self.model} заряжен на {self.battery_level}%"


phone = SmartPhone("Samsung", "A51", 89)

phone.charge()
print(phone.get_status())
