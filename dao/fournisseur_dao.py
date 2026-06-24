from models.fournisseur import Fournisseur
from Data_base.connexion import DatabaseConnection

class FournisseurDAO:
    # Ajouter un Fournisseur
    def ajouter_fournisseur(self, fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            print("Pas de connection")
            return False
        sql = """
        INSERT INTO fournisseur(code, raison_social, email, telephone, adresse, date_creation)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (fournisseur.code,fournisseur.raison_social,fournisseur.email,fournisseur.telephone,
                  fournisseur.adresse,fournisseur.date_creation)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok
    # Lister tous les Fournisseur0
    def lister_fournisseur(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM fournisseur"
        db.execute(sql)
        resultats = db.fetchall()
        db.disconnect()
        fournisseurs = []
        for ligne in resultats:
            fournisseur = Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_social=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )
            fournisseurs.append(fournisseur)
        return fournisseurs

    # Rechercher un fournisseur
    def rechercher_fournisseur(self, mot_cle): # Soit auteur oubien le titre
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM fournisseur WHERE code = %s or raison_social = %s"
        params = (mot_cle,mot_cle,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Fournisseur(*ligne)
        return None

    # Supprimer un Fournisseur
    def supprimer_fournisseur(self, id):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "DELETE FROM fournisseur WHERE id=%s"
        params = (id,)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Modifier un Fournisseur
    def modifier_fournisseur(self, fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = """
        UPDATE fournisseur
        SET code=%s, raison_social=%s, email=%s, telephone=%s, adresse=%s, date_creation=%s
        WHERE id = %s
        """
        params = (fournisseur.code,fournisseur.raison_social,fournisseur.email,
                  fournisseur.telephone,fournisseur.adresse,fournisseur.date_creation)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Trouver le fournisseur par son ID
    def get_by_id(self, id):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM fournisseur WHERE id = %s"
        params = (id,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_social=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )
        return None




