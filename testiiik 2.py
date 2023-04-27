print("Бар безалкогольного пива\nДоброго времени суток, я бармен - Олег")
print("Я не совсем понимаю, какое у вас сегодня настроение? Веселое, грустное, злое или обычное?\nУкажите один из вариантов!\nКстати, мне очень понравилась ваша одежда! Подскажите какой это бренд?\n Я уверен, что это Zara, Gucchi или Sela?\nУкажите один из вариантов!")
beer_suggestions = {
    "грустное": {"zara": ("Stout", "5%", 300), "gucchi": ("Porter", "6%", 350), "sela": ("Brown Ale", "4%", 250)},
    "веселое": {"zara": ("IPA", "7%", 350), "gucchi": ("Double IPA", "8%", 400),
                "sela": ("Belgian Witbier", "4%", 300)},
    "злое": {"zara": ("Imperial Stout", "10%", 450), "gucchi": ("Russian Imperial Stout", "11%", 500),
             "sela": ("Barleywine", "12%", 550)},
    "обычное": {"zara": ("Lager", "4%", 200), "gucchi": ("Pilsner", "5%", 250), "sela": ("Kölsch", "4%", 220)}
}


def suggest_beer(mood, brand):
    # Проверка настроения
    mood = mood.lower()
    brand = brand.lower()
    if mood not in ["грустное", "веселое", "злое", "обычное"]:
        print("Ошибка: Неправильное настроение")
        return
    # Проверка бренда одежды
    if brand not in ["zara", "gucchi", "sela"]:
        print("Ошибка: Неправильный бренд одежды")
        return

    # Получаем предложение по пиву на основе настроения и бренда одежды
    beer_type, beer_strength, beer_price = beer_suggestions[mood][brand]

    # Выводим рекомендацию
    print(f"Мы рекомендуем вам попробовать {beer_type} с крепостью {beer_strength} и ценой {beer_price} за литр.")


def add_beer(mood, brand, beer_type, beer_strength, beer_price):
    if mood not in beer_suggestions:
        beer_suggestions[mood] = {}
    beer_suggestions[mood][brand] = (beer_type, beer_strength, beer_price)
    print(f"Сорт пива {beer_type} добавлен в базу данных для настроения '{mood}' и бренда одежды '{brand}'.")


def remove_beer(mood, brand):
    if mood in beer_suggestions and brand in beer_suggestions[mood]:
        beer_suggestions[mood].pop(brand)
        print(f"Сорт пива для настроения '{mood}' и бренда одежды '{brand}' удален из базы данных.")
    else:
        print(f"Ошибка: Нет такого сорта пива для настроения '{mood}' и бренда одежды '{brand}'.")


def print_beer_suggestions():
    for mood in beer_suggestions:
        print(f"Для настроения '{mood}':")
        for brand in beer_suggestions[mood]:
            beer_type, beer_strength, beer_price = beer_suggestions[mood][brand]
            print(f"- Бренд одежды '{brand}': {beer_type} с крепостью {beer_strength} и ценой {beer_price} за литр.")

suggest_beer(mood=(str(input())), brand=(str(input())))