class Account:
    def __init__(self, account_id: int, account_type: str, account_balance: int, date_opened: int, owner_id: int):
        self.account_id = account_id
        self.account_type = account_type
        self.account_balance = account_balance
        self.date_opened = date_opened
        self.owner_id = owner_id

    def __str__(self):
        return f"id={self.account_id}, type={self.account_type}, balance={self.account_balance}, opened={self.date_opened}"

    def as_json_dict(self):
        return {
            "accountId": self.account_id,
            "accountType": self.account_type,
            "accountBalance": self.account_balance,
            "dateOpened": self.date_opened,
            "ownerId": self.owner_id
        }
