from typing import List

from daos.account_dao import AccountDAO
from entities.account import Account
from services.account_services import AccountServices


class AccountServicesImpl(AccountServices):
    def __init__(self, account_dao: AccountDAO):
        self.account_dao = account_dao

    def add_account(self, account: Account):
        return self.account_dao.create_account(account)

    def retrieve_all_accounts(self, user_id: int):
        return self.account_dao.get_all_accounts()

    def retrieve_account_by_id(self, account_id: int, user_id: int):
        return self.account_dao.get_account_by_id(account_id)

    def update_account(self, account: Account):
        return self.account_dao.update_account(account)

    def remove_account(self, account_id: int, user_id: int):
        return self.account_dao.delete_account(account_id)

    def withdraw_or_deposit(self, account: Account, user_id: int, amount: int, w_or_d: bool):
        if w_or_d:
            account.account_balance - amount
        else:
            account.account_balance + amount
        self.account_dao.update_account(account)
        return account

    def transfer_between_accounts(self, account1: Account, account2: Account, user_id: int, amount: int) -> List[Account]:
        account1.account_balance -= amount
        account2.account_balance += amount
        self.account_dao.update_account(account1)
        self.account_dao.update_account(account2)
        return [account1, account2]
