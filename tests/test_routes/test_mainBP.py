"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 04/01/2021
"""

# Import needed modules
import pathlib, sys

from werkzeug.wrappers import response

# Add parent dir to the path
cwd = pathlib.Path(__file__).parents[2]
parentdir = str(cwd)
sys.path.append(parentdir)


# Import personal modules
from app import create_app


def test_mainRoute():
    flask_app = create_app()

    test1 = "Bienvenue"
    test2 = "Les Cartes"
    test3 = "Les Statistiques"
    test4 = "Nom du Candidat"

    tests = [test1, test2, test3, test4]


    with flask_app.test_client() as test_client:
        response = test_client.get('/home')

        assert response.status_code == 200

        for test in tests:
            assert test in response.data.decode('utf-8')