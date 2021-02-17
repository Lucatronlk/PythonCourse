from abc import ABC,abstractmethod
from typing import List


class TaskStore(ABC):
    @abstractmethod
    def get_all(self) -> List[dict]:
        pass






