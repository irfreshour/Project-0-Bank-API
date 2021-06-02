from daos.client_dao import ClientDAO
from daos.client_dao_local import ClientDaoLocal
from daos.client_dao_postgres import ClientDaoPostgres
from entities.client import Client

client_dao: ClientDAO = ClientDaoPostgres()

test_client = Client(0, "Real Personson", 0)


def test_create_client():
    client_dao.create_client(test_client)
    assert test_client.client_id != 0


def test_get_client_by_id():
    client = client_dao.get_client_by_id(test_client.client_id)
    assert test_client.client_name == client.client_name


def test_update_client():
    test_client.client_name = "Fake Personson"
    updated_client = client_dao.update_client(test_client)
    assert updated_client.client_name == test_client.client_name


def test_delete_client():
    result = client_dao.delete_client(test_client.client_id)
    assert result


def test_get_all_clients():
    client1 = Client(0, "Numbuh One", 0)
    client2 = Client(0, "Numbuh Two", 0)
    client3 = Client(0, "Numbuh Three", 0)
    client_dao.create_client(client1)
    client_dao.create_client(client2)
    client_dao.create_client(client3)
    clients = client_dao.get_all_clients()
    assert len(clients) >= 3
