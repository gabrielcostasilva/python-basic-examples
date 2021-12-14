from abc import ABC, abstractmethod


class AbstractSearch(ABC):

    @staticmethod
    def of(item: str):
        if str == "simple":
            return SimpleSearch()

        else:
            return AdvancedSearch()

    # @abstractmethod
    def search(self, item: str, list):
        [print(x) for x in list if x == item]


class SimpleSearch(AbstractSearch):

    def search(self, item: str, list):  # method overriding
        [print(x) for x in list if x == item]

    def search(self, item: int, list):  # method overloading
        [print(x) for x in list if x == item]


class AdvancedSearch(AbstractSearch):
    pass


if __name__ == '__main__':
    # search: AbstractSearch = SimpleSearch()
    search: AbstractSearch = AbstractSearch.of("simple")
    search.search("hello", ["hello", "world"])
    search.search(1, [1, 2, 3, 4, 5])

    search = AbstractSearch.of("advanced")
    search.search("john", ["anna", "john"])
