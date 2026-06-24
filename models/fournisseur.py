class Fournisseur:
    def __init__(self, id=None, code="", raison_social="", email="", telephone="", adresse="", date_creation=""):
        self.id = id
        self.code = code
        self.raison_social = raison_social
        self.email = email
        self.telephone = telephone
        self.adresse = adresse
        self.date_creation = date_creation

    def __str__(self):
        return f"{self.id} - {self.code} - {self.raison_social} - {self.email} - {self.telephone}- {self.adresse}- {self.date_creation}"

    def afficher(self):
        print(f"ID : {self.id}")
        print(f"Code : {self.code}")
        print(f"Raison social : {self.raison_social}")
        print(f"Email : {self.email}")
        print(f"Telephone : {self.telephone}")
        print(f"Adresse : {self.adresse}")
        print(f"Date creation : {self.date_creation}")