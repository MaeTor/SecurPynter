class User:
    def __init__(self, user_id, nom, prenom, email, mdpa, mdpp):
        self.user_id = user_id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mdpa = mdpa
        self.mdpp = mdpp

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, value):
        self.user_id = value

    def get_nom(self):
        return self.nom

    def set_nom(self, value):
        self.nom = value

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, value):
        self.prenom = value

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    def get_mdpa(self):
        return self.mdpa

    def set_mdpa(self, value):
        self.mdpa = value

    def get_mdpp(self):
        return self.mdpp

    def set_mdpp(self, value):
        self.mdpp = value
    
    def __str__(self):
        return f"{self.user_id} {self.nom} {self.prenom} {self.email} {self.mdpa} {self.mdpp}"
