from typing import List
from daos.client_dao import ClientDAO
from entities.client import Client
from exceptions.not_found_exception import ResourceNotFoundError
from utils.connection_util import connection


class ClientDaoPostgres(ClientDAO):
    def create_client(self, client: Client) -> Client:
        sql = """insert into client(client_name, join_date) values (%s,%s) returning client_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (client.client_name,client.join_date))
        connection.commit()
        c_id = cursor.fetchone()[0]
        client.client_id = c_id
        return client

    def get_client_by_id(self, client_id: int) -> Client:
        sql = """select * from client where client_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        record = cursor.fetchone()
        client = Client(*record)
        return client

    def get_all_clients(self) -> List[Client]:
        sql = """select * from client"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        client_list = []
        for record in records:
            client_list.append(Client(*record))

        return client_list

    def update_client(self, client: Client) -> Client:
        sql = """update client set client_name=%s, join_date=%s where client_id =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [client.client_name, client.join_date, client.client_id])
        connection.commit()
        return client

    def delete_client(self, client_id: int) -> bool:
        sql = """delete from client where client_id =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()
        return True
