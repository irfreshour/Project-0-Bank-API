from abc import ABC, abstractmethod

from entities.account import Account


class AccountServices(ABC):
    @abstractmethod
    def add_account(self, account: Account):
        pass

    @abstractmethod
    def retrieve_all_accounts(self, user_id: int):
        pass

    @abstractmethod
    def retrieve_account_by_id(self, account_id: int, user_id: int):
        pass

    @abstractmethod
    def update_account(self, account: Account):
        pass

    @abstractmethod
    def remove_account(self, account_id: int, user_id: int):
        pass

    @abstractmethod
    def withdraw_or_deposit(self, account: Account, user_id: int, amount: int, w_or_d: bool) -> Account:
        pass

    @abstractmethod
    def transfer_between_accounts(self, account1: Account, account2: Account, user_id: int, amount: int) -> Account:
        pass
