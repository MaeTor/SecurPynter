class Account:
    def __init__(self, id, cle, salt, type_acc, user_id ):
        self.id = id
        self.cle = cle
        self.salt = salt
        self.type_acc = type_acc
        self.user_id = user_id

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_cle(self):
        return self.cle

    def set_cle(self, value):
        self.cle = value

    def get_salt(self):
        return self.salt

    def set_salt(self, value):
        self.salt = value

    def get_type_acc(self):
        return self.type_acc

    def set_type_acc(self, value):
        self.type_acc = value

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, value):
        self.user_id = value
    
    def __str__(self):
        return f"{self.id}, {self.cle}, {self.salt}, {self.type_acc}, {self.user_id}"
