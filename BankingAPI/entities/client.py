from typing import List


class Client:
    def __init__(self, client_id: int, client_name: str, join_date: int):
        self.client_id = client_id
        self.client_name = client_name
        self.join_date = join_date

    def __str__(self):
        return f"id={self.client_id}, owner={self.client_name}, joined={self.join_date}"

    def as_json_dict(self):
        return {
            "clientId": self.client_id,
            "clientName": self.client_name,
            "joinDate": self.join_date
        }
