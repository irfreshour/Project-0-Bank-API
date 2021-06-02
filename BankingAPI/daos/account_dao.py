from abc import ABC, abstractmethod
from typing import List

from entities.account import Account


class AccountDAO(ABC):

    # Create
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    # Read
    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_all_accounts(self) -> List[Account]:
        pass

    # Update
    @abstractmethod
    def update_account(self, account: Account) -> Account:
        pass

    # Delete
    @abstractmethod
    def delete_account(self, account_id: int) -> bool:
        pass
