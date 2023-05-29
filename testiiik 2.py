from threading import Thread

class BeerBar:
    def __init__(self):
        """
        Инициализирует объект класса BeerBar.

        Атрибуты:
        - beer_suggestions (dict): Словарь, содержащий рекомендации по пиву для различных настроений и брендов одежды.
        """
        self.beer_suggestions = {
            "грустное": {"zara": ("Stout", "5%", 300), "gucchi": ("Porter", "6%", 350), "sela": ("Brown Ale", "4%", 250)},
            "веселое": {"zara": ("IPA", "7%", 350), "gucchi": ("Double IPA", "8%", 400), "sela": ("Belgian Witbier", "4%", 300)},
            "злое": {"zara": ("Imperial Stout", "10%", 450), "gucchi": ("Russian Imperial Stout", "11%", 500), "sela": ("Barleywine", "12%", 550)},
            "обычное": {"zara": ("Lager", "4%", 200), "gucchi": ("Pilsner", "5%", 250), "sela": ("Kölsch", "4%", 220)}
        }

    def suggest_beer(self, mood, brand):
        """
        Рекомендует сорт пива на основе указанного настроения и бренда одежды.

        Аргументы:
        - mood (str): Настроение, для которого нужно получить рекомендацию.
        - brand (str): Бренд одежды.

        Выводит рекомендацию по сорту пива с указанием крепости и цены за литр.
        """
        mood = mood.lower()
        brand = brand.lower()
        if mood not in self.beer_suggestions:
            print("Ошибка: Неправильное настроение")
            return
        if brand not in ["zara", "gucchi", "sela"]:
            print("Ошибка: Неправильный бренд одежды")
            return

        beer_type, beer_strength, beer_price = self.beer_suggestions[mood][brand]
        print(f"Мы рекомендуем вам попробовать {beer_type} с крепостью {beer_strength} и ценой {beer_price} за литр.")

    def add_beer(self, mood, brand, beer_type, beer_strength, beer_price):
        """
        Добавляет новый сорт пива в базу данных рекомендаций.

        Аргументы:
        - mood (str): Настроение, для которого добавляется сорт пива.
        - brand (str): Бренд одежды.
        - beer_type (str): Сорт пива.
        - beer_strength (str): Крепость пива.
        - beer_price (int): Цена пива за литр.

        Добавляет указанный сорт пива в базу данных рекомендаций для указанного настроения и бренда одежды.
        """
        if mood not in self.beer_suggestions:
            self.beer_suggestions[mood] = {}
        self.beer_suggestions[mood][brand] = (beer_type, beer_strength, beer_price)
        print(f"Сорт пива {beer_type} добавлен в базу данных для настроения '{mood}' и бренда одежды '{brand}'.")

    def remove_beer(self, mood, brand):
        """
        Удаляет сорт пива из базы данных рекомендаций.

        Аргументы:
        - mood (str): Настроение, для которого удаляется сорт пива.
        - brand (str): Бренд одежды.

        Удаляет указанный сорт пива из базы данных рекомендаций для указанного настроения и бренда одежды.
        """
        if mood in self.beer_suggestions and brand in self.beer_suggestions[mood]:
            self.beer_suggestions[mood].pop(brand)
            print(f"Сорт пива для настроения '{mood}' и бренда одежды '{brand}' удален из базы данных.")
        else:
            print(f"Ошибка: Нет такого сорта пива для настроения '{mood}' и бренда одежды '{brand}'.")

    def print_beer_suggestions(self):
        """
        Выводит все рекомендации по сортам пива.

        Для каждого настроения и бренда одежды выводит рекомендуемый сорт пива, крепость и цену за литр.
        """
        for mood in self.beer_suggestions:
            print(f"Для настроения '{mood}':")
            for brand in self.beer_suggestions[mood]:
                beer_type, beer_strength, beer_price = self.beer_suggestions[mood][brand]
                print(f"- Бренд одежды '{brand}': {beer_type} с крепостью {beer_strength} и ценой {beer_price} за литр.")


if __name__ == "__main__":
    beer_bar = BeerBar()
    print("Бар безалкогольного пива\nДоброго времени суток, я бармен - Олег")
    print("Я не совсем понимаю, какое у вас сегодня настроение? Веселое, грустное, злое или обычное?")
    print("Укажите один из вариантов!\nКстати, мне очень понравилась ваша одежда!")
    print("Подскажите, какой это бренд? Я уверен, что это Zara, Gucchi или Sela?")
    print("Укажите один из вариантов!")
    mood = input().lower()
    brand = input().lower()

    suggestion_thread = Thread(target=beer_bar.suggest_beer, args=(mood, brand))
    suggestion_thread.start()
    suggestion_thread.join()

    beer_type, beer_strength, beer_price = beer_bar.beer_suggestions[mood][brand]

    add_thread = Thread(target=beer_bar.add_beer, args=(mood, brand, beer_type, beer_strength, beer_price))
    add_thread.start()
    add_thread.join()

    remove_thread = Thread(target=beer_bar.remove_beer, args=(mood, brand))
    remove_thread.start()
    remove_thread.join()

    print_suggestions_thread = Thread(target=beer_bar.print_beer_suggestions)
    print_suggestions_thread.start()
    print_suggestions_thread.join()
