from abc import ABC,abstractmethod

class Bike(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerte(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class Hunter(Bike):
    def start(self):
        print("hunter start method")

    def accelerte(self):
        print("hunter accelerate methid")

    def stop(self):
        print("hunter stop method")

hunter_instance=Hunter()
hunter_instance.start()                   