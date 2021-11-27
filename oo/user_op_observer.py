import logging

class Publisher:
    subscribers = set()

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)

    def notify_subscribers(self, added_name):
        for a_subscriber in self.subscribers:
            a_subscriber.update(added_name)

class Subscriber:
    def update(self, added_name):
        pass

class LoggingUtility(Subscriber):

    def update(self, added_name):
        logging.basicConfig(level=logging.DEBUG,
                            format="%(levelname)s %(asctime)s - %(message)s")

        logger = logging.getLogger()
        logger.addHandler(logging.StreamHandler())

        logger.info(f"Name '{added_name}' added!")

class InsertNames(Publisher):

    def __init__(self):
        self.__name_set = set()

    def insert(self):
        insert_name = True

        while insert_name:
            a_name = input("Enter a name: ").strip().title()
            self.__name_set.add(a_name)
            self.notify_subscribers(a_name)
            insert_name = input(
                "Do you wanna input another name? (y/n) ").strip().startswith("y")

def main():
    insert_names = InsertNames()
    insert_names.subscribe(LoggingUtility())
    insert_names.insert()

if __name__ == "__main__":
    main()