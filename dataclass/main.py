from dataclasses import dataclass, field


@dataclass()
class Person:
    name: str
    age: int = field(default=27)


person = Person('Marcin')
print(person)
