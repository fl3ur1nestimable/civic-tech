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


def test_redirectRoute():
    flask_app = create_app()

    test1 = """<title>Profil de Thibault Cheneviere</title>"""
    test2 = """<div class="input-picture">
                        <label class="picInput" for="picInputId">Photo de Profil : </label>
                        <input class="form-input" name="picture" type="file" accept="image/*" placeholder="Choisissez votre photo de profil">
                    </div>"""
    test3 = """<div class="submit-button">
                        <button class="btn btn-danger bg-danger">Enregister les modifications</button>
                    </div>"""

    testsWalking = [test1, test2, test3]

    with flask_app.test_client() as test_client:
        responseWalking = test_client.get('/r/profile/1', follow_redirects=True)

        assert responseWalking.status_code == 200

        for test in testsWalking:
            assert test in responseWalking.data.decode('utf-8')