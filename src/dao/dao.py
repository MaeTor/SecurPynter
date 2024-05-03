from typing import TypeVar, Generic, Iterable
from abc import ABC, abstractmethod
T = TypeVar('T')

class Dao (Generic[T], ABC):
    @abstractmethod
    def save(self, t: T) -> T:
        pass
    @abstractmethod
    def find_all(self) -> Iterable:
        pass
    @abstractmethod
    def find_by_id(self, t: int) -> T:
        pass
    @abstractmethod
    def update(self, t: T) -> T:
        pass
    @abstractmethod
    def remove(self, t: T) -> None:
        pass
