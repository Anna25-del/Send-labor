class Pets:
    """
    Базовый класс для представления домашних животных.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        _species (str): Вид животного (непубличный атрибут). Инкапсуляция вида
                       позволяет избежать случайного изменения этого атрибута,
                       вид животного не может измениться со временем.

    """
    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Конструктор класса Pets.

        Args:
            name (str): Имя животного.
            age (int): Возраст животного.
            species (str): Вид животного.
        """
        self.name = name
        self.age = age
        self._species = species

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Pets.
        """
        return f"{self.name} ({self._species}), возраст: {self.age}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Pets для отладки.
        """
        return f"Animal(name='{self.name}', age={self.age}, species='{self._species}')"

    def make_sound(self) -> str:
        """
        Издает звук животного.
        """
        return "Generic pets sound"

    def get_species(self) -> str:
        """
        Возвращает вид животного.
        """
        return self._species


class Dog(Pets):
    """
    Дочерний класс для представления собак. Наследуется от Pets.

    Атрибуты:
        breed (str): Порода собаки.
        name (str): Имя собаки (унаследовано от Pets).
        age (int): Возраст собаки (унаследовано от Pets).

    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog. Расширяет конструктор Pets, добавляя породу.

        Args:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, age, species="A pet dog")  # Вид общий для всех собак
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Dog.
        Перегружает метод __str__ базового класса, добавляя информацию о породе.
        Причина перегрузки: требуется добавить специфичную для собаки информацию в строковое представление.
        """
        return f"{self.name} ({self.breed}), возраст: {self.age}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Dog для отладки.
        Перегружает метод __repr__ базового класса, добавляя информацию о породе.
        Причина перегрузки: требуется добавить специфичную для собаки информацию в представление для отладки.
        """
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"

    def make_sound(self) -> str:
        """
        Издает звук собаки (перегруженный метод).
        Перегружает метод make_sound базового класса.
        Причина перегрузки: звук, издаваемый собакой, отличается от звука, издаваемого каким-либо другим животным.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Приносит предмет. Унаследованный и модифицированный метод.

        Args:
            item (str): Предмет, который нужно принести.

        Returns:
            str: Сообщение о том, что собака принесла предмет.
        """
        return f"{self.name} принесла {item}!"

    def wag_tail(self) -> str:
        """
        Виляет хвостом.
        """
        return f"{self.name} виляет хвостом!"

if __name__ == "__main__":
    # Write your solution here
    animal = Pets("Generic Animal", 5, "Animalia")
    print(animal)
    print(repr(animal))
    print(animal.make_sound())

    dog = Dog("Jack", 3, "Golden Retriever")
    print(dog)
    print(repr(dog))
    print(dog.make_sound())
    print(dog.fetch("палку"))
    print(dog.wag_tail())
    pass
