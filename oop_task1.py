# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Statuette:
    def __init__(self, weight: float, height: float):
        """
        Создание и подготовка к работе объекта "Статуэтка"

        :param weight: Вес статуэтки в граммах.
        :param height: Высота статуэтки в см.

        Примеры:
        >>> statuette = Statuette(850, 25)  # инициализация экземпляра класса
        """
        if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Вес статуэтки и её высота должны быть типа int или float")
        if weight <= 0 or height <= 0:
            raise ValueError("Вес статуэтки и её высота должны быть положительными числами")
        self.weight = weight
        self.height = height

    def move_statuette(self, distance: float) -> None:
        """
        Функция перемещения статуэтки на заданное расстояние

        :param distance: Расстояние в см., на которое переместили статуэтку
        
        :raise TypeError: Если расстояние задано не типами int и float
        :raise ValueError: Если расстояние задано не положительным числом или не нулем

        :return: На какое расстояние переместилась статуэтка.

        Примеры:
        >>> statuette = Statuette(850, 25)
        >>> statuette.move_statuette(35)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance < 0:
            raise ValueError("Расстояние должно быть положительным числом или нулем")

        ...

    def interact_with(self, other: str) -> None:
        """
        Функция описывает взаимодействие с другим физическим объектом.

        :param other: Другой физический объект.
        :raise TypeError: Если другой физическим объект задан числом, то вызываем ошибку.

        Примеры:
        >>> statuette = Statuette(850, 25)
        >>> statuette.interact_with('Салфетка')
        """
        if isinstance(other, (int, float)):
            raise TypeError("Физический объект не должен быть типа int или float")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


import doctest
class Classmates:
    def __init__(self, num_users: int, num_posts: int):
        """
        Создание и подготовка к работе объекта "Одноклассники (социальная сеть)"

        :param num_users: Количество пользователей.
        :param num_posts: Количество постов.

        :raise TypeError: Если количество пользователей или постов заданы не типом int.
        :raise ValueError: Если количество пользователей или постов являются отрицательными числами.

        Примеры:
        >>> сlassmates = Classmates(500000, 1500000)  # инициализация экземпляра класса
        """
        if not isinstance(num_users, (int)) or not (num_posts, (int)):
            raise TypeError("Количество пользователей и количество постов должны быть типа int.")
        if num_users < 0 or num_posts < 0:
            raise ValueError("Количество пользователей и количество постов должны быть положительными числами")
        self.num_users = num_users
        self.num_posts = num_posts

    def add_users(self, user_ID: str) -> None:
        """
        Функция добавления пользователя в социальную сеть.
        :param user_ID: ID пользователя.

        :raise TypeError: Если ID пользователя задано не типом str.

        :return: ID добавленного в социальную сеть пользователя.

        Примеры:
        >>> сlassmates = Classmates(500000, 1500000)
        >>> сlassmates.add_users("ID добавленного пользователя: 5647389567")
        """
        if not isinstance(user_ID, (str)):
            raise TypeError("ID пользователя должно быть типа str")
        ...

    def get_users_stats(self, user_ID: str) -> dict:
        """
        Функция возвращает статистику пользователя.
        :param user_ID: ID пользователя.

        :raise TypeError: Если ID пользователя задано не типом str.

        :return: Словарь со статистикой пользователя.

        Примеры:
        >>> сlassmates = Classmates(500000, 1500000)
        >>> сlassmates.get_users_stats("ID пользователя: 5647389567")
        """
        if not isinstance(user_ID, (str)):
            raise TypeError("ID пользователя должно быть типа str")
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


import doctest
class Car:
    def __init__(self, model: str, year: int, mileage: int, float):
        """
        Создание и подготовка к работе объекта "Машина"

        :param model: Модель машины.
        :param year: Год выпуска машины.
        :param  mileage: Пробег машины.

        :raise TypeError: Если год не является целым числом, или пробег не является числом.
        :raise ValueError: Если модель - пустая строка, год выпуска меньше или равен 0, или пробег меньше 0.

        Пример:
        >>> car = Car("Toyota Camry", 2023, 3000)  # инициализация экземпляра класса
        """
        if not isinstance(model, str) or not model:
            raise ValueError("Модель машины должна быть непустой строкой.")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом.")
        if year <= 0:
            raise ValueError("Год выпуска должен быть целым неотрицательным числом.")
        if not isinstance(mileage, (int, float)):
            raise TypeError("Пробег машины должен быть неотрицательным числом.")
        if mileage < 0:
            raise ValueError("Пробег машины должен быть неотрицательным числом.")

        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance: float) -> None:
        """
        Проехать указанное расстояние.

        :param distance: Расстояние в километрах.

        :raise ValueError: Если расстояние отрицательное.

        :return Количество километров, которые необходимо проехать.

        Пример:
        >>> car = Car("Toyota Camry", 2023, 3000)
        >>> car.drive(100)
        """
        if not isinstance(distance, (int, float)) or distance < 0:
            raise ValueError("Расстояние должно быть неотрицательным числом.")

        ...


    def get_info(self) -> str:
        """
        Возвращает информацию о машине.

        :return Строка с информацией о машине.

        Пример:
        >>> car = Car("Toyota Camry", 2023, 3000)
        >>> car.get_info()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


