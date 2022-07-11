"""
Напишите классы сериализации контейнеров с данными Python в json, bin файлы.
Сами классы должны соответствовать общему интерфейсу
(абстрактному базовому классу) SerializationInterface.
"""

from abc import ABCMeta, abstractmethod
import json
import csv


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def read(self, from_file):
        pass

    @abstractmethod
    def write(self, to_file, data):
        pass


class JsonFile(SerializationInterface):

    def read(self, from_file):
        with open(from_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write(self, to_file, data):
        with open(to_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)


class BinFile(SerializationInterface):

    def read(self, from_file):
        with open(from_file, 'rb', encoding='utf-8') as f:
            return f.readlines()

    def write(self, to_file, data):
        with open(to_file, 'wb', encoding='utf-8') as f:
            return f.write(data)


jdata = JsonFile()
jdata.write('json.json', 'sdfsdf')


