# -*- coding: utf-8 -*-
import json

# считывание через точку
class Object:
    def __init__(self, mapping):
        for key, value in mapping.items():
            if isinstance(value, dict):
                self.__dict__[key] = Object(value)
            else:
                self.__dict__[key] = value

# изменение цвета
class ColorizeMixin:
    # \033 - escape code  1 - bold 45m - white background
    cc = '\033[0m'

    def __str__(self):
        return f'\033[1;{self.repr_color_code};47m' + self.__repr__() + self.cc


class Advert(ColorizeMixin):
    repr_color_code = 33

    def __init__(self, mapping):
        self.price = 0
        self.__dict__.update(Object(mapping).__dict__)
        if 'title' not in self.__dict__.keys():
            raise ValueError("Title is missing.")
        if self.price < 0:
            raise ValueError('Price cannot be negative.')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'



if __name__ == "__main__":
    lesson_str = """{
        "title": "python",
        "price": -8,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    corgi_str = """{
          "title": "Вельш-корги",
          "price": 1000,
          "class": "dogs",
          "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
          }
        }"""
    corgi = json.loads(corgi_str)

    my_ad = Advert(lesson)
    print(my_ad.title, my_ad.location.address, my_ad.price)

    print(Advert(corgi))

    iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
    print(iphone_ad)