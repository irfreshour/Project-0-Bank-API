from abc import ABC, abstractmethod
from typing import List

from entities.client import Client


class ClientDAO(ABC):

    # Create
    @abstractmethod
    def create_client(self, client: Client) -> Client:
        pass

    # Read
    @abstractmethod
    def get_client_by_id(self, client_id: int) -> Client:
        pass

    @abstractmethod
    def get_all_clients(self) -> List[Client]:
        pass

    # Update
    @abstractmethod
    def update_client(self, client: Client) -> Client:
        pass

    # Delete
    @abstractmethod
    def delete_client(self, client_id: int) -> bool:
        pass
