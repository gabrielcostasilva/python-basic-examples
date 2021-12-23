from dataclasses import dataclass, field


@dataclass(frozen=True)
class User:
    name: str
    id: int = field(default=1)
    # id: int = 1

    def __post_init__(self):
        if (type(self.name) is not str) or (len(self.name) <= 2):
            raise TypeError("A name must be a text longer than 2 characters")


if __name__ == "__main__":
    # print(User())
    # print(User("Anna", 10))
    print(User(" Anna ", 10)) # We cannot trim!
    # print(User(True, 10)) # This validation works
    # print(User("ox")) # This validation works as well
