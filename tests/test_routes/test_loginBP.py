"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 05/01/2021
"""

# Import needed modules
import pathlib, sys
from flask import session


# Add parent dir to the path
cwd = pathlib.Path(__file__).parents[2]
parentdir = str(cwd)
sys.path.append(parentdir)


# Import personal modules
from app import create_app


def test_loginRoute():
    flask_app = create_app()

    test1 = "regagner la page d'accueil."
    test2 = "<strong>identifiants</strong>"
    test3 = "Informations de connexion"
    test4 = "Se souvenir de moi"

    tests = [test1, test2, test3, test4]


    with flask_app.test_client() as test_client:
        response = test_client.get('/login')

        assert response.status_code == 200

        for test in tests:
            assert test in response.data.decode('utf-8')


def test_logoutRoute():
    flask_app = create_app()

    test1 = "Catégorie socio-professionnelle"
    test2 = """Les statistiques du candidat montrent le pourcentage d'intérêt porté au thème en question dans le programme du candidat. Trois 
                                thèmes sont représentés : l'environnement, l'économie et le social."""
    test3 = "Les Statistiques"
    test4 = "Présentation du candidat"

    tests = [test1, test2, test3, test4]


    with flask_app.test_client() as test_client:
        response = test_client.get('/logout')

        assert response.status_code == 200

        assert session['id'] == None

        for test in tests:
            assert test in response.data.decode('utf-8')
        

def test_profileRoute():
    flask_app = create_app()

    getTest1 = """<div class="submit-button">
                        <button class="btn btn-danger bg-danger">Enregister les modifications</button>
                    </div>"""
    getTest2 = """<div class="card">
            <div class="profile-container">"""
    getTest3 = """<div class="border border-4 border-danger">
                        <h2 class="text-center">Profil de Thibault Cheneviere</h2>
                    </div>"""

    getTest = [getTest1, getTest2, getTest3]

    with flask_app.test_client() as test_client:
        getResponse = test_client.get('/profile/Thibault/Cheneviere/1')

        assert getResponse.status_code == 200

        for test in getTest:
            assert test in getResponse.data.decode('utf-8')