from unittest.mock import MagicMock

from daos.account_dao_postgres import AccountDaoPostgres
from entities.account import Account
from services.account_services import AccountServices
from services.account_services_impl import AccountServicesImpl

accounts = [Account(0, "savings", 700, 0, 0),
            Account(0, "checking", 9999, 0, 0),
            Account(0, "retirement", 1234, 0, 0)]

mock_dao = AccountDaoPostgres()
mock_dao.get_all_accounts = MagicMock(return_value=accounts)
accounts = mock_dao.get_all_accounts()

account_services: AccountServices = AccountServicesImpl(mock_dao)


def withdraw_or_deposit_test():
    result = account_services.withdraw_or_deposit(accounts[0], 0, 50, True)
    assert result == Account(0, "savings", 750, 0, 0)


def transfer_between_accounts_test():
    result = account_services.transfer_between_accounts(accounts[1], accounts[2], 0, 3)
    assert result[0] == Account(0, "checking", 9996, 0, 0)
    assert result[1] == Account(0, "retirement", 1237, 0, 0)
