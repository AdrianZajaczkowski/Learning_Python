from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):  # klasa bazowa obserwatorów

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Subject(ABC):  # klasa bazowa publikujących

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class Vilager1(Observer):
    panic_lv: int = 4
    notify_lv: int = 0

    def update(self, subject: Subject) -> None:
        if self.notify_lv >= self.panic_lv:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            subject._escape = True
        else:
            self.notify_lv += 1
            subject._alarm = "FIRE IN CASTLE"


class Vilager2(Observer):
    panic_lv: int = 4
    notify_lv: int = 0

    def update(self, subject: Subject) -> None:
        print(self.notify_lv)
        if self.notify_lv >= self.panic_lv:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            subject._escape = True
        else:
            self.notify_lv += 1
            subject._alarm = "FIRE IN CASTLE"


class Vilager3(Observer):
    panic_lv: int = 4
    notify_lv: int = 0

    def update(self, subject: Subject) -> None:
        print(self.notify_lv)
        if self.notify_lv >= self.panic_lv:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            subject._escape = True
        else:
            self.notify_lv += 1
            subject._alarm = "FIRE IN CASTLE"


class Vilager4(Observer):
    panic_lv: int = 4
    notify_lv: int = 0

    def update(self, subject: Subject) -> None:

        if self.notify_lv >= self.panic_lv:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            subject._escape = True
            subject._alarm = "FIRE IN CASTLE"
        else:
            self.notify_lv += 1


class Guard(Subject):
    _list_of_citizens: list = []
    _alarm: str = ''
    _escape: bool = False

    def attach(self, observer: Observer) -> None:
        self._list_of_citizens.append(observer)
        print(f' Welcome in castle {observer.__class__.__name__}')

    def detach(self, observer: Observer) -> None:
        self._list_of_citizens.remove(observer)
        print(f' See you later {observer.__class__.__name__}')

    def notify_observers(self):
        if self._escape:
            for observer in self._list_of_citizens:
                self.detach(observer)
        else:
            for observer in self._list_of_citizens:
                observer.update(self)
                print(self._alarm)


if __name__ == '__main__':
    farmer = Vilager1()
    monk = Vilager2()
    fishman = Vilager3()
    old_woman = Vilager4()
    guard_on_wall = Guard()
    guard_on_wall.attach(farmer)
    guard_on_wall.attach(monk)
    guard_on_wall.attach(fishman)
    guard_on_wall.attach(old_woman)
    for i in range(8):
        guard_on_wall.notify_observers()
