from flask import Flask, request, jsonify

from daos.account_dao_local import AccountDaoLocal
from daos.account_dao_postgres import AccountDaoPostgres
from daos.client_dao_local import ClientDaoLocal
from daos.client_dao_postgres import ClientDaoPostgres
from entities.account import Account
from entities.client import Client
from exceptions.not_found_exception import ResourceNotFoundError
from services.account_services_impl import AccountServicesImpl
from services.client_services_impl import ClientServicesImpl

app: Flask = Flask(__name__)
import logging

app: Flask = Flask(__name__)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')

client_dao = ClientDaoPostgres()
client_service = ClientServicesImpl(client_dao)
account_dao = AccountDaoPostgres()
account_service = AccountServicesImpl(account_dao)


@app.route("/clients", methods=["POST"])
def add_client():
    body = request.json
    client = Client(body["clientId"], body["owner"], body["joined"])
    client_service.add_client(client)
    return f"Created client with id{client.client_id}", 201


@app.route("/clients", methods=["GET"])
def get_all_clients():
    clients = client_service.retrieve_all_clients()  # list of books
    json_clients = [c.as_json_dict() for c in clients]  # list json dict
    return jsonify(json_clients), 200


@app.route("/clients/<client_id>", methods=["GET"])
def retrieve_client_by_id(client_id: str):
    client = client_service.retrieve_client_by_id(int(client_id))
    return jsonify(client.as_json_dict())


@app.route("/clients/<client_id>", methods=["PUT"])
def update_client(client_id: str):
    body = request.json
    client = Client(body["clientId"], body["owner"], body["joined"])
    client.client_id = (int(client_id))
    client_service.update_client(client)
    return "updated successfully"


@app.route("/clients/<client_id>", methods=["DELETE"])
def remove_client(client_id: str):
    client_service.remove_client(int(client_id))
    return "Deleted successfully", 200


@app.route("/clients/<client_id>/accounts", methods=["POST"])
def add_account(client_id: str):
    body = request.json
    account = Account(body["accountId"], body["accountType"], body["accountBalance"], body["dateOpened"],
                      body["ownerId"])
    account_service.add_account(account)
    return f"Created account with id{account.account_id}", 201


@app.route("/clients/<client_id>/accounts", methods=["GET"])
def retrieve_all_accounts(client_id: str):
    accounts = account_service.retrieve_all_accounts(int(client_id))
    json_accounts = [a.as_json_dict() for a in accounts]
    return jsonify(json_accounts)


@app.route("/clients/<client_id>/accounts/<account_id>", methods=["GET"])
def retrieve_account_by_id(client_id: str, account_id: str):
    account = account_service.retrieve_account_by_id(int(account_id), int(client_id))
    return jsonify(account.as_json_dict())


@app.route("/clients/<client_id>/accounts/<account_id>", methods=["PUT"])
def update_account(client_id: str, account_id: str):
    body = request.json
    account = Account(body["clientId"], body["owner"], body["joined"])
    account_service.add_account(account)
    return "updated successfully"


@app.route("/clients/<client_id>/accounts/<account_id>", methods=["DELETE"])
def remove_account(client_id: str, account_id: str):
    account_service.remove_account(int(account_id), int(client_id))
    return "Deleted successfully", 200


@app.route("/clients/<client_id>/accounts/<account_id>", methods=["PATCH"])
def withdraw_or_deposit(account_id: int, client_id: str):
    body = request.json
    w_or_d = True
    amount = ""
    if "withdraw" in body:
        w_or_d = True
        amount = body["withdraw"]
    elif "deposit" in body:
        w_or_d = False
        amount = body["deposit"]
    account = account_dao.get_account_by_id(account_id)
    account_service.withdraw_or_deposit(account, client_id, amount, w_or_d)
    return "Successfully withdrawn or deposited"


@app.route("/clients/<client_id>/accounts/<account_id_1>/transfer/<account_id_2>", methods=["PATCH"])
def transfer_between_accounts(account_id_1: str, account_id_2: str, client_id: str):
    body = request.json
    amount = body["amount"]
    account1 = account_dao.get_account_by_id(account_id_1)
    account2 = account_dao.get_account_by_id(account_id_2)
    account_service.transfer_between_accounts(account1, account2, client_id, amount)
    return "Successfully transferred"


if __name__ == '__main__':
    app.run()
