from ..models.user import User
from ..config.my_connection import MyConnection
from src.dao.dao import Dao


class UserDao (Dao[User]):
    __db = None

    def __init__(self):
        self.__db = MyConnection()

    def find_all(self):
        donnees_recuperees = self.__db.query(
            'SELECT * FROM User', None).fetchall()
        Users = [User(user_id, nom, prenom, email, mdpa, mdpp)
                 for user_id, nom, prenom, email, mdpa, mdpp in donnees_recuperees]
        return Users

    def save(self, User: User) -> User:
        pass

    def find_by_id(self, t: int) -> User:
        pass

    def update(self, t: User) -> User:
        pass

    def remove(self, t: User) -> None:
        pass
