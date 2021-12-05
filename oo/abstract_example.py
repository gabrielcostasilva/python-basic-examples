from abc import ABC, abstractmethod


class AbstractSearchClass(ABC):

    @abstractmethod
    def search(self, alist: list, an_item: int) -> int:
        pass


class NaiveSearch(AbstractSearchClass):

    def search(self, alist: list, an_item: int) -> int:
        for x in alist:
            if x == an_item:
                return True
            
class AutoSearch(AbstractSearchClass):
    
    def search(self, alist: list, an_item: int) -> int:
        return list(filter(lambda x: x == an_item, alist))
    

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # search = NaiveSearch()
    search = AutoSearch()
    value_to_search = 12
    
    if search.search(my_list, value_to_search):
        print(f"The value {value_to_search} is present in the list")
    
    else:
        print(f"The value {value_to_search} is NOT present in the list")


if __name__ == '__main__':
    main()
