from typing import List

from daos.account_dao import AccountDAO
from entities.account import Account


class AccountDaoLocal(AccountDAO):
    id_maker = 0
    account_table = {}

    def create_account(self, account: Account) -> Account:
        AccountDaoLocal.id_maker += 1
        account.account_id = AccountDaoLocal.id_maker
        AccountDaoLocal.account_table[AccountDaoLocal.id_maker] = account
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        account = AccountDaoLocal.account_table[account_id]
        return account

    def get_all_accounts(self) -> List[Account]:
        account_list = list(AccountDaoLocal.account_table.values())
        return account_list

    def update_account(self, account: Account) -> Account:
        AccountDaoLocal.account_table[account.account_id] = account
        return account

    def delete_account(self, account_id: int) -> bool:
        try:
            del AccountDaoLocal.account_table[account_id]
            return True
        except KeyError:
            return False
