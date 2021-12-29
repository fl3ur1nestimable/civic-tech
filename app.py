"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Flask


# Import personal modules



# Definition of the app
def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = '29FTh4Swfr3DuMlNRcQcZxCk7IFBMooP'

    # Import blueprints
    ## Import main blueprint
    from py.blueprints.mainBP import mainBP
    app.register_blueprint(mainBP)

    ## Import login blueprint
    from py.blueprints.loginBP import loginBP
    app.register_blueprint(loginBP)

    ## Import programm blueprint
    from py.blueprints.programBP import programBP
    app.register_blueprint(programBP)

    ## Import one program blueprint
    from py.blueprints.progFullBP import progFullBP
    app.register_blueprint(progFullBP)

    ## Import redirects blueprint
    from py.blueprints.redirectsBP import redirectsBP
    app.register_blueprint(redirectsBP)

    ## Import delete blueprint
    from py.blueprints.deleteBP import deleteBP
    app.register_blueprint(deleteBP)

    return app


# Start app if file is not imported
if __name__ == "__main__":
    app = create_app()
    app.run(debug=1, host='0.0.0.0', port=5454)
