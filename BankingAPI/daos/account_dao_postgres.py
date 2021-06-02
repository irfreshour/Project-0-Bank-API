from typing import List

from daos.account_dao import AccountDAO
from entities.account import Account
from utils.connection_util import connection


class AccountDaoPostgres(AccountDAO):
    def create_account(self, account: Account) -> Account:
        sql = """insert into account(account_type, account_balance, date_opened, owner_id) values (%s,%s,%s,%s) returning account_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_type, account.account_balance, account.date_opened, account.owner_id))
        connection.commit()
        a_id = cursor.fetchone()[0]
        account.account_id = a_id
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        sql = """select * from account where account_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        record = cursor.fetchone()
        account = Account(*record)
        return account

    def get_all_accounts(self) -> List[Account]:
        sql = """select * from account"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        account_list = []
        for record in records:
            account_list.append(Account(*record))

        return account_list

    def update_account(self, account: Account) -> Account:
        sql = """update account set account_type=%s, account_balance=%s, date_opened=%s, owner_id=%s where account_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_type, account.account_balance, account.date_opened, account.owner_id, account.account_id])
        connection.commit()
        return account

    def delete_account(self, account_id: int) -> bool:
        sql = """delete from account where account_id =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True
