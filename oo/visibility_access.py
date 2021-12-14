from dataclasses import dataclass


class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def print_data(self):
        print(f"{self.__id}, {self.__name}")

@dataclass
class UserDataclass:
    __id: int
    __name: str

    def __str__(self):
        return "UserDataclass: id = " + str(self.__id) + "; name = " + self.__name

if __name__ == '__main__':
    user = User(1, "John Doe")
    # print(user.name) # As expected, this code does not work
    user.print_data()

    user_dataclass = UserDataclass(1, "John Doe")
    # print(user_dataclass.name) # This does not work as well
    print(user_dataclass)

