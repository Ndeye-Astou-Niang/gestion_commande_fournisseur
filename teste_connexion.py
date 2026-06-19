"""
Script de test pour vérifier la connexion à la base de données
et la création des tables
"""
from Data_base.connexion import DatabaseConnection
from Data_base.config import TYPE_BD

def test_connexion():
    """Teste la connexion à la base de données"""
    print("\n" + "=" * 50)
    print("   TEST DE CONNEXION À LA BASE DE DONNÉES")
    print("=" * 50)

    db = DatabaseConnection()

    # Tentative de connexion
    print(f"\n1. Tentative de connexion à {TYPE_BD}...")
    if db.connect():
        print("   CONNEXION RÉUSSIE !")

        # Afficher les informations de connexion
        print(f"\n   Informations :")
        print(f"   - Type : {TYPE_BD}")

        db.disconnect()
        return True
    else:
        print("   ÉCHEC DE LA CONNEXION !")
        print("\n   Vérifiez :")
        print("   - Le service PostgreSQL/MySQL est démarré")
        print("   - Les identifiants dans config.py sont corrects")
        print("   - La base de données 'bibliotheque' existe")
        return False


def main():
    """Fonction principale de test"""
    print("\n" + "=" * 25)
    print("   TEST COMPLET DE LA BASE DE DONNÉES")
    print("=" * 25)

    # 1. Tester la connexion
    if not test_connexion():
        print("\nArrêt des tests - Connexion échouée")
        return


if __name__ == "__main__":
    main()