from typing import List

from daos.client_dao import ClientDAO
from entities.client import Client


class ClientDaoLocal(ClientDAO):
    id_maker = 0
    client_table = {}

    def create_client(self, client: Client) -> Client:
        ClientDaoLocal.id_maker += 1
        client.client_id = ClientDaoLocal.id_maker
        ClientDaoLocal.client_table[ClientDaoLocal.id_maker] = client
        return client

    def get_client_by_id(self, client_id: int) -> Client:
        client = ClientDaoLocal.client_table[client_id]
        return client

    def get_all_clients(self) -> List[Client]:
        client_list = list(ClientDaoLocal.client_table.values())
        return client_list

    def update_client(self, client: Client) -> Client:
        ClientDaoLocal.client_table[client.client_id] = client
        return client

    def delete_client(self, client_id: int) -> bool:
        try:
            del ClientDaoLocal.client_table[client_id]
            return True
        except KeyError:
            return False
