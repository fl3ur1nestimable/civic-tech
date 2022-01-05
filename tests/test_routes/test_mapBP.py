"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 05/01/2021
"""

# Import needed modules
import pathlib, sys

# Add parent dir to the path
cwd = pathlib.Path(__file__).parents[2]
parentdir = str(cwd)
sys.path.append(parentdir)


# Import personal modules
from app import create_app


def test_mapRoute():
    flask_app = create_app()

    test1 = """<h2 class="text-center">Chemin vers le bureau de vote le plus proche de chez vous</h2>"""
    test2 = """<div class="custom-card">    
            <div id='map'></div>
            <div id="instructions"></div>
        </div>"""
    test3 = """<title>Pour aller voter</title>"""
    test4 = """<div class="btn-group" role="group" aria-label="Basic radio toggle button group">
                    <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off">
                    <a href="/map/cycling" class="btn btn-outline-danger btn-lg">Vélo</a>
                
                    <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
                    <a href="/map/driving" class="btn btn-outline-danger btn-lg">Voiture</a>
                
                    <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off" checked>
                    <a href="/map/walking" class="btn btn-outline-danger btn-lg">Marche</a>
                </div>"""

    testsWalking = [test1, test2, test3, test4]

    with flask_app.test_client() as test_client:
        responseWalking = test_client.get('/map/walking')

        assert responseWalking.status_code == 200

        for test in testsWalking:
            assert test in responseWalking.data.decode('utf-8')