from daos.account_dao import AccountDAO
from daos.account_dao_local import AccountDaoLocal
from daos.account_dao_postgres import AccountDaoPostgres
from entities.account import Account

account_dao: AccountDAO = AccountDaoPostgres()

test_account = Account(0, "savings", 5, 0, 0)


def test_create_account():
    account_dao.create_account(test_account)
    assert test_account.account_id != 0


def test_get_account_by_id():
    account = account_dao.get_account_by_id(test_account.account_id)
    assert test_account.account_type == account.account_type


def test_update_account():
    test_account.account_type = "checking"
    updated_account = account_dao.update_account(test_account)
    assert updated_account.account_type == test_account.account_type


def test_delete_account():
    result = account_dao.delete_account(test_account.account_id)
    assert result


def test_get_all_accounts():
    account1 = Account(0, "savings", 5, 0, 0)
    account2 = Account(0, "checking", 5, 0, 0)
    account3 = Account(0, "retirement", 5, 0, 0)
    account_dao.create_account(account1)
    account_dao.create_account(account2)
    account_dao.create_account(account3)
    accounts = account_dao.get_all_accounts()
    assert len(accounts) >= 3
