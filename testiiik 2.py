class BeerBar:
    def __init__(self):
        self.beer_suggestions = {
            "грустное": {"zara": ("Stout", "5%", 300), "gucchi": ("Porter", "6%", 350), "sela": ("Brown Ale", "4%", 250)},
            "веселое": {"zara": ("IPA", "7%", 350), "gucchi": ("Double IPA", "8%", 400),
                        "sela": ("Belgian Witbier", "4%", 300)},
            "злое": {"zara": ("Imperial Stout", "10%", 450), "gucchi": ("Russian Imperial Stout", "11%", 500),
                     "sela": ("Barleywine", "12%", 550)},
            "обычное": {"zara": ("Lager", "4%", 200), "gucchi": ("Pilsner", "5%", 250), "sela": ("Kölsch", "4%", 220)}
        }

    def add_beer(self, mood, brand, beer_type, beer_strength, beer_price):
        if mood not in self.beer_suggestions:
            self.beer_suggestions[mood] = {}
        self.beer_suggestions[mood][brand] = (beer_type, beer_strength, beer_price)
        print(f"Сорт пива {beer_type} добавлен в базу данных для настроения '{mood}' и бренда одежды '{brand}'.")

    def remove_beer(self, mood, brand):
        if mood in self.beer_suggestions and brand in self.beer_suggestions[mood]:
            self.beer_suggestions[mood].pop(brand)
            print(f"Сорт пива для настроения '{mood}' и бренда одежды '{brand}' удален из базы данных.")
        else:
            print(f"Ошибка: Нет такого сорта пива для настроения '{mood}' и бренда одежды '{brand}'.")

    def display_beer_database(self):
        print("База данных пива:")
        for mood, suggestions in self.beer_suggestions.items():
            print(f"Настроение: {mood}")
            for brand, beer_info in suggestions.items():
                beer_type, beer_strength, beer_price = beer_info
                print(f"Бренд одежды: {brand}")
                print(f"Сорт пива: {beer_type}")
                print(f"Крепость: {beer_strength}")
                print(f"Цена: {beer_price} руб.")
                print("-----------------")

# Создаем экземпляр класса BeerBar
bar = BeerBar()

# Выводим базу данных пива
bar.display_beer_database()
print("-----------------")

# Добавляем новый сорт пива
bar.add_beer("праздничное", "zara", "Amber Ale", "6%", 300)
print("-----------------")

# Удаляем сорт пива
bar.remove_beer("грустное", "gucchi")
print("-----------------")

# Выводим обновленную базу данных пива
bar.display_beer_database()




