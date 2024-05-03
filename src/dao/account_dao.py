from ..models.account import Account
from ..config.my_connection import MyConnection
from src.dao.dao import Dao
class AccountDao (Dao[Account]):
    __db = None
    def __init__(self):
        self.__db = MyConnection()
    def find_all(self):
        donnees_recuperees = self.__db.query(
            'SELECT * FROM Account', None).fetchall()
        Accounts = [Account(id, cle, salt, type_acc, user_id)
                    for id, cle, salt, type_acc, user_id in donnees_recuperees]
        return Accounts
    def save(self, Account: Account) -> Account:
        pass
    def find_by_id(self, t: int) -> Account:
        pass
    def update(self, t: Account) -> Account:
        pass
    def remove(self, t: Account) -> None:
        pass