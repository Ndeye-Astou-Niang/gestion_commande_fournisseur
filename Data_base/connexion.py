import psycopg2
import mysql.connector

from Data_base.config import TYPE_BD, MYSQL

"from database.config import TYPE_BD, MYSQL, POSTGRES"


class DatabaseConnection:
    # Singleton
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.cursor = None
        return cls._instance

    def connect(self):
        """Établir connexion à la base de données"""
        try:
            if TYPE_BD == "mysql":
                self.connection = mysql.connector.connect(
                    host=MYSQL["host"],
                    port=MYSQL["port"],
                    database=MYSQL["database"],
                    user=MYSQL["user"],
                    password=MYSQL["password"]
                )
            else:
                print("TYPE_BD invalide")
                return False

            self.cursor = self.connection.cursor()
            return True

        except Exception as e:
            print(f"Erreur de connexion : {e}")
            return False

    def disconnect(self):
        """Fermer connexion"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def commit(self):
        """Valider transaction"""
        if self.connection:
            self.connection.commit()

    def rollback(self):
        """Annuler transaction"""
        if self.connection:
            self.connection.rollback()

    def execute(self, query, params=None):
        """Exécuter une requête SQL"""
        try:
            self.cursor.execute(query, params or ())
            return True
        except Exception as e:
            print(f"Erreur SQL : {e}")
            return False

    def fetchall(self):
        """Récupérer tous les résultats"""
        return self.cursor.fetchall()

    def fetchone(self):
        """Récupérer un seul résultat"""
        return self.cursor.fetchone()